import unittest
from markdown_to_blocks import markdown_to_blocks, BlockType, block_to_block_type


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

    def test_block_to_blocktype(self):
        blocks = [
            ["# This is a heading"],
            [
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
            ],
            ["> A block here", "> Is a block there"],
            ["```Me testing code```"],
            ["1. Hello Internet", "2. Welcome to Film Theory", "3. This is Matpat"],
            ["- Hello Again", "- Hihi"],
        ]
        check_types = [
            BlockType.block_type_heading,
            BlockType.block_type_paragraph,
            BlockType.block_type_quote,
            BlockType.block_type_code,
            BlockType.block_type_ordered_list,
            BlockType.block_type_unordered_list,
        ]
        block_types = []
        for text_b in blocks:
            block_types.append(block_to_block_type(text_b))
        self.assertEqual(block_types, check_types)

    def test_block_to_blocktype_combination(self):
        blocks = [
            ["####### This is not a heading"],
            [
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
            ],
            ["> A block here", "* Becomes a paragraph there"],
            ["`Me testing code without formatting```"],
            ["1. Hello Internet", "-. Welcome to Film Theory", "3. This is Matpat"],
            ["* Hello Again", "- Hihi"],
        ]
        check_types = [
            BlockType.block_type_paragraph,
            BlockType.block_type_paragraph,
            BlockType.block_type_paragraph,
            BlockType.block_type_paragraph,
            BlockType.block_type_paragraph,
            BlockType.block_type_paragraph,
        ]
        block_types = []
        for text_b in blocks:
            block_types.append(block_to_block_type(text_b))
        self.assertEqual(block_types, check_types)
