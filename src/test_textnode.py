import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("Another text node", "bold", None)
        node2 = TextNode("Another text node", "bold")
        self.assertEqual(node, node2)

    def test_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italics")
        self.assertNotEqual(node, node2)

    def test_test(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different node", "bold")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
