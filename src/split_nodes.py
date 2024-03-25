from htmlnode import LeafNode
from textnode import TextType, TextNode
from extract import extract_markdown_links, extract_markdown_images

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
            if node.text_type != TextType.text_type_text:
                new_nodes.append(node)
                continue
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


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if type(node) == TextNode:
            if node.text_type != TextType.text_type_text:
                new_nodes.append(node)
                continue
        extracted_images = extract_markdown_images(node.text)
        if extracted_images == None:
            new_nodes.append(node)
        else:
            text_val = node.text
            for extracted_image in extracted_images:
                print(extracted_image[1])
                split_text = text_val.split(
                    f"![{extracted_image[0]}]({extracted_image[1]})", 1
                )
                if len(split_text) < 1:
                    continue
                new_nodes.append(TextNode(split_text[0], TextType.text_type_text))
                new_nodes.append(
                    TextNode(
                        extracted_image[0],
                        TextType.text_type_image,
                        "." + extracted_image[1],
                    )
                )
                text_val = split_text[1]
            if len(text_val) > 0:
                new_nodes.append(TextNode(text_val, TextType.text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if type(node) == TextNode:
            if node.text_type != TextType.text_type_text:
                new_nodes.append(node)
                continue
        extracted_links = extract_markdown_links(node.text)
        if extracted_links == None:
            new_nodes.append(node)
        else:
            text_val = node.text
            for extracted_link in extracted_links:
                split_text = text_val.split(
                    f"[{extracted_link[0]}]({extracted_link[1]})", 1
                )
                if len(split_text) < 1:
                    continue
                new_nodes.append(TextNode(split_text[0], TextType.text_type_text))
                new_nodes.append(
                    TextNode(
                        extracted_link[0], TextType.text_type_link, extracted_link[1]
                    )
                )
                text_val = split_text[1]
            if len(text_val) > 0:
                new_nodes.append(TextNode(text_val, TextType.text_type_text))
    return new_nodes
