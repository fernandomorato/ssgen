import unittest
from textnode import TextNode, TextType


def split_words_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        split_nodes = []
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError(f"invalid markdown, inline delimiter not closed")
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            split_nodes.append(TextNode(split_text[i], TextType.NORMAL if i % 2 == 0 else text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

if __name__ == "__main__":
    unittest.main()
