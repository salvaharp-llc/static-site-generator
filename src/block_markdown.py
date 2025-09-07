from enum import Enum
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    U_LIST = "unordered_list"
    O_LIST = "ordered_list"

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)

def markdown_to_blocks(markdown):
    blocks = map(lambda block: block.strip(), markdown.split("\n\n"))
    return list(filter(lambda block: block != "", blocks))

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.U_LIST:
            return u_list_to_html_node(block)
        case BlockType.O_LIST:
            return o_list_to_html_node(block)
        case _:
            raise ValueError("invalid block type")

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.U_LIST
    if block.startswith("1. "):
        for i in range(len(lines)):
            if not lines[i].startswith(f"{i + 1}. "):
                return BlockType.PARAGRAPH
        return BlockType.O_LIST
    return BlockType.PARAGRAPH    

def paragraph_to_html_node(block):
    paragraph = " ".join(block.split("\n"))
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    i = 0
    while block[i] == "#":
        i += 1
    text = block[i + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{i}", children)

def code_to_html_node(block):
    text = block.strip("```")[1:]
    text_node = TextNode(text, TextType.CODE)
    children = [text_node_to_html_node(text_node)]
    return ParentNode("pre", children)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = list(map(lambda line: line.lstrip(">").strip(), lines))
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def u_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def o_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)
    
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return list(map(text_node_to_html_node, text_nodes))