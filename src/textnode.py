from enum import Enum

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
