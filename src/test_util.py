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

    def test_extract_markdown_images_1(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_2(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)

    def test_extract_markdown_images_3(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)

    def test_extract_markdown_links_1(self):
        matches = extract_markdown_links(
          "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_extract_markdown_links_2(self):
        matches = extract_markdown_links(
          "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_links_3(self):
        matches = extract_markdown_links(
          "This is text with a link [to boot dev](https://www.boot.dev) and [](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("", "https://www.youtube.com/@bootdotdev")], matches)


if __name__ == "__main__":
    unittest.main()