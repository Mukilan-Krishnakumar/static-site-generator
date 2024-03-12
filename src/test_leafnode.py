import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leafnode = LeafNode(tag="p", value="This is a paragraph of text.")
        str_repr = "<p>This is a paragraph of text.</p>"
        self.assertEqual(leafnode.to_html(), str_repr)

    def test_with_props(self):
        leafnode = LeafNode(
            tag="a", value="Click me!", props={"href": "https://www.google.com"}
        )
        str_repr = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(leafnode.to_html(), str_repr)
