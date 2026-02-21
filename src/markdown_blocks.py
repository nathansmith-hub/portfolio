from textnode import (
    TextNode,
    TextType,
    text_node_to_html_node,
)

from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode,
)

from inline_markdown import text_to_textnodes

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

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children

def markdown_to_html_node(markdown):
    html_block_nodes = []
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.HEADING:
            stripped = block.lstrip("#")
            count = len(block) - len(stripped)
            tag = f"h{count}"
            text = stripped.lstrip()
            children = text_to_children(text)
            html_block_nodes.append(ParentNode(tag, children))

        elif block_type == BlockType.CODE:
            text_type = TextType.CODE
            text = block[4:-3]
            text_node = TextNode(text, text_type)
            code_node = text_node_to_html_node(text_node)
            html_block_nodes.append(ParentNode("pre", [code_node]))

        elif block_type == BlockType.QUOTE:
            lines = block.splitlines()
            processed = [line.lstrip(">").removeprefix(" ") for line in lines]
            text = '\n'.join(processed)
            tag = "blockquote"
            children = text_to_children(text)
            html_block_nodes.append(ParentNode(tag, children))

        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.splitlines()
            li_nodes = []
            for line in lines:
                text = line.removeprefix("- ")
                tag = "li"
                children = text_to_children(text)
                li_nodes.append(ParentNode(tag, children))
            tag = "ul"
            html_block_nodes.append(ParentNode(tag, li_nodes))

        elif block_type == BlockType.ORDERED_LIST:
            lines = block.splitlines()
            li_nodes = []
            for line in lines:
                pos = line.find(". ")
                if pos != -1:
                    text = line[pos + 2:]
                tag = "li"
                children = text_to_children(text)
                li_nodes.append(ParentNode(tag, children))
            tag = "ol"
            html_block_nodes.append(ParentNode(tag, li_nodes))

        else:
            text = block.replace("\n", " ")
            tag = "p"
            children = text_to_children(text)
            html_block_nodes.append(ParentNode(tag, children))

    return ParentNode("div", html_block_nodes)
