import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

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
            "HTMLNode(a, link, children: None, {'href': 'https://www.google.com'})",
            repr(node),
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
        self.assertEqual(
            node.props, {"class": "greeting", "href": "https://incognia.com"}
        )

    def test_props_to_html(self):
        node = HTMLNode(tag="link", props={"rel": "stylesheet", "href": "styles.css"})
        self.assertEqual(
            ' rel="stylesheet" href="styles.css"',
            node.props_to_html(),
        )

    def test_leaf_value(self):
        tag = "p"
        value = "yo!"
        leaf = LeafNode(tag=tag, value=value)
        self.assertEqual(
            leaf.tag,
            tag,
        )
        self.assertEqual(
            leaf.value,
            value,
        )
        self.assertEqual(
            leaf.children,
            None,
        )
        self.assertEqual(
            leaf.props,
            None,
        )

    def test_leaf_repr_a(self):
        tag = "a"
        value = "duvido clicar"
        props = {"href": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
        leaf = LeafNode(tag=tag, value=value, props=props)

        self.assertEqual(
            repr(leaf),
            f"LeafNode({tag}, {value}, {props})",
        )

    def test_leaf_to_html(self):
        node = LeafNode("p", "txa boba jr")
        self.assertEqual(
            node.to_html(),
            "<p>txa boba jr</p>",
        )

        node_with_props = LeafNode(
            "a", "Xalala 123", {"href": "https://www.google.com"}
        )
        self.assertEqual(
            node_with_props.to_html(),
            '<a href="https://www.google.com">Xalala 123</a>',
        )

    # PARENT NODE
    def test_parent_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold"),
                LeafNode("i", "Italic"),
                LeafNode("sub", "Subscript"),
                LeafNode(None, "Normal"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold</b><i>Italic</i><sub>Subscript</sub>Normal</p>",
        )

if __name__ == "__main__":
    unittest.main()
