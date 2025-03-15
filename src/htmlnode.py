

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props == None:
            raise Exception("This HTMLNode has no properties.")
            
        return_text = ""
        for prop in self.props:
            return_text = return_text + " " + str(prop) + '="' + str(self.props[prop]) + '"'
        return return_text
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"