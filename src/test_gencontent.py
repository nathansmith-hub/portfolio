import unittest

from gencontent import extract_title

class TestExtractTitle(unittest.TestCase):
    
    def test_extract_title(self):
        markdown = """
# This is a title
This is text
This is more text
"""
        title = extract_title(markdown)
        self.assertEqual(title, "This is a title")

    def test_extract_title_extra_heading(self):
        markdown = """
## This is a heading, but not a title
# This is a title
This is text
"""
        title = extract_title(markdown)
        self.assertEqual(title, "This is a title")

    def test_extract_title_no_title(self):
        markdown = """
There is no title
This is just text
"""
        with self.assertRaises(Exception):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()
