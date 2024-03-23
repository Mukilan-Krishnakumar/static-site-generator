import unittest
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode


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

    def test_split_image_nodes(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.text_type_text,
        )
        new_nodes = split_nodes_image([node])
        check_nodes = [
            TextNode("This is text with an ", TextType.text_type_text),
            TextNode(
                "image", TextType.text_type_image, "https://i.imgur.com/zjjcJKZ.png"
            ),
            TextNode(" and another ", TextType.text_type_text),
            TextNode(
                "second image",
                TextType.text_type_image,
                "https://i.imgur.com/3elNhQu.png",
            ),
        ]
        self.assertEqual(new_nodes, check_nodes)

    def test_split_link_nodes(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            TextType.text_type_text,
        )
        check_nodes = [
            TextNode("This is text with a ", TextType.text_type_text),
            TextNode("link", TextType.text_type_link, "https://www.example.com"),
            TextNode(" and ", TextType.text_type_text),
            TextNode(
                "another",
                TextType.text_type_link,
                "https://www.example.com/another",
            ),
        ]
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, check_nodes)

    def test_combination_nodes_image(self):
        node = TextNode(
            "This is a text with a ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](http://www.example.com)",
            TextType.text_type_text,
        )
        new_nodes = split_nodes_image([node])
        check_nodes = [
            TextNode("This is a text with a ", TextType.text_type_text),
            TextNode(
                "image", TextType.text_type_image, "https://i.imgur.com/zjjcJKZ.png"
            ),
            TextNode(" and a [link](http://www.example.com)", TextType.text_type_text),
        ]
        self.assertEqual(new_nodes, check_nodes)

    def test_combination_nodes_link(self):
        node = TextNode(
            "This is a text with a ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](http://www.example.com)",
            TextType.text_type_text,
        )
        new_nodes = split_nodes_link([node])
        check_nodes = [
            TextNode(
                "This is a text with a ![image](https://i.imgur.com/zjjcJKZ.png) and a ",
                TextType.text_type_text,
            ),
            TextNode("link", TextType.text_type_link, "http://www.example.com"),
        ]
        self.assertEqual(new_nodes, check_nodes)

    def test_empty_nodes_image(self):
        node = TextNode("", TextType.text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [])

    def test_empty_nodes_link(self):
        node = TextNode("", TextType.text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [])

    def test_same_images_nodes(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.text_type_text,
        )
        new_nodes = split_nodes_image([node])
        check_nodes = [
            TextNode("This is text with an ", TextType.text_type_text),
            TextNode(
                "image", TextType.text_type_image, "https://i.imgur.com/zjjcJKZ.png"
            ),
            TextNode(" and another ", TextType.text_type_text),
            TextNode(
                "image", TextType.text_type_image, "https://i.imgur.com/zjjcJKZ.png"
            ),
        ]
        self.assertEqual(new_nodes, check_nodes)

    def test_same_link_nodes(self):
        node = TextNode(
            "This is a text with a [link](https://www.example.com) and a [link](https://www.example.com)",
            TextType.text_type_text,
        )
        new_nodes = split_nodes_link([node])
        check_nodes = [
            TextNode("This is a text with a ", TextType.text_type_text),
            TextNode("link", TextType.text_type_link, "https://www.example.com"),
            TextNode(" and a ", TextType.text_type_text),
            TextNode("link", TextType.text_type_link, "https://www.example.com"),
        ]
        self.assertEqual(new_nodes, check_nodes)
