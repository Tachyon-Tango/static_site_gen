from textnode import *

def main():
    new_text = TextNode("This is some link.", TextType.LINK, "https://www.boot.dev")
    print(str(new_text))


main()