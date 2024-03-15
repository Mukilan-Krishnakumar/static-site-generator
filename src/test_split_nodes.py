import unittest
from leafnode import LeafNode
from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType
from htmlnode import HTMLNode


class TestSplitNodes(unittest.TestCase):
    def test_code_block(self):
        node = TextNode(
            "This is text with a `code block` word", TextType.text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.text_type_code)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.text_type_text, None),
                TextNode("code block", TextType.text_type_code, None),
                TextNode(" word", TextType.text_type_text, None),
            ],
        )

    def test_inline_block(self):
        node = TextNode("This is a `complex test case", TextType.text_type_text)
        self.assertRaises(
            ValueError, split_nodes_delimiter, [node], "`", TextType.text_type_code
        )

    def test_bold_block(self):
        node = TextNode(
            "This is text with a **bold block** word", TextType.text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.text_type_bold)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.text_type_text, None),
                TextNode("bold block", TextType.text_type_bold, None),
                TextNode(" word", TextType.text_type_text, None),
            ],
        )

    def test_code_block(self):
        node = TextNode(
            "This is text with a *italics block* word", TextType.text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "*", TextType.text_type_italic)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.text_type_text, None),
                TextNode("italics block", TextType.text_type_italic, None),
                TextNode(" word", TextType.text_type_text, None),
            ],
        )

    def test_leaf_node(self):
        leaf_node = LeafNode("p", "This is a **random** paragraph", None)
        new_nodes = split_nodes_delimiter([leaf_node], "**", TextType.text_type_bold)
        self.assertEqual(new_nodes, [leaf_node])
