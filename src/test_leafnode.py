import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_value(self):
        leaf = LeafNode(tag="p", value="yo!")
        self.assertEqual(
            leaf.tag,
            "p",
        )
        self.assertEqual(
            leaf.value,
            "yo!",
        )
        self.assertEqual(
            leaf.children,
            None,
        )
        self.assertEqual(
            leaf.props,
            None,
        )

    def test_repr(self):
        leaf = LeafNode(tag="a", value="duvido clicar", props={"href": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"})

        self.assertEqual(
            repr(leaf),
            "LeafNode(a, duvido clicar, {'href': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'})",
        )

    def test_to_html(self):
        node = LeafNode("p", "txa boba jr")
        node_with_props = LeafNode("a", "Xalala 123", {"href": "https://www.google.com"})

        self.assertEqual(
            node.to_html(),
            "<p>txa boba jr</p>",
        )
        self.assertEqual(
            node_with_props.to_html(),
            '<a href="https://www.google.com">Xalala 123</a>',
        )

