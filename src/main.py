from textnode import TextNode, TextType

def main():
    # create an instance of TextNode and print its string representation
    node = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
    print(node)

main()
