from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


def text_to_textnode(text):
    node = TextNode(text, TextType.text_type_text)
    bold_split = split_nodes_delimiter([node], "**", TextType.text_type_bold)
    italic_split = split_nodes_delimiter(bold_split, "*", TextType.text_type_italic)
    code_split = split_nodes_delimiter(italic_split, "`", TextType.text_type_code)
    image_split = split_nodes_image(code_split)
    link_split = split_nodes_link(image_split)
    return link_split
