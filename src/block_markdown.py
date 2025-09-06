from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    U_LIST = "unordered_list"
    O_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = map(lambda block: block.strip(), markdown.split("\n\n"))
    return list(filter(lambda block: block != "", blocks))

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