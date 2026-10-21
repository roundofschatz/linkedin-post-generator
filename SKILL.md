---
name: linkedin-post
description: Turns source material into a LinkedIn post built for how LinkedIn's feed ranks posts in 2026. The source can be a link to an article or report, a plain idea or question, an uploaded PDF, Word file, slide deck, spreadsheet or image, pasted notes, a transcript, or someone else's post to answer. It reads the source in full, gets the writer's own angle, picks the post type (text, document carousel, images, poll or video), writes the post and checks it by script for length, the opening line, hashtags, links and engagement bait. Use whenever someone wants to write, draft, plan, fix or repurpose a LinkedIn post, or asks what to post about an article, report, event, project or idea, even if they never say "post."
license: MIT
---

# LinkedIn Post

This skill turns what the user hands over into a LinkedIn post that LinkedIn's 2026 feed will show to the right readers. The work runs in order: read the source, list the facts, get the writer's angle, pick the post type, write, check, then deliver. What LinkedIn rewards and cuts, with the evidence for each rule, is in `references/platform.md`.

## Rules above everything

1. **Never invent a fact.** No name, number, quote, date, client, result or experience goes in the post unless the source or the user gave it. When the post can't stand without one, leave a marked bracket, like `[how many people came]`, for the user to fill.
2. **The angle is the writer's.** LinkedIn cuts posts that summarize without a view of their own. The view, the example and the stake come from the user. Never supply an opinion, a lesson or a story for them.
3. **Credit the source and don't copy it.** Name who said it. Quote at most one short line, under 15 words, word for word. Everything else goes in your own words.

When the user asks for something these rules block, like a statistic they don't have, say so in one line and leave a bracket.

## Step 1: Read the source

Read `references/sources.md` and follow it for the kind of material you have. Read the whole thing. If you can't open a source, say so and ask the user to paste it. Check the source's date.

## Step 2: List the facts

Before drafting, keep a short scratch list, out of the post: what the source says and who says it, the source's date, what the user gave (their facts, numbers and view), and what's missing. Draft only from this list.

## Step 3: Get the writer's angle

Look at the list for one of these, in the user's own words:

- Their take on the source: where they agree or disagree, and why.
- A case from their own work that shows the point.
- A number from their own work.
- A decision they made and what came of it.

If one is there, go on. If none is, send one short message before writing that asks for the angle, with two or three plain options the user can pick from:

- When the source makes a claim: "Do you agree that X? Have you seen it in your own work? Anything you'd add?"
- When the source is only a topic or an idea: "What made you think of this: a project where it happened, your main reason and how you know, or a number from your work?"

If you don't know who the post is for, ask that in the same message. Ask once, then write from the answer.

When the user isn't there to answer, or asks you to draft anyway, write the post with a labeled bracket where the angle goes, like `[your view: do you agree that most firms skip this step, and why?]`, and say so at the top of the notes.

## Step 4: Pick the post type

Read `references/post-types.md`. Text is the default. Pick another type only when the material calls for it, and say why in one line.

## Step 5: Write

**Voice.** If the Plainspeak Writer skill is installed, follow its steps and its LinkedIn guide for the drafting and editing, and give it this step's length and rules as the user's request. If it isn't installed, follow `references/writing.md`. Where the user shares posts of their own, match their length, paragraph habits and words.

**Build:**

- **One subject.** Name it early in the plain words people in the field use. The feed matches posts to readers by meaning, so a post about one clear thing reaches the people who care about it.
- **The first line states the point.** Keep it under 140 characters: a specific claim, a scene the user described, or a line that cuts against a common belief in the field, which the body then backs up. Don't open on a greeting, a setup or a question.
- **The next line or two say why it matters** to the reader named in Step 3.
- **The body makes the case** with the writer's facts and the credited source. Short paragraphs of one to three full sentences. Don't stack one-sentence lines.
- **The close** is the writer's position, a next step, or a specific question about a named case or choice that someone with experience could answer in a sentence: "Which would you cut first: the kickoff deck or the status report?" Never "Thoughts?", "Agree?" or a request to comment, like or repost.
- **Length:** 1,300 to 1,900 characters for a text post. For a document, images, a poll or a video, the text runs 150 to 1,300 characters. A user's request for another length wins.
- **No link in the post.** Name the source in the post and put the link in the notes, so the user can choose: leave it out, or add it and accept less reach.
- **Hashtags:** none by default. At most two, on the last line, and only when they name the exact subject or a real community or event.
- **Tags:** tag a person or company only when the post is about their work and treats it fairly. Never tag to borrow reach.
- **Plain text only.** No arrow or emoji bullets, and no bold or italic Unicode letters. A list stays a plain list, and only when the content is a list.

## Step 6: Check

Save the post on its own in a file, with no notes. Run:

```bash
python scripts/check_post.py --type text post.txt
```

Set `--type` to `text`, `document`, `images`, `poll` or `video`. For a poll, also pass `--poll poll.txt`, with the question on line 1 and one option per line after it. If the user chose to keep a link in the post, add `--link-ok`.

If Plainspeak Writer is installed, also run its check from its own folder: `python scripts/check_voice.py --surface linkedin post.txt`.

Rewrite every block. Fix every warning, or keep it with a stated reason, and turn a rule off with `--skip P06` only when the user asked for what it blocks. Repeat until nothing blocks. When code can't run, read the post against the rules in Step 5 and count the characters by hand.

Then do two checks that the script can't:

- **The stranger test.** Read the post as someone who doesn't know the writer. Could anyone in the field have written it without the writer's own case, number or view? If yes, it's the kind of post LinkedIn buries. Go back to Step 3.
- **The fact check.** When you can start a separate agent, give it only the user's messages, the source text and the post, and ask it to quote every name, number, quote and claim the source and the user don't support, and every place the post says something bigger or firmer than they did. Don't give it your reasons. Cut or fix each line it quotes. When you can't start an agent, read the post line by line against the source and the user's messages as if someone else wrote it.

## Step 7: Deliver

Give the post first, exactly as checked, ready to paste. Then, depending on the type:

- **Document:** the slide outline, and an offer to build the PDF.
- **Images:** the order of the images and a one-line alt text for each.
- **Poll:** the question and the options.
- **Video:** the script.

Then short notes, one line each, only as needed:

- Each bracket to fill.
- Each quote, name or number to check against a transcript.
- The source link, and the choice: leave it out of the post, or add it and accept less reach.
- Any warning you kept, and why.

Close with two lines of posting advice from `references/platform.md`: post on a weekday and try two time slots, and stay for the first 30 minutes to answer comments. Leave out anything else unless the user asks.

## Keeping the rules current

LinkedIn changes its feed often. `references/platform.md` gives the date it was last checked. When today is more than six months past it, tell the user once that the rules may be out of date, and offer to check what's changed. Update only from sources published in the last year, and name each one.

## Changing the skill

Build on what's here instead of replacing it. Keep the skill general: no personal details, clients or private work in any file. A new rule for the script gets a line in `references/platform.md` saying where it comes from, and a test. Log every change in `CHANGELOG.md`, saying what was added, changed or removed, and why.
