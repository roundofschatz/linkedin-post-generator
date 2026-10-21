# LinkedIn Post Generator

LinkedIn Post Generator is a Claude skill that turns what you hand it into a LinkedIn post built for how LinkedIn's feed works in 2026. Give it a link to an article, a rough idea, a report, a slide deck, a spreadsheet, a photo, your notes from a talk or someone else's post you want to answer. It reads the source in full, asks for your own take when the source doesn't hold one, picks the right kind of post and writes it. Then a script checks the post before you see it.

## Why it works this way

In March 2026, LinkedIn rebuilt its feed around an AI model that reads what a post is about and shows it to people whose work and reading fit, in or out of your network. Since May 2026 it has cut the reach of posts that sound generic or AI-made, and by October it screened every post shown outside the writer's network. It also cuts engagement bait like "Comment YES if you agree."

So the posts that travel now are specific, about one clear subject and plainly the writer's own. A post that only summarizes an article is the kind LinkedIn buries. That's why this skill asks for your view, your example or your number before it writes, and never makes one up.

What LinkedIn rewards and cuts, with the evidence and sources for each rule, is in `references/platform.md`.

## How it works

1. **Read the source.** The whole article, document or transcript, never just the title. If a page won't open, it asks you to paste it.
2. **List the facts.** What the source says, who says it, when, and what you added. The post uses only that list.
3. **Get your angle.** Your take, a case from your work, a number or a decision. If the source and your message don't hold one, it asks you one question first.
4. **Pick the post type.** Sharing your own work when the point is to send readers to it, otherwise text by default. A PDF carousel for a framework or steps, photos when you have them, a poll when you want the answer, a video script when you'll film.
5. **Write.** The point in the first line, under the "see more" cut. One subject. 1,300 to 1,900 characters for a text post. Short paragraphs. A close that invites a real answer, not a reflex comment. A link only when the post's job needs one, like sharing your own article, and no more than two hashtags.
6. **Check.** A script checks the length, the opening against the "see more" fold, paragraphs, hashtags, links and engagement bait. Then two checks it can't do: would a stranger know only you could have written this, and is every fact backed by the source or by you?
7. **Deliver.** The post, ready to paste, with the slide outline, image notes or poll when there is one, and a short list of anything to fill or check.

## Works with Plainspeak Writer

When [Plainspeak Writer](https://github.com/roundofschatz/plainspeak-writer) is installed, LinkedIn Post Generator hands it the sentence work and runs its check too. On its own, it uses the short writing rules in `references/writing.md`.

## What's in the folder

```
linkedin-post-generator/
├── SKILL.md                  the steps Claude follows
├── README.md                 this file
├── LICENSE                   MIT
├── CHANGELOG.md              every change, newest first
├── references/
│   ├── platform.md           what LinkedIn rewards and cuts, dated, with sources
│   ├── sources.md            how to read each kind of source
│   ├── post-types.md         text, carousel, images, poll, video
│   └── writing.md            writing rules for when Plainspeak Writer isn't installed
├── scripts/
│   └── check_post.py         the post check
└── tests/
    └── test_check_post.py    tests for the check
```

The repository is the skill folder, so the folder name has to stay `linkedin-post-generator`. Skills only load from a folder whose name matches the `name` field in SKILL.md.

## Install

Custom skills don't sync between Claude products, so install LinkedIn Post Generator in each one you use.

**As a plugin.** LinkedIn Post Generator is listed in the author's plugin marketplace, `roundofschatz`, which lives in the job-seeker-ops repository. In Claude Code, run `/plugin marketplace add roundofschatz/job-seeker-ops`, then `/plugin install linkedin-post-generator@roundofschatz`. In the Claude app, add the same marketplace under Customize, Plugins.

**Claude Code.** Clone the repository into your skills folder. Use `~/.claude/skills/` for every project, or `.claude/skills/` inside one project:

```bash
git clone https://github.com/roundofschatz/linkedin-post-generator ~/.claude/skills/linkedin-post-generator
```

**Claude.ai.** Download `linkedin-post-generator.zip` from the Releases page and upload it under Skills in Settings. Custom skills need a paid plan with code execution turned on. Don't use GitHub's green "Download ZIP" button, because it names the folder `linkedin-post-generator-main`, which doesn't match the skill's name.

**Claude API.** Upload the `linkedin-post-generator` folder through the Skills API.

## Use

Hand it the material and say what you want. For example:

> Turn this article into a LinkedIn post. I disagree with its second point. [link]

> I want to post about why we stopped doing kickoff decks. Here are my notes.

> Make a carousel from this report for operations leaders. [PDF]

> Someone posted that agencies are dead. Here's their post. Help me answer it.

## The check

From inside the folder, with Python 3 and nothing else:

```bash
python3 scripts/check_post.py --type text post.txt
```

Set `--type` to `text`, `document`, `images`, `poll` or `video`. For a poll, add `--poll poll.txt`, with the question on line 1 and one option per line. If you've chosen to keep a link in the post, add `--link-ok`. Run `--list-rules` to see every rule. HARD rules block the post; WARN rules stay only with a reason.

A clean check means the post has none of the surface problems. Whether it's worth reading is still the edit's call.

## Keeping it current

LinkedIn changes its feed often, so the rules live in one dated file, `references/platform.md`. When that date is more than six months old, the skill tells you the rules may be out of date and offers to check.

## Contributing

Pull requests are welcome when they keep to these rules:

- **Keep it general.** No personal details, clients or private work in any file.
- **Build on what's here.** Change or extend a rule instead of replacing the file around it.
- **Show the source for a platform rule.** Each rule in `platform.md` names where it comes from and when, and only sources from the past year count.
- **Test a new check.** A rule added to `check_post.py` gets a test in `tests/test_check_post.py`.
- **Log every change** in `CHANGELOG.md`: what was added, changed or removed, and why.

## Author

Ryan Schatzman · [LinkedIn](https://www.linkedin.com/in/ryanschatzman)

## License

LinkedIn Post Generator is released under the MIT License. See `LICENSE` for the terms. It isn't made by or affiliated with LinkedIn.
