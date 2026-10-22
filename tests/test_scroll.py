import unittest

from _pylings.listmode import ScrollState


class ScrollStateTests(unittest.TestCase):
    def test_selection_bounds(self):
        s = ScrollState(5, 0, 5)
        s.set_max_n_rows_to_display(3)
        s.select_previous()
        self.assertEqual(s.selected, 0)
        for _ in range(10):
            s.select_next()
        self.assertEqual(s.selected, 4)
        self.assertEqual(s.offset, 2)
        s.select_first()
        self.assertEqual((s.selected, s.offset), (0, 0))
        s.select_last()
        self.assertEqual(s.selected, 4)

    def test_empty(self):
        s = ScrollState(3, 1, 5)
        s.set_max_n_rows_to_display(10)
        s.set_n_rows(0)
        self.assertIsNone(s.selected)
        s.set_n_rows(2)
        self.assertEqual(s.selected, 0)

    def test_initial_offset_shows_selected(self):
        s = ScrollState(50, 40, 5)
        s.set_max_n_rows_to_display(10)
        self.assertLessEqual(s.offset, 40)
        self.assertGreater(s.offset + 10, 40)


if __name__ == "__main__":
    unittest.main()
