import unittest

from htmlnode import HTMLNode
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):

    def test_repr(self):
        node = HTMLNode("p", "um paragrafo")
        self.assertEqual("HTMLNode(p, um paragrafo, children: None, None)", repr(node))

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
            "HTMLNode(ul, None, children: [HTMLNode(li, Coffee, children: None, None), HTMLNode(li, Tea, children: None, None), HTMLNode(li, Milk, children: None, None)], None)",
            repr(node),
        )

    def test_repr_hyperlink(self):
        node = HTMLNode(tag="a", value="link", props={"href": "https://www.google.com"})
        self.assertEqual(
            "HTMLNode(a, link, children: None, {'href': 'https://www.google.com'})", repr(node)
        )

    def test_repr_props(self):
        node = HTMLNode(tag="link", props={"rel": "stylesheet", "href": "styles.css"})
        self.assertEqual(
            "HTMLNode(link, None, children: None, {'rel': 'stylesheet', 'href': 'styles.css'})",
            repr(node),
        )

    def test_values(self):
        node = HTMLNode(
                "div",
                "Hello, world!",
                None,
                {"class": "greeting", "href": "https://incognia.com"},
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello, world!")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"class": "greeting", "href": "https://incognia.com"})

    def test_props_to_html(self):
        node = HTMLNode(tag="link", props={"rel": "stylesheet", "href": "styles.css"})
        self.assertEqual(
            ' rel="stylesheet" href="styles.css"',
            node.props_to_html(),
        )


if __name__ == "__main__":
    unittest.main()
