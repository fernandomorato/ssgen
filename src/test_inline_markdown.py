import unittest

from inline_markdown import split_words_delimiter
from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    
    def test_bold(self):
        nodes = [TextNode("Text in **bold**", TextType.NORMAL)]
        new_nodes = split_words_delimiter(nodes, "**", TextType.BOLD)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("Text in ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
           ]
        )

    def test_italic(self):
        nodes = [TextNode("_Italic_ text", TextType.NORMAL)]
        new_nodes = split_words_delimiter(nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("Italic", TextType.ITALIC),
                TextNode(" text", TextType.NORMAL),
            ]
        )

    def test_code(self):
        nodes = [TextNode("This is a `java code` and a `python code` and a `go code` for nothing", TextType.NORMAL)]
        new_nodes = split_words_delimiter(nodes, "`", TextType.CODE)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is a ", TextType.NORMAL),
                TextNode("java code", TextType.CODE),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("python code", TextType.CODE),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("go code", TextType.CODE),
                TextNode(" for nothing", TextType.NORMAL),
           ]
        )

    def test_multiple_inlines(self):
        node = TextNode("This text has **bolded words**, _also italic_ and `some code`", TextType.NORMAL)
        new_nodes = split_words_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_words_delimiter(new_nodes, "_", TextType.ITALIC)
        new_nodes = split_words_delimiter(new_nodes, "`", TextType.CODE)

        self.assertListEqual(
            new_nodes,
            [
                TextNode("This text has ", TextType.NORMAL),
                TextNode("bolded words", TextType.BOLD),
                TextNode(", ", TextType.NORMAL),
                TextNode("also italic", TextType.ITALIC),
                TextNode(" and ", TextType.NORMAL),
                TextNode("some code", TextType.CODE),
            ])
