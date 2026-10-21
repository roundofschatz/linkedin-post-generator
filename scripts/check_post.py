#!/usr/bin/env python3
"""Check a LinkedIn post against what LinkedIn's feed rewards and punishes.

    python scripts/check_post.py post.txt
    python scripts/check_post.py --type document post.txt
    python scripts/check_post.py --type poll --poll poll.txt post.txt
    python scripts/check_post.py --link-ok post.txt
    python scripts/check_post.py --list-rules

The check reads the post as LinkedIn shows it: the character count includes
spaces and line breaks, and the opening is the first line a reader sees
before "see more". It finds surface patterns only: length, the opening,
paragraph count, hashtags, links and engagement bait. Whether the
post says something worth reading is the edit's job, not this script's.

HARD rules block the post. WARN rules stay only with a stated reason.
Exit code 1 when anything blocks.

The numbers come from references/platform.md, which says where each one
comes from and when it was checked. Change them there first, then here.

Standard library only.
"""
import argparse
import re
import sys
from pathlib import Path

__version__ = "1.2.0"

# Limits and targets. Each number is in references/platform.md, as a
# finding with its source or in "The skill's own choices".
POST_LIMIT = 3000          # LinkedIn's limit on a post
SEE_MORE_DESKTOP = 210     # about where desktop folds the post
SEE_MORE_MOBILE = 140      # about where mobile folds the post
TEXT_RANGE = (1300, 1900)  # skill's choice, inside the 1,300-2,500 that did best
SHORT_RANGE = (150, 1300)  # skill's choice: text over a document, images, a poll or a video
POLL_QUESTION = 140        # LinkedIn's limits
POLL_OPTION = 30
POLL_OPTIONS = (2, 4)
HASHTAG_MAX = 3            # 1-3 relevant tags helped in one measure
MIN_PARAGRAPHS = 7         # posts with fewer than 7 paragraphs did 66% worse (one dataset)
MENTION_MAX = 3            # skill's choice

TYPES = ("text", "share", "document", "images", "poll", "video")


def rule(rid, level, name, fix):
    return {"id": rid, "level": level, "name": name, "fix": fix}


RULES = [
    rule("P01", "HARD", "over LinkedIn's 3,000-character limit", "cut a point; LinkedIn won't post it"),
    rule("P02", "WARN", "length outside the target for this post type", "add the writer's argument or cut what repeats"),
    rule("P03", "HARD", "first line runs past the desktop fold (210 characters)", "state the point in the first 140 characters"),
    rule("P04", "WARN", "first sentence runs past the mobile fold (140 characters)", "state the point in the first 140 characters"),
    rule("P05", "WARN", "greeting or setup opener", "spend the first 140 characters on the point"),
    rule("P06", "WARN", "opens on a question", "open on a short story or a claim; question openers did worst in 2026 data"),
    rule("P07", "HARD", "engagement bait LinkedIn named", "end on a position or a specific question about a named case"),
    rule("P08", "HARD", "more than three hashtags", "use one to three that name the exact subject or a real community"),
    rule("P11", "WARN", "fewer than 7 paragraphs", "start a new paragraph at each new point, one or two full sentences each"),
    rule("P09", "WARN", "hashtag inside a sentence", "put hashtags on the last line"),
    rule("P10", "WARN", "link in the post", "ask the writer: keep it and accept the reach cost, or leave it out"),
    rule("P12", "WARN", "arrow or emoji bullets", "write the points as sentences, or as a plain list"),
    rule("P13", "WARN", "bold or italic Unicode letters", "use plain text; screen readers can't read these"),
    rule("P14", "HARD", "'it's not X, it's Y' or 'not just X, but Y'", "say the point straight; LinkedIn cuts reach for this shape"),
    rule("P16", "WARN", "more than three @mentions", "tag only people the post is about"),
    rule("P17", "HARD", "poll question or option over LinkedIn's limit", "140 characters for the question, 30 for each option"),
    rule("P18", "HARD", "poll needs two to four options", "give two, three or four options"),
    rule("P19", "HARD", "a post sharing the writer's own work has no link", "put the link on its own line after the body"),
    rule("P20", "WARN", "other engagement bait", "end on a position or a specific question about a named case"),
]
BY_ID = {r["id"]: r for r in RULES}

GREETING = re.compile(
    r"^\s*(?:hi|hey|hello|happy\s+(?:monday|tuesday|wednesday|thursday|friday|weekend|new\s+year)"
    r"|good\s+(?:morning|afternoon|evening)|dear\s+(?:network|connections|linkedin)"
    r"|in\s+today'?s\b|in\s+a\s+world\s+where|i'?ve\s+been\s+(?:thinking|reflecting)"
    r"|let'?s\s+talk\s+about|quick\s+(?:thought|question)|a\s+(?:quick\s+)?reminder"
    r"|(?:(?:i'?m|we'?re|i\s+am|we\s+are)\s+)?(?:so\s+)?(?:thrilled|excited|delighted|happy|proud)\s+to\s+(?:announce|share))\b",
    re.I)

