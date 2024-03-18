import unittest
from text_to_textnodes import text_to_textnode
from textnode import TextNode, TextType


class TestTextNodeConversion(unittest.TestCase):
    def test_textnode(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        new_nodes = text_to_textnode(text)
        check_nodes = [
            TextNode("This is ", TextType.text_type_text),
            TextNode("text", TextType.text_type_bold),
            TextNode(" with an ", TextType.text_type_text),
            TextNode("italic", TextType.text_type_italic),
            TextNode(" word and a ", TextType.text_type_text),
            TextNode("code block", TextType.text_type_code),
            TextNode(" and an ", TextType.text_type_text),
            TextNode(
                "image", TextType.text_type_image, "https://i.imgur.com/zjjcJKZ.png"
            ),
            TextNode(" and a ", TextType.text_type_text),
            TextNode("link", TextType.text_type_link, "https://boot.dev"),
        ]
        self.assertEqual(new_nodes, check_nodes)
