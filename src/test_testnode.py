import unittest
from textnode import TextNode, TextType

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
        node = TextNode("This is a test node", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a test node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node, node2)

    # method to test the string representation of a TextNode object
    def test_repr(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT, "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, plain_text, https://www.boot.dev)", repr(node))

if __name__ == "__main__":
    unittest.main()
