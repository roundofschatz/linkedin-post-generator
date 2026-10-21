# Changelog

Every change to this skill is logged here: what was added, changed or removed, and why. Nothing comes out without a line saying so. Newest first.

## 1.2.2 · One tone rule, everywhere

Why: 1.2.1's tone rule lives in SKILL.md, but `references/post-types.md` still told the skill to "cut what's vague" in a writer's own draft, which works against keeping their voice.

- Changed: the share post's line on the writer's own draft now points to Step 5's tone rule: keep their tone, framing and terms, and apply the tactics on top.
- Changed: the checker's version to 1.2.2.

## 1.2.1 · The writer's tone, built out with the tactics

Why: on October 21, 2026, the owner rewrote a post the skill drafted. The rewrite was more human, and the skill's earlier drafts had flattened his voice. He ruled that the skill should match the tone of voice it receives, and build it out with the tactics a high-quality post needs, rather than replace it or leave it untouched.

- Added: Step 5's tone rule. The skill matches the writer's words, phrasing, rhythm and formality, including choices a style rule would flag, and writes what each tactic needs (the fold, length, paragraphs, close, link, hashtags) in that style. It fixes errors, flags style questions in the notes, and makes the smallest change that meets a tactic.
- Changed: `tests/cases/share-own-work.md` checks the same.
- Changed: the checker's version to 1.2.1.

## 1.2.0 · Evidence over style rules

Why: 1.1.1 set aside a paragraph finding because it worked against Plainspeak Writer's style rule against one sentence per line, and 1.1.0 capped hashtags at two to match Plainspeak Writer. On October 21, 2026, the owner ruled that a style rule never outranks evidence of what works. Where `platform.md` has a finding, the skill follows it; its own choices cover only what the evidence leaves open.

- Changed: paragraphs. Posts with more than 14 paragraphs did 66% better than posts with fewer than 7 in one 400,000-post dataset, so paragraphs run one or two full sentences, a new one at each new point, usually 10 to 14 in a text post. P11 warns again under 7.
- Changed: hashtags. One to three relevant tags, following the only measure (1 to 3 gave about 9% more reach). P08 now blocks above three.
- Added: when a Plainspeak Writer rule works against a finding, the finding wins and the warning is cleared with the finding as the reason.
- Changed: the text-length choice now gives its evidence reason, not its fit with Plainspeak Writer.

## 1.1.1 · No paragraph-count target

Why: 1.1.0 asked for 8 to 12 paragraphs and warned under 7, after one vendor dataset found posts with more than 14 paragraphs did better. In a post of 1,300 to 2,500 characters, that many paragraphs means one short sentence per line, the layout Plainspeak Writer bars as an AI tell. The owner rejected it on October 21, 2026: the finding comes from one source with a private method, and it works against a settled voice rule.

- Changed: paragraphs run one to three full sentences, with no count to hit. `platform.md` keeps the finding and says why the skill doesn't follow it.
- Removed: P11, the under-7-paragraphs warning, and its test.
- Changed: the checker's version to 1.1.1.

## 1.1.0 · Posts that share the writer's own work

Why: the first real use, on October 21, 2026, was a post sharing the owner's own paper. The skill moved the link out of the post for reach, opened on one vivid case from deep in the paper that covered one of its three industries, and dropped facts into sentences as quick asides. The owner rejected all three. A post that exists to send readers to the writer's work needs the link, an opening that covers the whole piece, and the evidence left in the piece.

- Added: Step 3 now settles the post's job first: share the writer's own work, respond to someone else's source, or make a point of the writer's own. The job sets the link, the post type and the length.
- Added: a "sharing your own work" post in `references/post-types.md`: the piece's central point across its full scope, a preview of the argument, the link on its own line with the preview card removed, and the writer's own terms kept.
- Changed: the opening rule. The first line states the central point of the whole source or idea. An example opens only when the writer's point is that story.
- Added: one example, explained, or none. No fact tacked onto a sentence as an aside, and no run of facts.
- Changed: links follow the post's job. They stay in a post sharing the writer's work, the writer decides for someone else's source, and the cost moves to `platform.md` instead of the notes.
- Added: the scope test in Step 6.
- Added: `--type share` in `check_post.py`, and a new rule, P19, that blocks a share post with no link.

