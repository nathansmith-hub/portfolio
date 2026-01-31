from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    for line in lines:
        if not line.startswith(">"):
            break
    else:
        return BlockType.QUOTE
    
    for line in lines:
        if not line.startswith("- "):
            break
    else:
        return BlockType.UNORDERED_LIST
    
    num = 0
    for line in lines:
        num += 1
        if not line.startswith(f"{num}. "):
            break
    else:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = []
    split_markdown = markdown.split("\n\n")

    for split in split_markdown:
        stripped_markdown = split.strip()
        if stripped_markdown != "":
            blocks.append(stripped_markdown)

    return blocks