# LinkedIn's named examples: "Comment 'Yes' if you agree", like-if lines,
# and typing a word to get something sent.
BAIT_NAMED = re.compile(
    r"\bcomment\s+['\"‘“]?\w+['\"’”]?\s+(?:if|and\s+i'?ll|below\s+(?:if|and))\b"
    r"|\b(?:type|comment|reply|drop)\s+['\"‘“]\w+['\"’”]"
    r"|\b(?:like|repost|share|react)\s+(?:this\s+)?if\b"
    r"|\bdm\s+me\s+['\"‘“]\w+",
    re.I)

# The skill's own list, beyond LinkedIn's examples.
BAIT_OTHER = re.compile(
    r"\bdrop\s+(?:a|an|your)\s+(?:comment|emoji|\S+\s+below)\b|\bcomment\s+below\b"
    r"|\brepost\s+(?:to|this\s+to)\s+help\b|♻️?\s*repost"
    r"|\bfollow\s+(?:me\s+)?for\s+more\b|\bhit\s+(?:the\s+)?(?:bell|follow)\b|\bsmash\s+that\b"
    r"|\btag\s+(?:someone|a\s+friend|a\s+colleague|\d+)\b"
    r"|\bwho\s+else\s+(?:has|is|agrees|feels)\b"
    r"|(?:^|[.!?\n]\s*)(?:agree|thoughts|right|yes\s+or\s+no)\s*\?",
    re.I | re.M)

NOT_X_Y = re.compile(
    r"\b(?:it'?s|this\s+is|that'?s|it\s+is|this\s+isn'?t|it\s+isn'?t)\s+not\s+(?:about\s+)?[^.?!\n]{1,60}?[,;:—-]\s*"
    r"(?:it'?s|it\s+is|this\s+is|that'?s)\b"
    r"|\bnot\s+just\s+[^.?!\n]{1,60}?,?\s+but\b"
    r"|\b(?:this|it)\s+isn'?t\s+about\s+[^.?!\n]{1,60}?[.;,]\s*(?:it'?s|this\s+is)\s+about\b",
    re.I)

ARROW = re.compile(r"^\s*(?:[→➡➔▶►•✔✅❌⭐✨⚡\U0001F449\U0001F525\U0001F4A1\U0001F4CC\U0001F680\U0001F4C8\U0001F4CA\U0001F539\U0001F538\U0001F536\U0001F537☑⏩]|\d️⃣)", re.M)
FANCY = re.compile(r"[\U0001D400-\U0001D7FF]")
HASHTAG = re.compile(r"(?<![\w#&/])#[A-Za-z][\w]*")
URL = re.compile(r"\bhttps?://\S+|\bwww\.\S+|(?<![@\w.])(?:[a-z0-9-]+\.)+[a-z]{2,12}(?:/\S*)?(?=[\s,;:!?)]|\.(?:\s|$)|$)", re.I)
MENTION = re.compile(r"(?<![\w@])@[A-Z][\w.-]*")


def paragraphs(text):
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def lines(text):
    return [l for l in text.splitlines() if l.strip()]


def line_no(text, index):
    return text.count("\n", 0, index) + 1


def snippet(s, n=70):
    s = " ".join(s.split())
    return s if len(s) <= n else s[: n - 1] + "…"


