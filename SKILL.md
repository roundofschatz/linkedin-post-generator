---
name: linkedin-post-generator
description: Turns source material into a LinkedIn post built for how LinkedIn's feed ranks posts in 2026. The source can be a link to an article or report, a plain idea or question, an uploaded PDF, Word file, slide deck, spreadsheet or image, pasted notes, a transcript, or someone else's post to answer. It reads the source in full, gets the writer's own angle, picks the post type (text, document carousel, images, poll or video), writes the post and checks it by script for length, the opening line, hashtags, links and engagement bait. Use whenever someone wants to write, draft, plan, fix or repurpose a LinkedIn post, or asks what to post about an article, report, event, project or idea, even if they never say "post."
license: MIT
---

# LinkedIn Post Generator

This skill turns what the user hands over into a LinkedIn post that LinkedIn's 2026 feed will show to the right readers. The work runs in order: read the source, list the facts, get the writer's angle, pick the post type, write, check, then deliver. What LinkedIn rewards and cuts, with the evidence for each rule, is in `references/platform.md`.

## Rules above everything

1. **Never invent a fact.** No name, number, quote, date, client, result or experience goes in the post unless the source or the user gave it. When the post can't stand without one, leave a marked bracket, like `[how many people came]`, for the user to fill.
2. **The angle is the writer's.** LinkedIn shows generic posts with no clear point of view less widely beyond the writer's network. The view, the example and the stake come from the user. Never supply an opinion, a lesson or a story for them.
3. **Credit the source and don't copy it.** Name who said it. Quote at most one short line, under 15 words, word for word. Everything else goes in your own words.

When the user asks for something these rules block, like a statistic they don't have, say so in one line and leave a bracket.

## Step 1: Read the source

Read `references/sources.md` and follow it for the kind of material you have. Read the whole thing. If you can't open a source, say so and ask the user to paste it. Check the source's date.

## Step 2: List the facts

Before drafting, keep a short scratch list, out of the post: what the source says and who says it, the source's date, what the user gave (their facts, numbers and view), and what's missing. Draft only from this list.

## Step 3: Get the post's job and the writer's angle

**First, the post's job.** Every post has one, and it sets the rules that follow:

- **Share the writer's own work:** an article, paper, page, report or launch the writer made, where the point is to send readers to it. The link stays in the post.
- **Respond to someone else's source:** an article, report, talk or post by someone else.
- **Make a point of the writer's own:** an idea, a lesson or a story, with no source to send readers to.

Read the job from the request. A link to the writer's own site or a piece they say they wrote is the first job. If the job isn't clear, ask it in the same message as the angle question below.

**Then the angle.** For the first job, the piece itself is the angle: the post states the piece's argument, so no further angle is needed unless the user gave one. For the other two, look at the list for one of these, in the user's own words:

- Their take on the source: where they agree or disagree, and why.
- A clear opinion they'd defend.
- A case from their own work that shows the point.
- A number from their own work.
- A decision they made and what came of it.

If one is there, go on. If none is, send one short message before writing that asks for the angle, with two or three plain options the user can pick from:

- When the source makes a claim: "Do you agree that X? Have you seen it in your own work? Anything you'd add?"
- When the source is only a topic or an idea: "What made you think of this: a project where it happened, your main reason and how you know, or a number from your work?"

If you don't know who the post is for, ask that in the same message. Ask once, then write from the answer.

**Then the lane.** The feed matches posts to readers by topic and reads each writer's history, so posts on the same two or three subjects, backed by the profile, build reach over time (`references/platform.md`). If the user has named their core subjects or shared their headline, check the post's subject against them. When it falls outside them, say so in one line of the notes; don't block the post.

When the user isn't there to answer, or asks you to draft anyway, write the post with a labeled bracket where the angle goes, like `[your view: do you agree that most firms skip this step, and why?]`, and say so at the top of the notes.

## Step 4: Pick the post type

Read `references/post-types.md`. For the first job, use the "sharing your own work" post. Otherwise text is the skill's default, and a document is the better choice when the material is a framework, steps or findings with real substance. Say why in one line.

## Step 5: Write

**Voice.** If the Plainspeak Writer skill is installed, follow its steps and its LinkedIn guide for the drafting and editing, and give it this step's length and rules as the user's request. Where the two skills differ, this one sets the length, the paragraphs, the hashtags, the fact check's inputs and what the reply holds. When a Plainspeak Writer rule works against a finding in `references/platform.md`, the finding wins: clear that warning with the finding as the reason. If it isn't installed, follow `references/writing.md`. Where the user shares posts of their own, match their length, paragraph habits and words.

**Build:**

