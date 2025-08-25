import unittest
from htmlnode import HTMLNode

# unit tests for the HTMLNode class
class TestHTMLNode(unittest.TestCase):
    # method to test the props_to_html method of the HTMLNode class
    def test_to_html_props(self):
        node = HTMLNode("div", "Hello, world!", None, {
            "class": "greeting",
            "href": "https://www.boot.dev"
        })
        expected = ' class="greeting" href="https://www.boot.dev"'
        self.assertEqual(node.props_to_html(), expected)

    # method to test the initialization of a HTMLNode object
    def test_values(self):
        node = HTMLNode("div", "Hello, world!")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello, world!")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    # method to test the string representation of a HTMLNode object
    def test_repr(self):
        node = HTMLNode("p", "Hello, world!", None, {"class": "primary"})
        expected = "HTMLNode(p, Hello, world!, children: None, {'class': 'primary'})"
        self.assertEqual(repr(node), expected)