def check(text, post_type="text", link_ok=False, poll=None, skip=()):
    hits = []

    def hit(rid, where, what):
        if rid not in skip:
            hits.append((rid, where, what))

    body = text.strip()
    n = len(body)

    if n > POST_LIMIT:
        hit("P01", "-", f"{n:,} characters")
    lo, hi = TEXT_RANGE if post_type in ("text", "share") else SHORT_RANGE
    if not lo <= n <= hi:
        hit("P02", "-", f"{n:,} characters; the target for a {post_type} post is {lo:,} to {hi:,}")

    first = lines(body)[0] if body else ""
    if len(first) > SEE_MORE_DESKTOP:
        hit("P03", "line 1", f"{len(first)} characters: {snippet(first)}")
    else:
        m = re.search(r"[.!?](?=\s|$)", body)
        lead = body[: m.end()] if m else body
        if len(lead) > SEE_MORE_MOBILE:
            hit("P04", "line 1", f"{len(lead)} characters: {snippet(lead)}")
    if GREETING.search(first):
        hit("P05", "line 1", snippet(first))
    first_sentence = re.split(r"(?<=[.!?])\s", first, maxsplit=1)[0]
    if first_sentence.rstrip().endswith("?"):
        hit("P06", "line 1", snippet(first_sentence))

    for m in BAIT_NAMED.finditer(body):
        hit("P07", f"line {line_no(body, m.start())}", snippet(m.group(0).strip()))
    for m in BAIT_OTHER.finditer(body):
        hit("P20", f"line {line_no(body, m.start())}", snippet(m.group(0).strip()))

    tags = list(HASHTAG.finditer(body))
    if len(tags) > HASHTAG_MAX:
        hit("P08", "-", f"{len(tags)} hashtags")
    paras = paragraphs(body)
    all_lines = body.splitlines()
    for m in tags:
        line = all_lines[line_no(body, m.start()) - 1]
        if not re.fullmatch(r"(?:\s*#[A-Za-z]\w*[\s,]*)+", line):
            hit("P09", f"line {line_no(body, m.start())}", f"{m.group(0)} inside a sentence")

    if post_type == "share" and not URL.search(body):
        hit("P19", "-", "no link found")
    if not link_ok and post_type != "share":
        for m in URL.finditer(body):
            hit("P10", f"line {line_no(body, m.start())}", snippet(m.group(0), 50))


    for m in ARROW.finditer(body):
        hit("P12", f"line {line_no(body, m.start())}", snippet(body[m.start(): m.start() + 40]))
    m = FANCY.search(body)
    if m:
        hit("P13", f"line {line_no(body, m.start())}", snippet(body[max(0, m.start() - 10): m.start() + 30]))
    for m in NOT_X_Y.finditer(body):
        hit("P14", f"line {line_no(body, m.start())}", snippet(m.group(0)))
    if post_type in ("text", "share"):
        prose = [p for p in paras if not re.fullmatch(r"(?:\s*#[A-Za-z]\w*[\s,]*)+", p) and not URL.fullmatch(p)]
        if len(prose) < MIN_PARAGRAPHS:
            hit("P11", "-", f"{len(prose)} paragraphs")
    mentions = MENTION.findall(body)
    if len(mentions) > MENTION_MAX:
        hit("P16", "-", f"{len(mentions)} mentions")

    if poll is not None:
        plines = [l.strip() for l in poll.splitlines() if l.strip()]
        question, options = (plines[0], plines[1:]) if plines else ("", [])
        options = [re.sub(r"^[-*\d.)\s]+", "", o) for o in options]
        if len(question) > POLL_QUESTION:
            hit("P17", "poll", f"question is {len(question)} characters")
        for o in options:
            if len(o) > POLL_OPTION:
                hit("P17", "poll", f"option is {len(o)} characters: {snippet(o, 40)}")
        if not POLL_OPTIONS[0] <= len(options) <= POLL_OPTIONS[1]:
            hit("P18", "poll", f"{len(options)} options")
    return n, len(first), len(tags), hits


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check a LinkedIn post.")
    ap.add_argument("post", nargs="?", help="the post, as plain text")
    ap.add_argument("--type", choices=TYPES, default="text",
                    help="text, share, document, images, poll or video (default: text)")
    ap.add_argument("--poll", metavar="FILE", help="poll file: the question on line 1, one option per line after")
    ap.add_argument("--link-ok", action="store_true", help="the writer chose to keep a link in the post")
    ap.add_argument("--skip", default="", help="rule IDs to turn off, comma-separated, each with a stated reason")
    ap.add_argument("--list-rules", action="store_true")
    ap.add_argument("--version", action="version", version=f"check_post {__version__}")
    a = ap.parse_args(argv)

    if a.list_rules:
        for r in RULES:
            print(f"{r['id']}  {r['level']:4}  {r['name']}  ->  {r['fix']}")
        return 0
    if not a.post:
        ap.error("give the post file")
    text = Path(a.post).read_text(encoding="utf-8")
    poll = Path(a.poll).read_text(encoding="utf-8") if a.poll else None
    if a.type == "poll" and poll is None:
        ap.error("--type poll needs --poll FILE")
    skip = {s.strip().upper() for s in a.skip.split(",") if s.strip()}

    n, first, tags, hits = check(text, a.type, a.link_ok, poll, skip)
    hard = [h for h in hits if BY_ID[h[0]]["level"] == "HARD"]
    warn = [h for h in hits if BY_ID[h[0]]["level"] == "WARN"]
    print(f"check_post {__version__} | {a.type} post | {n:,} characters | opening line {first} | hashtags {tags}")
    if skip:
        print("turned off: " + ", ".join(sorted(skip)))
    for label, group in (("HARD", hard), ("WARN", warn)):
        for rid, where, what in group:
            r = BY_ID[rid]
            print(f"{label} {rid} {where}: {r['name']} | {what} | fix: {r['fix']}")
    print(f"{len(hard)} blocking, {len(warn)} warnings")
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