- **One subject.** Name it early in the plain words people in the field use. The feed matches posts to readers by meaning, so a post about one clear thing has the best chance of reaching the people who care about it.
- **The opening lands the central point before the fold.** The first 140 characters are all most readers see. They state the main argument of the whole source or idea, across its full scope: a source about three industries opens on all three, never on one of them. In 2026 data, story openers did best and contrarian openers next, and question openers did worst. So open on a short story or a claim that cuts against a common belief, as long as it stands for the post's whole point. A story pulled from deep in a source to stand in for its argument fails that test. Don't open on a question, a greeting or a setup.
- **The next line or two say why it matters** to the reader named in Step 3.
- **The body makes the case** with the writer's facts and the credited source. In one 2026 dataset, posts with more than 14 paragraphs did 66% better than posts with fewer than 7. Write paragraphs of one or two full sentences and start a new one at each new point, so a text post usually lands at 10 to 14 paragraphs. Every sentence is still a whole sentence that follows from the one before. Use plain, short words.
- **One example, explained, or none.** A post makes an argument; the source holds the evidence. Use at most one example, and give it the sentences it needs: what happened, and how it shows the point. Never tack a statistic, a name or a finding onto a sentence as a quick aside, and never run several facts one after another. When the post shares the writer's own work, leave the evidence in the piece.
- **The close** invites a real answer: a specific question about a named case or choice that someone with experience could answer in a sentence ("Which would you cut first: the kickoff deck or the status report?"), or a position people will want to add to or push back on. LinkedIn is cutting bait like "Comment YES if you agree" and low-value comments, so never ask for a comment, a like or a repost, and never close on "Thoughts?" or "Agree?".
- **Length:** posts of 1,300 to 2,500 characters did best in 2026 data, and posts under 400 did worst. This skill aims for 1,300 to 1,900, about 1,500 to 1,700, for a text post or a post sharing the writer's work. For a document, images, a poll or a video, the text runs 150 to 1,300 characters, a choice the skill makes because no data covers it. A user's request for another length wins.
- **Links follow the post's job.** A link costs reach, by 12% to 60% depending on the study, and a link-preview card roughly halves it (`references/platform.md`). When the post shares the writer's own work, the link goes in the post on its own line after the body, because sending readers to the work is the post's job. Tell the user to remove the preview card LinkedIn adds when they paste it, so the link shows as plain text. When the piece has a framework or findings that would fill slides, offer a document post as the other route, in one line. When the post responds to someone else's source, name the source and ask the user whether to include the link, with the cost in one line. When there's no source, there's no link.
- **Hashtags:** one to three, on the last line, each naming the post's exact subject or a real community or event. In one 2026 measure, 1 to 3 relevant hashtags gave about 9% more reach and 12.6% more engagement, with falling returns at 6 or more. Never more than three.
- **Tags:** tag a person or company only when the post is about their work and treats it fairly. Never tag to borrow reach.
- **Plain text only.** No arrow or emoji bullets, and no bold or italic Unicode letters. A list stays a plain list, and only when the content is a list.

## Step 6: Check

Save the post on its own in a file, with no notes. From this skill's folder, run:

```bash
python3 scripts/check_post.py --type text post.txt
```

Set `--type` to `share` for a post sharing the writer's own work, or to `text`, `document`, `images`, `poll` or `video`. A `share` post expects its link and doesn't flag it. For a poll, also pass `--poll poll.txt`, with the question on line 1 and one option per line after it. If the user chose to keep a link in any other post, add `--link-ok`.

If Plainspeak Writer is installed, also run its check from that skill's folder: `python3 scripts/check_voice.py --surface linkedin post.txt`. Where only `python` exists, use that.

Rewrite every block. Fix every warning, or keep it with a stated reason, and turn a rule off with `--skip P06` only when the user asked for what it blocks. Repeat until nothing blocks. When code can't run, read the post against the rules in Step 5 and count the characters by hand.

Then do two checks that the script can't:

- **The stranger test.** Read the post as someone who doesn't know the writer. Could anyone in the field have written it without the writer's own case, number, decision or view? If yes, it's the kind of post LinkedIn shows less widely. Go back to Step 3.
- **The scope test.** Does the first line cover what the whole source or idea covers? Does any sentence drop in a fact without saying how it shows the point? Fix either one before going on.
- **The fact check.** When you can start a separate agent, write the notes from Step 7 into their own file first, then give it only the user's messages, the source text, the post and the notes, and ask it to quote every name, number, quote and claim the source and the user don't support, and every place the post says something bigger or firmer than they did. Don't give it your reasons. Cut or fix each line it quotes. When you can't start an agent, read the post line by line against the source and the user's messages as if someone else wrote it.

## Step 7: Deliver

Give the post first, exactly as checked, ready to paste. For any type but text, follow it with the one line on why you picked the type. Then, depending on the type:

- **Document:** the slide outline, and an offer to build the PDF.
- **Images:** the order of the images and a one-line alt text for each.
- **Poll:** the question and the options.
- **Video:** the script.

Then short notes, one line each, only as needed:

- Each bracket to fill.
- Each quote, name or number to check against a transcript.
- For a post responding to someone else's source, the link and the choice, if the user hasn't made it.
- Anything in the source that looks unfinished or unreal, like a placeholder name.
- Any warning you kept, and why.

Close with short posting advice from `references/platform.md`: post on a weekday and try two time slots; stay 30 to 60 minutes after posting and reply properly to every serious comment; and don't use comment tools or engagement groups. Leave out anything else unless the user asks.

## Keeping the rules current

LinkedIn changes its feed often. `references/platform.md` gives the date it was last checked. When today is more than six months past it, tell the user once that the rules may be out of date, and offer to check what's changed. Update only from sources published in the last year, and name each one.

## Changing the skill

Build on what's here instead of replacing it. Keep the skill general: no personal details, clients or private work in any file. A new rule for the script gets a line in `references/platform.md` saying where it comes from, and a test. Log every change in `CHANGELOG.md`, saying what was added, changed or removed, and why.
