from typing import Counter
from markdown_to_blocks import BlockType
from htmlnode import ParentNode
from leafnode import LeafNode
from text_to_textnodes import text_to_textnode
from convert_textnode_to_htmlnode import text_node_to_html_node


def text_to_children(text_nodes):
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def convert_to_paragraph(block):
    paragraph = " ".join(block.split("\n"))
    text_nodes = text_to_textnode(paragraph)
    children = text_to_children(text_nodes)
    paragraph_node = ParentNode("p", children)
    return paragraph_node


def convert_to_quote(block):
    quote = ""
    for text in block.splitlines():
        quote += text[2:] + "\n"
    quote = quote[:-1]
    quote_node = LeafNode("blockquote", quote)
    return quote_node


def convert_to_heading(block):
    heading_dict = {1: "h1", 2: "h2", 3: "h3", 4: "h4", 5: "h5", 6: "h6"}
    heading = ""
    for text in block:
        heading_hash = text.split(" ")[0]
        heading_text = " ".join(text.split(" ")[1:])
        heading_count = Counter(heading_hash)["#"]
        if heading_count in heading_dict:
            heading += f"<{heading_dict[heading_count]}>{heading_text}</{heading_dict[heading_count]}>\n"
        else:
            heading += "<p>" + text + "</p>" + "\n"
    return heading


def convert_to_code(block):
    # Remove the first code lines
    block[0] = block[0][3:]
    # Remove the last code lines
    block[-1] = block[-1][:-3]
    code = "<pre>\n<code>\n"
    for text in block:
        code += text + "\n"
    code += "</code>\n</pre>"
    return code


def convert_to_unordered_list(block):
    unordered_list = "<ul>\n"
    for text in block:
        unordered_list += f"<li>{text[2:]}</li>\n"
    unordered_list += "</ul>"
    return unordered_list


def convert_to_ordered_list(block):
    ordered_list = "<ol>\n"
    for text in block:
        ordered_list += f"<li>{text[3:]}</li>\n"
    ordered_list += "</ol>"
    return ordered_list
