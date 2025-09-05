from enum import Enum
from htmlnode import LeafNode
import re

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

# function to split a TextNode object by a delimiter and wrap its parts in the specified text type
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # initialize an empty list to hold the new nodes
    new_nodes = []

    # for each node in the old nodes list
    for node in old_nodes:
        # if the node is not plain text, add it to the new nodes list and continue
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        
        # initialize an empty list to hold the parts of the split text (currently unused; reserved for future logic)
        parts = []

        # split the text into sections using the delimiter
        sections = node.text.split(delimiter)

        # if the number of sections is even, raise an exception with a message
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")

        # for each section index in the sections list
        for i in range(len(sections)):
            # if the section is empty, continue to the next section
            if sections[i] == "":
                continue

            # if the index is even, create a plain text TextNode
            if i % 2 == 0:
                new_nodes.append(TextNode(sections[i], TextType.PLAIN_TEXT))
            # otherwise, create a formatted TextNode
            else:
                new_nodes.append(TextNode(sections[i], text_type))

        # extend the new nodes list with the parts list (currently unused; reserved for future logic)
        new_nodes.extend(parts)

    # return the final list of new nodes
    return new_nodes

# function to extract markdown image syntax from a string
def extract_markdown_images(text):
    # regex pattern to match markdown image syntax: ![alt text](url)
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

    # find all matches of the pattern in the text
    matches = re.findall(pattern, text)

    # return a list of (alt_text, url) tuples for each match
    return matches

# function to extract markdown link syntax from a string
def extract_markdown_links(text):
    # regex pattern to match markdown link syntax: [link text](url)
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

    # find all matches of the pattern in the text
    matches = re.findall(pattern, text)

    # return a list of (link_text, url) tuples for each match
    return matches
