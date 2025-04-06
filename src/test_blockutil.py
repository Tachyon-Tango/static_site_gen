
from textnode import *
from htmlnode import *
from blockutil import *

import unittest


class TestBlockUtil(unittest.TestCase):
    def test_markdown_to_blocks_1(self):
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

    def test_markdown_to_blocks_2(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
            ],
        )

    def test_block_to_block_type_heading_1(self):
        md = "# This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "heading"
        )

    def test_block_to_block_type_heading_2(self):
        md = "## This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "heading"
        )

    def test_block_to_block_type_heading_3(self):
        md = "### This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "heading"
        )

    def test_block_to_block_type_heading_4(self):
        md = "#### This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "heading"
        )

    def test_block_to_block_type_heading_5(self):
        md = "##### This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "heading"
        )

    def test_block_to_block_type_heading_6(self):
        md = "###### This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "heading"
        )

    def test_block_to_block_type_heading_7(self):
        md = "####### This is not a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "paragraph"
        )

    def test_block_to_block_type_heading_8(self):
        md = "#This is not a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "paragraph"
        )

    def test_block_to_block_type_code_1(self):
        md = "```This is a code block```"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "code"
        )

    def test_block_to_block_type_code_2(self):
        md = "``` This is a code block ```"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "code"
        )

    def test_block_to_block_type_code_3(self):
        md = "`` This is a code block ```"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "paragraph"
        )

    def test_block_to_block_type_quote_1(self):
        md = ">This is the first quote item in a quote block\n>This is a quote item\n>This is another quote item"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "quote"
        )

    def test_block_to_block_type_quote_2(self):
        md = ">This is the first quote item in a quote block\n>This is a quote item\nThis is not another quote item"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "paragraph"
        )

    def test_block_to_block_type_unordered_list_1(self):
        md = "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "unordered_list"
        )

    def test_block_to_block_type_unordered_list_2(self):
        md = "-This is not the first list item in a list block\n-This is not a list item\n-This is not another list item"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "paragraph"
        )

    def test_block_to_block_type_unordered_list_3(self):
        md = "- This is not the first list item in a list block\n- This is not a list item\nThis is not another list item"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "paragraph"
        )

    def test_block_to_block_type_ordered_list_1(self):
        md = "1. This is the first list item in a list block\n2. This is a list item\n3. This is another list item"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "ordered_list"
        )

    def test_block_to_block_type_ordered_list_2(self):
        md = "1. This is the first list item in a list block\n1. This is a list item\n3. This is another list item"
        block_type = block_to_block_type(md)
        self.assertEqual(
            str(block_type.value), "paragraph"
        )

if __name__ == "__main__":
    unittest.main()