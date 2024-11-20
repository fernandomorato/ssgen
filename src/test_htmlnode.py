import unittest

from htmlnode import HTMLNode
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):

    def test_repr(self):
        node = HTMLNode("p", "um paragrafo")
        self.assertEqual("HTMLNode(p, um paragrafo, None, None)", repr(node))

    def test_repr_list(self):
        node = HTMLNode(
            tag="ul",
            children=[
                HTMLNode("li", "Coffee"),
                HTMLNode("li", "Tea"),
                HTMLNode("li", "Milk"),
            ],
        )
        self.assertEqual(
            "HTMLNode(ul, None, [HTMLNode(li, Coffee, None, None), HTMLNode(li, Tea, None, None), HTMLNode(li, Milk, None, None)], None)",
            repr(node),
        )

    def test_repr_hyperlink(self):
        node = HTMLNode(tag="a", value="link", props={"href": "https://www.google.com"})
        self.assertEqual(
            "HTMLNode(a, link, None, {'href': 'https://www.google.com'})", repr(node)
        )

    def test_repr_props(self):
        node = HTMLNode(tag="link", props={"rel": "stylesheet", "href": "styles.css"})
        self.assertEqual(
            "HTMLNode(link, None, None, {'rel': 'stylesheet', 'href': 'styles.css'})",
            repr(node),
        )

    def test_props_to_html(self):
        node = HTMLNode(tag="link", props={"rel": "stylesheet", "href": "styles.css"})
        self.assertEqual(
            'rel="stylesheet" href="styles.css"',
            node.props_to_html(),
        )


if __name__ == "__main__":
    unittest.main()
