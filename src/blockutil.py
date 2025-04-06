from textnode import *
from htmlnode import *

class BlockType(Enum):
    PARAGRAPH       = "paragraph"     
    HEADING         = "heading"       
    CODE            = "code"          
    QUOTE           = "quote"         
    UNORDERED_LIST  = "unordered_list"
    ORDERED_LIST    = "ordered_list"  

def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    blocks = []
    for block in split_markdown:
        if block != "" or block !="\n":
            blocks.append(block.strip())
    return blocks


def isHeadingBlock(markdown):
    return markdown[:2] == "# " or \
    markdown[:3] == "## " or \
    markdown[:4] == "### " or \
    markdown[:5] == "#### " or \
    markdown[:6] == "##### " or \
    markdown[:7] == "###### "

def isCodeBlock(markdown):
    return markdown[:3] == "```" and markdown[-3:] == "```"

def isQuoteBlock(markdown):
    split_lines = markdown.split("\n")
    if len(split_lines) == 0:
        return False
    for line in split_lines:
        if not(line[0] == ">"):
            return False
    return True

def isUnorderedListBlock(markdown):
    split_lines = markdown.split("\n")
    if len(split_lines) == 0:
        return False
    for line in split_lines:
        if not(line[:2] == "- "):
            return False
    return True

def isOrderedListBlock(markdown):
    split_lines = markdown.split("\n")
    current_num = 0
    if len(split_lines) == 0:
        return False
    for line in split_lines:
        words = line.split(" ")
        current_num += 1
        if len(words) == 0:
            return False
        if not(words[0] == f"{current_num}."):
            return False
    return True


def block_to_block_type(markdown):
    if isHeadingBlock(markdown):
        return BlockType.HEADING
    elif isCodeBlock(markdown):
        return BlockType.CODE
    elif isQuoteBlock(markdown):
        return BlockType.QUOTE
    elif isUnorderedListBlock(markdown):
        return BlockType.UNORDERED_LIST
    elif isOrderedListBlock(markdown):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH




