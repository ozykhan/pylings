import unittest

from _pylings.app_state import next_pending_index, parse_state, render_state


class StateFileTests(unittest.TestCase):
    def test_roundtrip(self):
        text = render_state("basics3", ["basics1", "basics2"])
        self.assertEqual(
            text, "DON'T EDIT THIS FILE!\n\nbasics3\n\nbasics1\nbasics2"
        )
        self.assertEqual(parse_state(text), ("basics3", {"basics1", "basics2"}))

    def test_no_done(self):
        self.assertEqual(parse_state(render_state("basics1", [])), ("basics1", set()))

    def test_garbage_is_not_read(self):
        self.assertIsNone(parse_state(""))
        self.assertIsNone(parse_state("DON'T EDIT THIS FILE!\n\n"))
        self.assertIsNone(parse_state("DON'T EDIT THIS FILE!\n\nbasics1"))


class NextPendingTests(unittest.TestCase):
    def check(self, done, expected):
        for ind, want in enumerate(expected):
            self.assertEqual(next_pending_index(done, ind), want, f"done={done} ind={ind}")

    def test_like_rustlings(self):
        self.check([True, True, True], [None, None, None])
        self.check([False, False, False], [1, 2, 0])
        self.check([False, True, True], [None, 0, 0])
        self.check([True, False, True], [1, None, 1])
        self.check([True, True, False], [2, 2, None])
        self.check([True, False, False], [1, 2, 1])
        self.check([False, True, False], [2, 2, 0])
        self.check([False, False, True], [1, 0, 0])


if __name__ == "__main__":
    unittest.main()
