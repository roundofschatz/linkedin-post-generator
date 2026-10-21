# Changelog

Every change to this skill is logged here: what was added, changed or removed, and why. Nothing comes out without a line saying so. Newest first.

## 1.1.0 · Posts that share the writer's own work

Why: the first real use, on October 21, 2026, was a post sharing the owner's own paper. The skill moved the link out of the post for reach, opened on one vivid case from deep in the paper that covered one of its three industries, and dropped facts into sentences as quick asides. The owner rejected all three. A post that exists to send readers to the writer's work needs the link, an opening that covers the whole piece, and the evidence left in the piece.

- Added: Step 3 now settles the post's job first: share the writer's own work, respond to someone else's source, or make a point of the writer's own. The job sets the link, the post type and the length.
- Added: a "sharing your own work" post in `references/post-types.md`: the piece's central point across its full scope, a preview of the argument, the link on its own line, 700 to 1,200 characters, and the writer's own terms kept.
- Changed: the opening rule. The first line states the central point of the whole source or idea. An example opens only when the writer's point is that story.
- Added: one example, explained, or none. No fact tacked onto a sentence as an aside, and no run of facts.
- Changed: links follow the post's job. They stay in a post sharing the writer's work, the writer decides for someone else's source, and the cost moves to `platform.md` instead of the notes.
- Added: the scope test in Step 6.
- Added: `--type share` in `check_post.py`, with its length range and a new rule, P19, that blocks a share post with no link. Three tests.
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
