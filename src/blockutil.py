from textnode import *
from htmlnode import *

def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    blocks = []
    for block in split_markdown:
        if block != "" or block !="\n":
            blocks.append(block.strip())
    return blocks