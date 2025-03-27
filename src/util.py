import re
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

def extract_markdown_images(text):
    filter_param = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(filter_param, text)
    return matches
            
def extract_markdown_links(text):
    filter_param = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(filter_param, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            extracted_tuples = extract_markdown_images(node.text)
            
            if len(extracted_tuples) > 0: # Split occurrs
                current_node = node
                for curr_tuple in extracted_tuples:
                    delimiter = f"![{curr_tuple[0]}]({curr_tuple[1]})"
                    node_split_texts = current_node.text.split(delimiter, maxsplit=1)

                    new_nodes.append(TextNode(node_split_texts[0], TextType.TEXT))
                    new_nodes.append(TextNode(curr_tuple[0], TextType.IMAGE, curr_tuple[1]))
                    current_node = TextNode(node_split_texts[1], TextType.TEXT)
                
                if len(current_node.text) > 0:
                    new_nodes.append(current_node)

            else: # No Split Needed
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            extracted_tuples = extract_markdown_links(node.text)
            
            if len(extracted_tuples) > 0: # Split occurrs
                current_node = node
                for curr_tuple in extracted_tuples:
                    delimiter = f"[{curr_tuple[0]}]({curr_tuple[1]})"
                    node_split_texts = current_node.text.split(delimiter, maxsplit=1)

                    new_nodes.append(TextNode(node_split_texts[0], TextType.TEXT))
                    new_nodes.append(TextNode(curr_tuple[0], TextType.LINK, curr_tuple[1]))
                    current_node = TextNode(node_split_texts[1], TextType.TEXT)
                
                if len(current_node.text) > 0:
                    new_nodes.append(current_node)
                    
            else: # No Split Needed
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes