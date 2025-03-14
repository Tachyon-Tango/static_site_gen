from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD   = "bold"
    ITALIC = "italic"
    CODE   = "code"
    LINK   = "link"
    IMAGE  = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(text_node_1, text_node_2):
        if(text_node_1.text == text_node_2.text
            and text_node_1.text_type == text_node_2.text_type
            and text_node_1.url == text_node_2.url):
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

