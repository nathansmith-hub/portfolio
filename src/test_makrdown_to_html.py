import unittest

from main import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading_with_inline_and_trailing_space(self):
        md = "### This is a **bold** and _italic_ heading "
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is a <b>bold</b> and <i>italic</i> heading</h3></div>",
        )

    def test_quote_with_inline_code_and_leading_spaces(self):
        md = """>     This is a `code block` within a quote.
>     It has leading spaces."""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>    This is a <code>code block</code> within a quote.\n    It has leading spaces.</blockquote></div>",
        )

    def test_unordered_list_multi_feature(self):
        md = """- This is **bolded** item
- This is another _italic_ item
- A third item with `code`"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is <b>bolded</b> item</li><li>This is another <i>italic</i> item</li><li>A third item with <code>code</code></li></ul></div>",
        )

    def test_ordered_list_multi_feature(self):
        md = """1. First **bold** item
2. Second _italic_ item
3. Third `code` item"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First <b>bold</b> item</li><li>Second <i>italic</i> item</li><li>Third <code>code</code> item</li></ol></div>",
        )

if __name__ == "__main__":
    unittest.main()
