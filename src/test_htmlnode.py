import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq_1(self):
        node = HTMLNode("This is a tag,", "This is a value", "This is a child", {"prop": "the property value"})
        node2 = HTMLNode("This is a tag,", "This is a value", "This is a child", {"prop": "the property value"})
        self.assertEqual(str(node), str(node2))

    def test_eq_2(self):
        node = HTMLNode()
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(str(node), str(node2))

    def test_uneq_1(self):
        node = HTMLNode("This is a tag,", "This is a value", "This is a child")
        node2 = HTMLNode("This is a tag,", "This is a value", "This is a child", {"prop": "the property value"})
        self.assertNotEqual(node, node2)

    def test_uneq_2(self):
        node = HTMLNode("This is a tag,", "This is a value", None, {"prop": "the property value"})
        node2 = HTMLNode("This is a tag,", "This is a value", "This is a child", {"prop": "the property value"})
        self.assertNotEqual(str(node), str(node2))

    def test_uneq_3(self):
        node = HTMLNode("This is a tag,", None, "This is a child", {"prop": "the property value"})
        node2 = HTMLNode("This is a tag,", "This is a value", "This is a child", {"prop": "the property value"})
        self.assertNotEqual(str(node), str(node2))

    def test_uneq_4(self):
        node = HTMLNode(None, "This is a value", "This is a child", {"prop": "the property value"})
        node2 = HTMLNode("This is a tag,", "This is a value", "This is a child", {"prop": "the property value"})
        self.assertNotEqual(str(node), str(node2))

    def test_props_to_html(self):
        text = ' prop="the property value" prop2="the property value 2"'
        node = HTMLNode("This is a tag,", "This is a value", "This is a child", {"prop": "the property value", "prop2" : "the property value 2"})
        self.assertEqual(node.props_to_html(), text)

if __name__ == "__main__":
    unittest.main()