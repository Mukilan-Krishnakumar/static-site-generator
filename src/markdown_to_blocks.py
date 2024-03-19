from enum import Enum
import re


class BlockType(Enum):
    block_type_paragraph = "paragraph"
    block_type_heading = "heading"
    block_type_code = "code"
    block_type_quote = "quote"
    block_type_unordered_list = "unordered_list"
    block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    split_blocks = markdown.split("\n\n")
    mkdwn_blocks = []
    for num, split_text in enumerate(split_blocks):
        curr_block = []
        individual_blocks = split_text.splitlines()
        for element in individual_blocks:
            if element not in ["", "\n"]:
                curr_block.append(" ".join(element.split()))
        mkdwn_blocks.append(curr_block)
    # print(mkdwn_blocks)
    return mkdwn_blocks


def block_to_block_type(block):
    num_list = [str(n) for n in range(1, len(block) + 1)]
    created_num_list = []
    for num, text in enumerate(block):
        if re.match(r"(?<!#)#{1,6} \w*", text) != None:
            return BlockType.block_type_heading
        num_search = re.search(f"^(\d). ", text)
        if num_search != None:
            created_num_list.append(num_search.group(1))
    if created_num_list == num_list:
        return BlockType.block_type_ordered_list
    if block[0][:3] == "```" and block[-1][-3:] == "```":
        return BlockType.block_type_code
    initial_characters = [word[0] for word in block]
    if all(flag == ">" for flag in initial_characters):
        return BlockType.block_type_quote
    elif all(flag == "*" for flag in initial_characters):
        return BlockType.block_type_unordered_list
    elif all(flag == "-" for flag in initial_characters):
        return BlockType.block_type_unordered_list
    return BlockType.block_type_paragraph
