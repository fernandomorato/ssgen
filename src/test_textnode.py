import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.boot.dev")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_init(self):
        text = "text"
        text_type = TextType.LINK
        url = "xalala.com.br"

        node = TextNode(text, text_type, url)

        self.assertEqual(node.text, text)
        self.assertEqual(node.text_type, text_type)
        self.assertEqual(node.url, url)

    def test_repr(self):
        node = TextNode("text", TextType.NORMAL, "https://www.google.com")
        self.assertEqual("TextNode(text, normal, https://www.google.com)", repr(node))


if __name__ == "__main__":
    unittest.main()
