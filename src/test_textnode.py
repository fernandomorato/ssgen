import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_normal(self):
        node_normal = TextNode("This is a text node", TextType.NORMAL)
        html_node_normal = text_node_to_html_node(node_normal)
        self.assertEqual(html_node_normal.tag, None)
        self.assertEqual(html_node_normal.value, "This is a text node")

    def test_bold(self):
        node_bold = TextNode("This is a bold text node", TextType.BOLD)
        html_node_bold = text_node_to_html_node(node_bold)
        self.assertEqual(html_node_bold.tag, "b")
        self.assertEqual(html_node_bold.value, "This is a bold text node")

    def test_italic(self):
        node_italic = TextNode("This is a italic text node", TextType.ITALIC)
        html_node_italic = text_node_to_html_node(node_italic)
        self.assertEqual(html_node_italic.tag, "i")
        self.assertEqual(html_node_italic.value, "This is a italic text node")

    def test_code(self):
        node_code = TextNode("This is a code text node", TextType.CODE)
        html_node_code = text_node_to_html_node(node_code)
        self.assertEqual(html_node_code.tag, "code")
        self.assertEqual(html_node_code.value, "This is a code text node")

    def test_link(self):
        node_link = TextNode("This is a link text node", TextType.LINK)
        html_node_link = text_node_to_html_node(node_link)
        self.assertEqual(html_node_link.tag, "a")
        self.assertEqual(html_node_link.value, "This is a link text node")

    def test_img(self):
        node_img = TextNode("This is a image text node", TextType.IMAGE, "xalala.com")
        html_node_img = text_node_to_html_node(node_img)
        self.assertEqual(html_node_img.tag, "img")
        self.assertEqual(html_node_img.props["alt"], "This is a image text node")
        self.assertEqual(html_node_img.props["src"], "xalala.com")


if __name__ == "__main__":
    unittest.main()
