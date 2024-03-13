import unittest

from htmlnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_recursive_functionality(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode("p", [ParentNode("i", [LeafNode("span", "Hello")])]),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        val = node.to_html()
        self.assertTrue(val)

    def test_functionality(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        str_repr = node.to_html()
        self.assertEqual(
            str_repr, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
