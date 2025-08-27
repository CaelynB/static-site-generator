import unittest
from htmlnode import HTMLNode, LeafNode

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

# unit tests for the LeafNode subclass
class TestLeafNode(unittest.TestCase):
    # method to test the rendering of a LeafNode object with a paragraph tag
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        expected = "<p>Hello, world!</p>"
        self.assertEqual(node.to_html(), expected)

    # method to test the rendering of a LeafNode object with an anchor tag and href property
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Boot.dev", {"href": "https://www.boot.dev"})
        expected = '<a href="https://www.boot.dev">Boot.dev</a>'
        self.assertEqual(node.to_html(), expected)

    # method to test the rendering of a LeafNode object with no tag
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        expected = "Hello, world!"
        self.assertEqual(node.to_html(), expected)

    # method to test the rendering of a LeafNode object with multiple properties
    def test_leaf_to_html_multiple_props(self):
        node = LeafNode("span", "Hello world!", {
            "class": "highlight",
            "id": "main"
        })
        expected = '<span class="highlight" id="main">Hello world!</span>'
        self.assertEqual(node.to_html(), expected)

    # method to test the rendering of a LeafNode object with no value (should raise an ValueError)
    def test_leaf_to_html_no_value(self):
        node = LeafNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    # method to test the string representation of a LeafNode object
    def test_leaf_repr(self):
        node = LeafNode("p", "Hello, world!", {"class": "primary"})
        expected = "LeafNode(p, Hello, world!, {'class': 'primary'})"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()
