def markdown_to_blocks(markdown):
    blocks = []
    split_markdown = markdown.split("\n\n")

    for split in split_markdown:
        stripped_markdown = split.strip()
        if stripped_markdown != "":
            blocks.append(stripped_markdown)

    return blocks
