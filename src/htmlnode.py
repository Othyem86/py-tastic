class HTMLNode:
    def __init__(
            self,
            tag:str = None,
            value:str = None,
            children: list['HTMLNode'] = None,
            props: dict[str, str] = None
        ) -> None:
        self.tag = tag
        self.value = value
        self.childre = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError()
    
    def props_to_html(self) -> str:
        if not self.props:
            return ""
        html_props = ""
        for prop in self.props:
            html_props += f' {prop}="{self.props[prop]}"'
        return html_props

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(
            self, 
            tag: str = None, 
            value: str = None, 
            props: dict[str, str] = None
        )-> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError()
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}<{self.tag}/>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"