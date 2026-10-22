import unittest

from _pylings.exercise import clean_traceback
from _pylings.term import progress_bar, strip_ansi


class ProgressBarTests(unittest.TestCase):
    def test_shape(self):
        plain = strip_ansi(progress_bar(12, 53, 60))
        self.assertTrue(plain.startswith("Progress: ["))
        self.assertTrue(plain.endswith("]  12/53"))
        bar = plain[len("Progress: [") : -len("]  12/53")]
        self.assertEqual(len(bar), 60 - len("Progress: [") - len("] xxx/xxx"))
        self.assertRegex(bar, r"^#*>-*$")

    def test_full(self):
        plain = strip_ansi(progress_bar(53, 53, 60))
        self.assertNotIn(">", plain)
        self.assertNotIn("-", plain)

    def test_narrow_terminal(self):
        self.assertEqual(strip_ansi(progress_bar(3, 9, 10)), "Progress: 3/9")


class TracebackTests(unittest.TestCase):
    def test_drops_helper_frames(self):
        tb = (
            "Traceback (most recent call last):\n"
            '  File "/x/exercises/01_basics/basics1.py", line 17, in <module>\n'
            '    eq(greet("Faruk"), "Hello, Faruk!")\n'
            '  File "/x/pylings_check.py", line 21, in eq\n'
            "    _fail(label, ...)\n"
            '  File "/x/pylings_check.py", line 15, in _fail\n'
            "    raise AssertionError(...)\n"
            "AssertionError: values differ\n"
        )
        out = clean_traceback(tb)
        self.assertNotIn("pylings_check", out)
        self.assertIn("basics1.py", out)
        self.assertIn("AssertionError: values differ", out)


if __name__ == "__main__":
    unittest.main()
