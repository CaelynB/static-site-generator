import unittest
from textnode import (
    TextNode,
    TextType,
    text_node_to_html_node,
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
)

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

# unit tests for the split_nodes_delimiter function
class TestSplitNodesDelimiter(unittest.TestCase):
    # method to test splitting a TextNode with a bold delimiter
    def test_bold_delimiter(self):
        node = TextNode("This is **bold** text", TextType.PLAIN_TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        expected = [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" text", TextType.PLAIN_TEXT)
        ]
        self.assertEqual(result, expected)

    # method to test splitting a TextNode with a double bold delimiter
    def test_double_bold_delimiter(self):
        node = TextNode("This is **bold** and **more bold** text", TextType.PLAIN_TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        expected = [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" and ", TextType.PLAIN_TEXT),
            TextNode("more bold", TextType.BOLD_TEXT),
            TextNode(" text", TextType.PLAIN_TEXT)
        ]
        self.assertEqual(result, expected)

    # method to test splitting a TextNode with a multiword bold delimiter
    def test_multiword_bold_delimiter(self):
        node = TextNode("This is **bold text**", TextType.PLAIN_TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        expected = [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("bold text", TextType.BOLD_TEXT)
        ]
        self.assertEqual(result, expected)

    # method to test splitting a TextNode with a italic delimiter
    def test_italic_delimiter(self):
        node = TextNode("This is _italic_ text", TextType.PLAIN_TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        expected = [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" text", TextType.PLAIN_TEXT)
        ]
        self.assertEqual(result, expected)

    # method to test splitting a TextNode with a bold and italic delimiter
    def test_bold_and_italic_delimiter(self):
        node = [
            TextNode("This is **bold** and ", TextType.PLAIN_TEXT),
            TextNode("_italic_ text", TextType.PLAIN_TEXT)
        ]
        result = split_nodes_delimiter(node, "**", TextType.BOLD_TEXT)
        result = split_nodes_delimiter(result, "_", TextType.ITALIC_TEXT)
        expected = [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" and ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" text", TextType.PLAIN_TEXT)
        ]
        self.assertEqual(result, expected)

    # method to test splitting a TextNode with a code delimiter
    def test_code_delimiter(self):
        node = TextNode("This is `code` text", TextType.PLAIN_TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        expected = [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("code", TextType.CODE_TEXT),
            TextNode(" text", TextType.PLAIN_TEXT)
        ]
        self.assertEqual(result, expected)

    # method to test that splitting a TextNode with an unmatched delimiter raises a ValueError
    def test_unmatched_delimiter(self):
        node = TextNode("This is **bold text", TextType.PLAIN_TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)

# unit tests for the extract_markdown_images function
class TestExtractMarkdownImage(unittest.TestCase):
    # method to test extraction of a single markdown image
    def test_single_image(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertListEqual(expected, matches)

    # method to test extraction of multiple markdown images
    def test_multiple_images(self):
        matches = extract_markdown_images("![image](https://i.imgur.com/zjjcJKZ.png) and ![image](https://i.imgur.com/zjjcJKZ.png)")
        expected = [
            ("image", "https://i.imgur.com/zjjcJKZ.png"),
            ("image", "https://i.imgur.com/zjjcJKZ.png")
        ]
        self.assertListEqual(expected, matches)

    # method to test that no images are extracted from text without images
    def test_text_without_images(self):
        matches = extract_markdown_images("This has no images.")
        expected = []
        self.assertListEqual(expected, matches)

    # method to test that malformed image syntax is ignored
    def test_ignores_malformed_image(self):
        matches = extract_markdown_images("![alt text](missing-parenthesis")
        expected = []
        self.assertListEqual(expected, matches)

# unit tests for the extract_markdown_links function
class TestExtractMarkdownLinks(unittest.TestCase):
    # method to test extraction of a single markdown link
    def test_single_link(self):
        matches = extract_markdown_links("This is text with a [link](https://boot.dev)")
        expected = [("link", "https://boot.dev")]
        self.assertListEqual(expected, matches)

    # method to test extraction of multiple markdown links
    def test_multiple_links(self):
        matches = extract_markdown_links("This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)")
        expected = [
            ("link", "https://boot.dev"),
            ("another link", "https://blog.boot.dev"),
        ]
        self.assertListEqual(expected, matches)

    # method to test that no links are extracted from text without links
    def test_text_without_links(self):
        matches = extract_markdown_links("Nothing to link here.")
        expected = []
        self.assertListEqual(expected, matches)

    # method to test that image syntax is ignored when extracting links
    def test_ignores_image_links(self):
        matches = extract_markdown_links("![image](https://i.imgur.com/zjjcJKZ.png)")
        expected = []
        self.assertListEqual(expected, matches)

    # method to test that malformed link syntax is ignored
    def test_ignores_malformed_link(self):
        matches = extract_markdown_links("[broken](missing-parenthesis")
        expected = []
        self.assertListEqual(expected, matches)

# unit tests for the split_nodes_image function
class TestSplitNodesImage(unittest.TestCase):
    # method to test splitting a TextNode with multiple markdown images into individual TextNodes
    def test_multiple_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN_TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
            ],
            new_nodes
        )

    # method to test splitting a TextNode with a single markdown image into a single TextNode
    def test_single_image(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")], new_nodes)

    # method to test that a TextNode without any markdown images remains unchanged
    def test_no_image(self):
        node = TextNode("This is text without any images", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    # method to test that a TextNode with malformed markdown image syntax is ignored
    def test_malformed_image_ignored(self):
        node = TextNode("This has a malformed ![image](https://i.imgur.com/zjjcJKZ.png", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

# unit tests for the split_nodes_link function
class TestSplitNodesLink(unittest.TestCase):
    # method to test splitting a TextNode with multiple markdown links into individual TextNodes
    def test_multiple_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.PLAIN_TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.PLAIN_TEXT),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.PLAIN_TEXT)
            ], 
            new_nodes
        )

    # method to test splitting a TextNode with a single markdown link into a single TextNode
    def test_single_link(self):
        node = TextNode("[link](https://boot.dev)", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("link", TextType.LINK, "https://boot.dev")], new_nodes)

    # method to test that a TextNode without any markdown links remains unchanged
    def test_no_link(self):
        node = TextNode("This is text without any links", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    # method to test that a TextNode with malformed markdown link syntax is ignored
    def test_malformed_link_ignored(self):
        node = TextNode("This is a malformed [link](https://boot.dev", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

# unit tests for the text_to_textnodes function
class TestTextToTextNodes(unittest.TestCase):
    # method to test conversion of plain text into a list of TextNode objects
    def test_plain_text_only(self):
        nodes = text_to_textnodes("This is plain text")
        self.assertListEqual([TextNode("This is plain text", TextType.PLAIN_TEXT)], nodes)

    # method to test conversion of bold markdown text into a list of TextNode objects
    def test_bold_only(self):
        nodes = text_to_textnodes("This is **bold** text")
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAIN_TEXT),
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode(" text", TextType.PLAIN_TEXT)
            ],
            nodes
        )

    # method to test conversion of italic markdown text into a list of TextNode objects
    def test_italic_only(self):
        nodes = text_to_textnodes("This is _italic_ text")
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAIN_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" text", TextType.PLAIN_TEXT)
            ],
            nodes
        )
    
    # method to test conversion of code markdown text into a list of TextNode objects
    def test_code_only(self):
        nodes = text_to_textnodes("This is `code` text")
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAIN_TEXT),
                TextNode("code", TextType.CODE_TEXT),
                TextNode(" text", TextType.PLAIN_TEXT)
            ],
            nodes
        )

    # method to test conversion of image markdown syntax into a list of TextNode objects
    def test_image_only(self):
        nodes = text_to_textnodes("This is an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual(
            [
                TextNode("This is an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            nodes
        )

    # method to test conversion of link markdown syntax into a list of TextNode objects
    def test_link_only(self):
        nodes = text_to_textnodes("This is a [link](https://boot.dev)")
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev")
            ],
            nodes
        )

    # method to test conversion of mixed markdown syntax into a list of TextNode objects
    def test_mixed_markdown(self):
        nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAIN_TEXT),
                TextNode("text", TextType.BOLD_TEXT),
                TextNode(" with an ", TextType.PLAIN_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" word and a ", TextType.PLAIN_TEXT),
                TextNode("code block", TextType.CODE_TEXT),
                TextNode(" and an ", TextType.PLAIN_TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )

    # method to test that unclosed bold markdown syntax raises a ValueError
    def test_unclosed_bold(self):
        text = "This is **not closed"
        with self.assertRaises(ValueError):
                text_to_textnodes(text)

    # method to test that unclosed italic markdown syntax raises a ValueError
    def test_unclosed_italic(self):
        text = "Some _italic text"
        with self.assertRaises(ValueError):
            text_to_textnodes(text)

    # method to test that unclosed code markdown syntax raises a ValueError
    def test_unclosed_code(self):
        text = "Broken `code"
        with self.assertRaises(ValueError):
            text_to_textnodes(text)

if __name__ == "__main__":
    unittest.main()
