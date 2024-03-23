from typing import Counter
from markdown_to_blocks import BlockType
from htmlnode import ParentNode, LeafNode
from text_to_textnodes import text_to_textnode
from convert_textnode_to_htmlnode import text_node_to_html_node
from markdown_to_blocks import markdown_to_blocks, block_to_block_type


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
    heading_children = []
    for text in block.splitlines():
        heading_hash = text.split(" ")[0]
        heading_text = " ".join(text.split(" ")[1:])
        heading_count = Counter(heading_hash)["#"]
        if heading_count in heading_dict:
            heading_children.append(LeafNode(heading_dict[heading_count], heading_text))
        else:
            heading_children.append(LeafNode("p", text))
    return heading_children


def convert_to_code(block):
    # Remove the first code lines
    block = block[3:]
    # Remove the last code lines
    block = block[:-3]
    code = ""
    for text in block.splitlines():
        code += text + "\n"
    code = code[:-1]
    code_node = LeafNode("code", code)
    pre_node = ParentNode("pre", [code_node])
    return pre_node


def convert_to_unordered_list(block):
    unordered_list_children = []
    for text in block.splitlines():
        unordered_list_children.append(LeafNode("li", text[2:]))
    unordered_list = ParentNode("ul", unordered_list_children)
    return unordered_list


def convert_to_ordered_list(block):
    ordered_list_children = []
    for text in block.splitlines():
        ordered_list_children.append(LeafNode("li", text[3:]))
    ordered_list = ParentNode("ol", ordered_list_children)
    return ordered_list


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_types = []
    for block in blocks:
        block_types.append(block_to_block_type(block))
    block_tuples = zip(blocks, block_types)
    children_nodes = []
    block_type_to_function = {
        BlockType.block_type_quote: convert_to_quote,
        BlockType.block_type_paragraph: convert_to_paragraph,
        BlockType.block_type_code: convert_to_code,
        BlockType.block_type_heading: convert_to_heading,
        BlockType.block_type_unordered_list: convert_to_unordered_list,
        BlockType.block_type_ordered_list: convert_to_ordered_list,
    }
    for block_tuple in block_tuples:
        children_nodes.append(block_type_to_function[block_tuple[1]](block_tuple[0]))
    div_node = ParentNode("div", children_nodes)
    return div_node
