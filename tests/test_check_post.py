"""Tests for scripts/check_post.py. Run: python tests/test_check_post.py"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_post as cp  # noqa: E402

PARA = ("We rebuilt the onboarding for a 40-person accounting firm last spring, and the "
        "change that mattered most was the smallest one. New hires used to wait three days "
        "for a laptop, so their first week started on day four.")


def ids(text, **kw):
    return {h[0] for h in cp.check(text, **kw)[3]}


def good_post():
    opening = "New hires at one firm waited three days for a laptop. Fixing that beat every other change."
    body = "\n\n".join([PARA] * 6)
    close = "Which first-week delay would you fix before anything else: equipment or access?"
    return f"{opening}\n\n{body}\n\n{close}"


class Length(unittest.TestCase):
    def test_good_post_is_clean(self):
        post = good_post()
        self.assertTrue(1300 <= len(post) <= 1900, len(post))
        self.assertEqual(ids(post), set())

    def test_over_limit_blocks(self):
        self.assertIn("P01", ids("x " * 1600))

    def test_short_text_post_warns(self):
        self.assertIn("P02", ids("One short line about a real thing we did."))

    def test_document_range_is_shorter(self):
        self.assertNotIn("P02", ids(PARA, post_type="document"))


class Opening(unittest.TestCase):
    def test_long_opening_blocks(self):
        self.assertIn("P03", ids("a" * 220 + "\n\n" + PARA))

    def test_mid_opening_warns(self):
        self.assertIn("P04", ids("a" * 160 + "\n\n" + PARA))

    def test_fold_counts_across_lines(self):
        self.assertIn("P04", ids("a" * 80 + "\n" + "b" * 80 + ".\n\n" + PARA))

    def test_greeting_blocks(self):
        for opener in ("Happy Monday, everyone!", "In today's market, brands struggle.",
                       "I've been thinking about onboarding.", "Thrilled to announce our new office."):
            self.assertIn("P05", ids(opener + "\n\n" + PARA), opener)

    def test_question_opener_warns(self):
        self.assertIn("P06", ids("Ever waited three days for a laptop?\n\n" + PARA))


class Bait(unittest.TestCase):
    def test_named_bait_blocks(self):
        for line in ("Comment YES if you agree.", "Type 'GUIDE' below and I'll send it.",
                     "Like if you agree.", "Repost if this helped."):
            self.assertIn("P07", ids(PARA + "\n\n" + line), line)

    def test_other_bait_warns(self):
        for line in ("Agree?", "Thoughts?", "Follow me for more.", "Tag someone who needs this.",
                     "Who else has seen this?", "Drop a comment below."):
            found = ids(PARA + "\n\n" + line)
            self.assertIn("P20", found, line)
            self.assertNotIn("P07", found, line)

    def test_specific_question_passes(self):
        self.assertNotIn("P07", ids(PARA + "\n\nWhich would you fix first: equipment or access?"))


class Hashtags(unittest.TestCase):
    def test_two_at_end_pass(self):
        found = ids(good_post() + "\n\n#Onboarding #HRTech")
        self.assertFalse({"P08", "P09"} & found)

    def test_three_block(self):
        self.assertIn("P08", ids(good_post() + "\n\n#A #B #C"))

    def test_inline_warns(self):
        self.assertIn("P09", ids("We fixed #onboarding in a week.\n\n" + PARA))


class Other(unittest.TestCase):
    def test_link_warns_unless_ok(self):
        post = PARA + "\n\nRead it at https://example.com/report"
        self.assertIn("P10", ids(post))
        self.assertNotIn("P10", ids(post, link_ok=True))

    def test_bare_domain_counts_as_link(self):
        self.assertIn("P10", ids(PARA + "\n\nRead it at basecollab.studio today."))
        self.assertNotIn("P10", ids(PARA + "\n\nWe tried it, e.g. twice, in 2.5 weeks."))

    def test_arrow_bullets_warn(self):
        self.assertIn("P12", ids(PARA + "\n\n→ Faster laptops\n→ Earlier access"))

    def test_fancy_letters_block(self):
        self.assertIn("P13", ids("\U0001D5E7\U0001D5F6\U0001D600 matters.\n\n" + PARA))

    def test_not_x_y_blocks(self):
        self.assertIn("P14", ids(PARA + "\n\nIt's not about the laptop, it's about the first day."))
        self.assertIn("P14", ids(PARA + "\n\nThis is not just a fix, but a reset."))

    def test_mentions_warn(self):
        self.assertIn("P16", ids(PARA + "\n\nThanks @Ana @Ben @Cal @Dee"))

    def test_skip(self):
        self.assertNotIn("P06", ids("Ever waited for a laptop?\n\n" + PARA, skip={"P06"}))


class Share(unittest.TestCase):
    def test_share_post_keeps_its_link(self):
        post = good_post().replace("Which first-week", "https://example.com/paper\n\nWhich first-week")
        found = ids(post, post_type="share")
        self.assertFalse({"P02", "P03", "P10", "P19"} & found, found)

    def test_share_post_without_link_blocks(self):
        self.assertIn("P19", ids(PARA + "\n\n" + PARA, post_type="share"))

    def test_share_range(self):
        self.assertIn("P02", ids(PARA + "\n\nhttps://example.com/paper", post_type="share"))


class Poll(unittest.TestCase):
    def test_poll_limits(self):
        found = ids(PARA, post_type="poll", poll="Which first?\n- Equipment\n- " + "x" * 31)
        self.assertIn("P17", found)
        self.assertIn("P18", ids(PARA, post_type="poll", poll="Which first?\n- Equipment"))
        clean = ids(PARA, post_type="poll", poll="Which first?\n- Equipment\n- Access")
        self.assertFalse({"P17", "P18"} & clean)


class Cli(unittest.TestCase):
    def test_exit_codes(self):
        tmp = Path(__file__).with_name("_tmp_post.txt")
        try:
            tmp.write_text(good_post(), encoding="utf-8")
            self.assertEqual(cp.main([str(tmp)]), 0)
            tmp.write_text(PARA + "\n\nAgree?", encoding="utf-8")
            self.assertEqual(cp.main([str(tmp)]), 1)
        finally:
            tmp.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
