

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        return_text = ""
        if self.props is None:
            return return_text

        for prop in self.props:
            return_text = return_text + f' {prop}="{self.props[prop]}"'
        return return_text
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if(self.value == None):
            raise ValueError("LeafNodes must have a value.")
        
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if(self.tag == None):
            raise ValueError("ParentNodes must have a tag.")
        if(self.children == None):
            raise ValueError("ParentNodes must have children.")
        
        children_string = ""
        for child in self.children:
            children_string += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"