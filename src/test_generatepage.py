import unittest
from generatepage import extract_title

class TesGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        md = """
# This is the title

## This a subtitle
"""
        self.assertEqual(extract_title(md), "This is the title")

def test_eq_double(self):
        actual = extract_title(
            """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(actual, "This is a title")

def test_eq_long(self):
    actual = extract_title(
        """
# title

this is a bunch

of text

- and
- a
- list
"""
    )
    self.assertEqual(actual, "title")

def test_none(self):
        with self.assertRaises(Exception):
            extract_title(
                """
no title
"""
            )

if __name__ == "__main__":
    unittest.main()