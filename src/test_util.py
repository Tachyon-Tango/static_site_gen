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

    def test_split_images_1(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_2(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )

    def test_split_images_3(self):
        node = TextNode(
            "This is text with no image.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with no image.", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_images_4(self):
        node = TextNode(
            "This is text with an ![](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_5(self):
        node = TextNode(
            "This is code with no image.",
            TextType.CODE,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is code with no image.", TextType.CODE)
            ],
            new_nodes,
        )

    def test_split_links_1(self):
        node = TextNode(
             "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_split_links_2(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")
            ],
            new_nodes,
        )

    def test_split_links_3(self):
        node = TextNode(
             "This is text with no link.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with no link.", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_links_4(self):
        node = TextNode(
             "This is text with a link [](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_split_links_5(self):
        node = TextNode(
             "This is code with no link.",
            TextType.CODE,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is code with no link.", TextType.CODE)
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = "This is **bold text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()