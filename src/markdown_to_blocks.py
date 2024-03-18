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
