import unittest

from textnode import *
from htmlnode import *
from util import *

class TestUtil(unittest.TestCase):
    def test_eq_1(self):
        node_array_test = [TextNode("This is a `code` block.", TextType.TEXT)]
        node_array_expected = [TextNode("This is a ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" block.", TextType.TEXT)]
        node_array_function = split_nodes_delimiter(node_array_test, "`", TextType.CODE)
        self.assertEqual(str(node_array_expected), str(node_array_function))

    def test_eq_2(self):
        node_array_test = [TextNode("This is a text block.", TextType.TEXT)]
        node_array_expected = [TextNode("This is a text block.", TextType.TEXT)]
        node_array_function = split_nodes_delimiter(node_array_test, "`", TextType.CODE)
        self.assertEqual(str(node_array_expected), str(node_array_function))

    def test_eq_3(self):
        node_array_test = [TextNode("This is a `code`` block.", TextType.TEXT)]
        node_array_expected = [TextNode("This is a ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode("` block.", TextType.TEXT)]
        node_array_function = split_nodes_delimiter(node_array_test, "`", TextType.CODE)
        self.assertEqual(str(node_array_expected), str(node_array_function))

    def test_eq_4(self):
        node_array_test = [TextNode("This is a **bold** block.", TextType.TEXT)]
        node_array_expected = [TextNode("This is a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" block.", TextType.TEXT)]
        node_array_function = split_nodes_delimiter(node_array_test, "**", TextType.BOLD)
        self.assertEqual(str(node_array_expected), str(node_array_function))

    def test_eq_5(self):
        node_array_test = [TextNode("This is a _italic_ block.", TextType.TEXT)]
        node_array_expected = [TextNode("This is a ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" block.", TextType.TEXT)]
        node_array_function = split_nodes_delimiter(node_array_test, "_", TextType.ITALIC)
        self.assertEqual(str(node_array_expected), str(node_array_function))


if __name__ == "__main__":
    unittest.main()