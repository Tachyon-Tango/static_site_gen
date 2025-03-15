import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    #HTMLNode Tests
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
    


    #LeafNode Tests
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Click me!")
        self.assertEqual(node.to_html(), '<b>Click me!</b>')

    #ParentNode Tests
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child")
        child_node2 = LeafNode("span", "child")
        child_node3 = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node1, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><span>child</span><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_grandchildren(self):
        grandchild_node1 = LeafNode("b", "grandchild1")
        grandchild_node2 = LeafNode("b", "grandchild2")
        grandchild_node3 = LeafNode("b", "grandchild3")
        child_node1 = ParentNode("span", [grandchild_node1, grandchild_node2, grandchild_node3])
        child_node2 = ParentNode("span", [grandchild_node1, grandchild_node2, grandchild_node3])
        child_node3 = ParentNode("span", [grandchild_node1, grandchild_node2, grandchild_node3])
        parent_node = ParentNode("div", [child_node1, child_node2, child_node3])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild1</b><b>grandchild2</b><b>grandchild3</b></span><span><b>grandchild1</b><b>grandchild2</b><b>grandchild3</b></span><span><b>grandchild1</b><b>grandchild2</b><b>grandchild3</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()