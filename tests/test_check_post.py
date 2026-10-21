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

    def test_greeting_blocks(self):
        for opener in ("Happy Monday, everyone!", "In today's market, brands struggle.",
                       "I've been thinking about onboarding.", "Thrilled to announce our new office."):
            self.assertIn("P05", ids(opener + "\n\n" + PARA), opener)

    def test_question_opener_warns(self):
        self.assertIn("P06", ids("Ever waited three days for a laptop?\n\n" + PARA))


class Bait(unittest.TestCase):
    def test_bait_blocks(self):
        for line in ("Comment YES if you agree.", "Agree?", "Thoughts?", "Type 'GUIDE' below and I'll send it.",
                     "Repost if this helped.", "Follow me for more.", "Tag someone who needs this.",
                     "Who else has seen this?", "Drop a comment below."):
            self.assertIn("P07", ids(PARA + "\n\n" + line), line)

    def test_specific_question_passes(self):
        self.assertNotIn("P07", ids(PARA + "\n\nWhich would you fix first: equipment or access?"))


class Hashtags(unittest.TestCase):
    def test_two_at_end_pass(self):
        found = ids(good_post() + "\n\n#Onboarding #HRTech")
        self.assertFalse({"P08", "P09"} & found)

    def test_three_warn(self):
        self.assertIn("P09", ids(good_post() + "\n\n#A #B #C"))

    def test_four_block(self):
        self.assertIn("P08", ids(good_post() + "\n\n#A #B #C #D"))

    def test_inline_warns(self):
        self.assertIn("P09", ids("We fixed #onboarding in a week.\n\n" + PARA))


class Other(unittest.TestCase):
    def test_link_warns_unless_ok(self):
        post = PARA + "\n\nRead it at https://example.com/report"
        self.assertIn("P10", ids(post))
        self.assertNotIn("P10", ids(post, link_ok=True))

    def test_one_line_stack_warns(self):
        post = "\n\n".join(f"Short line number {i}." for i in range(8))
        self.assertIn("P11", ids(post))

    def test_arrow_bullets_warn(self):
        self.assertIn("P12", ids(PARA + "\n\n→ Faster laptops\n→ Earlier access"))

    def test_fancy_letters_block(self):
        self.assertIn("P13", ids("\U0001D5E7\U0001D5F6\U0001D600 matters.\n\n" + PARA))

    def test_not_x_y_warns(self):
        self.assertIn("P14", ids(PARA + "\n\nIt's not about the laptop, it's about the first day."))
        self.assertIn("P14", ids(PARA + "\n\nThis is not just a fix, but a reset."))

    def test_stock_line_warns(self):
        self.assertIn("P15", ids(PARA + "\n\nLet that sink in."))

    def test_mentions_warn(self):
        self.assertIn("P16", ids(PARA + "\n\nThanks @Ana @Ben @Cal @Dee"))

    def test_skip(self):
        self.assertNotIn("P06", ids("Ever waited for a laptop?\n\n" + PARA, skip={"P06"}))


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
