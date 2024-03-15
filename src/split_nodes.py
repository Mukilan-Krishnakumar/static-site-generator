from leafnode import LeafNode
from textnode import TextType, TextNode

allowed_delimiter = {
    "`": TextType.text_type_code,
    "**": TextType.text_type_bold,
    "*": TextType.text_type_italic,
}


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if type(node) != TextNode:
            new_nodes.append(node)
        else:
            if delimiter in allowed_delimiter.keys():
                split_nodes = node.text.split(delimiter)
                if len(split_nodes) % 2 == 0:
                    raise ValueError(f"Closing {delimiter} not found")
                node_list = []
                for num, i in enumerate(split_nodes):
                    if num % 2 != 0:
                        node_list.append(TextNode(i, allowed_delimiter[delimiter]))
                    else:
                        node_list.append(TextNode(i, TextType.text_type_text))
                new_nodes.extend(node_list)
    return new_nodes
