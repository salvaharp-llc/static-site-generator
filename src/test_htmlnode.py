import unittest
from htmlnode import HTMLNode

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
        

if __name__ == "__main__":
    unittest.main()