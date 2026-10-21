# Case: sharing the writer's own paper

Run this case by hand, or with a fresh agent that sees only the skill and the request, after any change to Steps 3 to 6 or to `references/post-types.md`.

## The request

The writer pastes a draft post and a link to their own paper. The paper compares what one term means in three industries, finds three missions that all three share, and ends with a set of questions readers can use. Deep in the paper sit several cases: a city that rejected a project, a company's public commitments, a survey count.

Their draft:

> I recently examined what one term means across three industries, as the meaning differs for each. What unites them is a focus on three missions: customer, company and community. I created a framework showing how consultants can align these missions upstream and avoid friction downstream.

## What a passing post does

- Treats the job as sharing the writer's own work, and keeps the link in the post, on its own line.
- Opens on the paper's central point across all three industries.
- Keeps the writer's own terms (customer, company and community), even where the paper words them differently.
- Previews the argument and what the reader gets (the questions), and leaves the cases in the paper.
- Runs 1,300 to 1,900 characters and passes `check_post.py --type share`.
- Tells the writer to remove the link-preview card, and offers a document post as the other route only if the paper has findings that would fill slides.

## What fails it

These all happened in the first version of this skill:

- The link moved to the notes, with advice to leave it out for reach.
- The opening pulled one case from deep in the paper, about one of the three industries.
- Facts from the paper dropped into sentences as quick asides: a group's name and a count, a company's list of commitments, with no sentence saying how each showed the point.
- The writer's terms swapped for the paper's.
