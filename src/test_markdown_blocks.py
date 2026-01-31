import unittest

from markdown_blocks import (
    BlockType,
    block_to_block_type,
    markdown_to_blocks,
)

class TestMarkdownBlocks(unittest.TestCase):
    def test_block_to_block_heading(self):
        block = "### This is a Heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_heading_extra_hashes(self):
        block = "####### I have too many hashes so I am a Paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_code(self):
        block = "```\nThis is Code\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_code_one_line(self):
        block = "```I have only one line so I am a Paragraph```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_quote(self):
        block = "> This is a Quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_to_block_unordered_list(self):
        block = "- This is an Unordered List"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_block_to_block_unordered_list_no_space(self):
        block = "-No space so I am a Paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_ordered_list(self):
        block = "1. This is an Ordered List"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_block_to_block_ordered_list_multi(self):
        block = "1. This\n2. Is\n3. An\n4. Ordered\n5. List"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_block_to_block_ordered_list_wrong_num_order(self):
        block = "6. Reversed\n5. Numbers\n4. So\n3. I'm\n2. A\n1. Paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_paragraph(self):
        block = "This is a Paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_multi_newlines(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines_before_and_after(self):
        md = """

        
        
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items



"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_only_paragraph(self):
        md = """
This is the **only** paragraph
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is the **only** paragraph",
            ],
        )

    def test_markdown_to_blocks_only_list(self):
        md = """
- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_only_list_one_item(self):
        md = """
- This is a list with only one item
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "- This is a list with only one item",
            ],
        )

    def test_markdown_to_blocks_empty_input(self):
        md = """
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [],
        )

    def test_markdown_to_blocks_whitespace(self):
        md = """
First block content
    

Second block content
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First block content",
                "Second block content",
            ],
        )

    def test_markdown_to_blocks_only_whitespace(self):
        md = """
    

        
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [],
        )

if __name__ == "__main__":
    unittest.main()
