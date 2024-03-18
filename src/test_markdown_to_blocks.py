import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        mkdwn = """
        This is **bolded** paragraph

        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line

        * This is a list
        * with items"""
        blocks = markdown_to_blocks(mkdwn)
        check_blocks = [
            ["This is **bolded** paragraph"],
            [
                "This is another paragraph with *italic* text and `code` here",
                "This is the same paragraph on a new line",
            ],
            ["* This is a list", "* with items"],
        ]
        self.assertEqual(blocks, check_blocks)

    def test_convert_markdown(self):
        mkdwn = """
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is a list item
        * This is another list item"""
        blocks = markdown_to_blocks(mkdwn)
        check_blocks = [
            ["# This is a heading"],
            [
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
            ],
            ["* This is a list item", "* This is another list item"],
        ]
        self.assertEqual(blocks, check_blocks)
