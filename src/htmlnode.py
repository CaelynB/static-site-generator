# class representing a node in an html document tree
class HTMLNode:
    # constructor to initialize an HTMLNode object with attributes (tag, value, children, and properties)
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # method to convert the HTMLNode object into html
    def to_html(self):
        raise NotImplementedError("to_html method not implemented") 
    
    # method to convert the properties of the HTMLNode object into a string of html attributes
    def props_to_html(self):
        # if there are no properties, return an empty string
        if self.props is None:
            return ""
        
        # initialize an empty string
        props_html = ""

        # for each property in the props dictionary, append a formatted string to the props_html string
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
            
        # return the final string of html attributes
        return props_html
        
    # method to return a string representation of the HTMLNode object
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
