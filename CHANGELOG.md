# Changelog

Every change to this skill is logged here: what was added, changed or removed, and why. Nothing comes out without a line saying so. Newest first.

## 1.0.0 · First release

Why: LinkedIn rebuilt its feed in 2026. It now matches posts to readers by meaning, cuts generic and AI-sounding posts, and cuts engagement bait. Advice written before 2026, like stacking hashtags, no longer holds. This skill builds a post from source material for the feed as it works now.

- Added: `SKILL.md`, seven steps from reading the source to delivering the post. The writer's own angle is required, and the skill asks for it rather than inventing one.
- Added: `references/platform.md`, what LinkedIn rewards and cuts, from 2026 sources only (one dated 2025 statement is marked as such). Each rule carries its evidence: LinkedIn's own word, a large study, or opinion. Last checked October 21, 2026.
- Added: `references/sources.md`, how to read links, ideas, documents, images, transcripts and other people's posts, and how to credit them.
- Added: `references/post-types.md`, when to use text, a PDF carousel, images, a poll or a video, and what each needs.
- Added: `references/writing.md`, writing rules for when Plainspeak Writer isn't installed.
- Added: `scripts/check_post.py`, 18 rules for length, the opening line, hashtags, links, engagement bait, stock lines and poll limits, with tests in `tests/test_check_post.py`.
- Set: a text post aims for 1,300 to 1,900 characters. 2026 data favors 1,300 to 2,500, and Plainspeak Writer's LinkedIn guide sets 150 to 300 words; this range fits both. Hashtags are capped at two, also to match Plainspeak Writer.
