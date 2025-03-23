from textnode import *
from htmlnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            node_split_texts = node.text.split(delimiter, maxsplit=2)
            if len(node_split_texts) == 3: # Split occurrs
                new_nodes.append(TextNode(node_split_texts[0], TextType.TEXT))
                new_nodes.append(TextNode(node_split_texts[1], text_type))
                new_nodes.append(TextNode(node_split_texts[2], TextType.TEXT))
            elif len(node_split_texts) == 1: # No Split Needed
                new_nodes.append(node)
            else:
                raise Exception("Incomplete delimiter found on: " + str(node.text))
        else:
            new_nodes.append(node)
    return new_nodes

            

            