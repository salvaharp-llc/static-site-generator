import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(), 
            ' href="https://www.google.com" target="_blank"'
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node1 = HTMLNode("a", "link1", None, {"target": "_blank"})
        node = HTMLNode("p", "This is a paragraph", [node1])
        self.assertEqual(
            repr(node), 
            "HTMLNode(p, This is a paragraph, children: [HTMLNode(a, link1, children: None, {'target': '_blank'})], None)"
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            node.to_html(), 
            '<a href="https://www.google.com" target="_blank">Hello, world!</a>',
        )
    
    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_to_html_with_children(self):
        parent_node = ParentNode(
            "div", 
            [
                LeafNode("span", "child1"), 
                LeafNode("span", "child2"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span>child1</span><span>child2</span>Normal text</div>",
        )

    def test_parent_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_to_html_with_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError): 
            parent_node.to_html()
        
    def test_parent_to_html_with_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError): 
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()