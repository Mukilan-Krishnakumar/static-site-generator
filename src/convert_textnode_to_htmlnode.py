from textnode import TextNode
from leafnode import LeafNode


def text_node_to_html_node(text_node):
    if text_node.text_type == "text_type_text":
        return LeafNode(value=text_node.text)
    elif text_node.text_type == "text_type_bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type == "text_type_italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type == "text_type_code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type == "text_type_link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == "text_type_image":
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("Not a valid text type")