The same day, a fresh reviewer checked every rule against the research report the skill was built from, and found 46 places where the skill went past, against or short of it. Every requirement now rests on a finding at the strength the report gives it, or sits in a new list in `platform.md` of the skill's own choices, each with its reason.

- Changed: the opening. Story and contrarian openers did best in the data, so the skill now uses them, as long as they stand for the post's whole point. It used to bar stories.
- Changed: paragraphs. One dataset found posts with more than 14 paragraphs beat posts with fewer than 7. The skill now asks for paragraphs of one or two full sentences, usually 8 to 12, and P11 warns under 7. P11 used to flag the short-paragraph shape the data favors.
- Changed: a post sharing the writer's own work runs 1,300 to 1,900 characters, like a text post, since that range did best. Its earlier 700 to 1,200 had no source.
- Added: remove the link-preview card, which roughly halved reach in one study, and offer a document post when the piece would fill slides.
- Added: Step 3 checks the post's subject against the writer's two or three core subjects when known. The report rates staying in a lane as strongly supported.
- Added: a clear, arguable opinion counts as the writer's angle, as the report says.
- Changed: posting advice now says to reply to every serious comment for 30 to 60 minutes and not to use comment tools or engagement groups.
- Changed: `platform.md` rewritten against the report: the link cost as the studies give it, not a rounded range; the AI-slop numbers with their caveats; hook data marked secondary; frequency marked as disputed; poll limits with their source; the skill's own choices listed.
- Changed: the script. Only LinkedIn's named bait blocks (P07); other bait warns (P20). Hashtags block above two, matching the stated cap. "It's not X, it's Y" now blocks (P14), since LinkedIn said it cut reach for it. Greeting openers and Unicode letters now warn. The opening check measures the first sentence across lines. Links are found on any domain. The stock-line rule (P15) is gone; it had no source and flagged contrarian openers the data favors.
- Added: never quote from a web tool's summary of a page; quote only text the user pasted or the tool returned word for word. A rerun quoted a line from a summary.
- Removed: "open in the first five seconds" for video, and "readers save these" for documents, neither in the research.
- Added: `tests/cases/share-own-work.md`, the case that found these problems, to rerun after changes.

## 1.0.0 · First release

Why: LinkedIn rebuilt its feed in 2026. It now matches posts to readers by meaning, cuts generic and AI-sounding posts, and cuts engagement bait. Advice written before 2026, like stacking hashtags, no longer holds. This skill builds a post from source material for the feed as it works now.

- Added: `SKILL.md`, seven steps from reading the source to delivering the post. The writer's own angle is required, and the skill asks for it rather than inventing one.
- Added: `references/platform.md`, what LinkedIn rewards and cuts, from 2026 sources only (one dated 2025 statement is marked as such). Each rule carries its evidence: LinkedIn's own word, a large study, or opinion. Last checked October 21, 2026.
- Added: `references/sources.md`, how to read links, ideas, documents, images, transcripts and other people's posts, and how to credit them.
- Added: `references/post-types.md`, when to use text, a PDF carousel, images, a poll or a video, and what each needs.
- Added: `references/writing.md`, writing rules for when Plainspeak Writer isn't installed.
- Added: `scripts/check_post.py`, 18 rules for length, the opening line, hashtags, links, engagement bait, stock lines and poll limits, with tests in `tests/test_check_post.py`.
- Set: a text post aims for 1,300 to 1,900 characters. 2026 data favors 1,300 to 2,500, and Plainspeak Writer's LinkedIn guide sets 150 to 300 words; this range fits both. Hashtags are capped at two, also to match Plainspeak Writer.

Tested before release: three runs by fresh agents that saw only the skill and the request. An article with the writer's own result produced a 1,602-character post that passed both checks. A topic with no angle produced a single message asking for the writer's case, number or view, with no post written. A survey PDF with the writer's own number produced a carousel post with a nine-slide outline. Twelve unclear steps the runs reported were fixed: how the angle question reads for a bare topic, which skill sets the length and the reply when both are installed, what the fact check sees, an unnamed source, the reply's order, and the run command.
