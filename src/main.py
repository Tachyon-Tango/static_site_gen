from textnode import *
from htmlnode import *

def main():
    new_text = TextNode("This is some link.", TextType.LINK, "https://www.boot.dev")
    print(new_text)

    new_html = HTMLNode("This is a tag,", "This is a value", "This is a child", {"prop": "the property value", "prop2" : "the property value 2"})
    print(new_html)
    print(new_html.props_to_html())

main()