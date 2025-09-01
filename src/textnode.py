from enum import Enum
from htmlnode import LeafNode

# enum representing different types of text formatting
class TextType(Enum):
    PLAIN_TEXT = "plain_text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEXT = "code_text"
    LINK = "link"
    IMAGE = "image"

# class representing a node of text
class TextNode:
    # constructor to initialize a TextNode object with text, a text type, and an optional url
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # method to check equality between two TextNode objects
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    # method to return a string representation of the TextNode object
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
# function to convert a TextNode object into a corresponding LeafNode object
def text_node_to_html_node(text_node):
    # check the text type and create the appropriate LeafNode
    if text_node.text_type == TextType.PLAIN_TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD_TEXT:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC_TEXT:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE_TEXT:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    # otherwise, raise an exception for invalid text types
    else:
        raise ValueError(f"invalid text type: {text_node.text_type}")
