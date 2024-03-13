class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_text = ""
        if self.props == None:
            return html_text
        for k, v in self.props.items():
            html_text += f' {k}="{v}"'
        return html_text

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        self.tag = tag
        self.children = children
        super().__init__(tag=self.tag, value=None, children=self.children, props=None)

    def to_html(self):
        str_repr = f"<{self.tag}>"
        if self.tag == None:
            raise ValueError
        if self.children == None:
            raise ValueError("Children are not present")
        for child in self.children:
            node = child
            str_repr += node.to_html()
        str_repr += f"</{self.tag}>"
        return str_repr
