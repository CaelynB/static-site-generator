import unittest
from textnode import TextNode, TextType, text_node_to_html_node

# unit tests for the TextNode class
class TestTextNode(unittest.TestCase):
    # method to test equality between two identical TextNode objects
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    # method to test inequality between two different TextNode objects
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        node2 = TextNode("This is a different text node", TextType.PLAIN_TEXT)
        self.assertNotEqual(node, node2)

    # method to test inequality between two TextNode objects with different text types
    def test_properties_not_eq(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

    # method to test equality between two TextNode objects with the same url
    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.PLAIN_TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)

    # method to test the string representation of a TextNode object
    def test_repr(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT, "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, plain_text, https://www.boot.dev)", repr(node))

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

# unit tests for the text_node_to_html_node function
class TestTextNodeToHTMLNode(unittest.TestCase):
    # method to test conversion of a plain text TextNode to a LeafNode
    def test_plain_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    # method to test conversion of a bold TextNode to a LeafNode
    def test_bold_text(self):
        node = TextNode("This is a bold text node", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    # method to test conversion of an italic TextNode to a LeafNode
    def test_italic_text(self):
        node = TextNode("This is an italic text node", TextType.ITALIC_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")

    # method to test conversion of a code TextNode to a LeafNode
    def test_code_text(self):
        node = TextNode("This is a code text node", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")

    # method to test conversion of a link TextNode to a LeafNode
    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

    # method to test conversion of an image TextNode to a LeafNode
    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {
            "src": "https://www.boot.dev",
            "alt": "This is an image"
        })

    # method to test that an invalid text type raises a ValueError
    def test_invalid_text_type(self):
        node = TextNode("This is an invalid text type", "invalid_type")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()
