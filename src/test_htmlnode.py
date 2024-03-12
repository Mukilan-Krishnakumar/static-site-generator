import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "<a>", "Hey this is a link", None, {"href": "https://localhost:3000"}
        )
        from_func = node.props_to_html()
        actucal_repr = ' href="https://localhost:3000"'
        self.assertEqual(from_func, actucal_repr)

    def test_repr(self):
        node = HTMLNode(
            "<a>", "Hey this is a link", None, {"href": "https://localhost:3000"}
        )
        actual_repr = str(
            "HTMLNode(<a>, Hey this is a link, None, {'href': 'https://localhost:3000'})"
        )
        self.assertEqual(str(node), actual_repr)
