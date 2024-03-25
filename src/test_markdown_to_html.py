import unittest
from markdown_to_html import (
    convert_to_paragraph,
    convert_to_quote,
    convert_to_heading,
    convert_to_code,
    convert_to_unordered_list,
    convert_to_ordered_list,
    markdown_to_html_node,
)
from htmlnode import HTMLNode, ParentNode, LeafNode
from main import extract_title


class TestMarkdownToHtml(unittest.TestCase):
    def test_paragraph_conversion(self):
        block = "This is a paragraph block\nwith multiple lines"
        converted_paragraphs = convert_to_paragraph(block)
        check_paragraphs = LeafNode(
            "p", "This is a paragraph block with multiple lines"
        )
        self.assertEqual(converted_paragraphs.to_html(), check_paragraphs.to_html())

    def test_quote_conversion(self):
        blocks = "> This is one quote\n> This is another quote"
        converted_quotes = convert_to_quote(blocks)
        check_quotes = LeafNode(
            "blockquote", "This is one quote\nThis is another quote"
        )
        self.assertEqual(converted_quotes.to_html(), check_quotes.to_html())

    def test_heading_conversion(self):
        blocks = "# Heading 1\n## Heading 2\n### Heading 3\n####### Heading 7"
        converted_headings = convert_to_heading(blocks)
        converted_text = ""
        for child in converted_headings:
            converted_text += child.to_html() + "\n"
        converted_text = converted_text[:-1]
        check_headings = "<h1>Heading 1</h1>\n<h2>Heading 2</h2>\n<h3>Heading 3</h3>\n<p>####### Heading 7</p>"
        self.assertEqual(converted_text, check_headings)

    def test_code_conversion(self):
        blocks = "```This is a code block\nacross multiple lines```"
        converted_code = convert_to_code(blocks)
        check_code = ParentNode(
            "pre", [LeafNode("code", "This is a code block\nacross multiple lines")]
        )
        self.assertEqual(converted_code.to_html(), check_code.to_html())

    def test_unordered_list_conversion(self):
        blocks = "- L1\n- L2\n- L3"
        converted_unordered_list = convert_to_unordered_list(blocks)
        check_unordered_list = ParentNode(
            "ul", [LeafNode("li", "L1"), LeafNode("li", "L2"), LeafNode("li", "L3")]
        )
        self.assertEqual(
            converted_unordered_list.to_html(), check_unordered_list.to_html()
        )

    def test_ordered_list_conversion(self):
        blocks = "1. Testing\n2. Another Test"
        converted_ordered_list = convert_to_ordered_list(blocks)
        check_ordered_list = ParentNode(
            "ol", [LeafNode("li", "Testing"), LeafNode("li", "Another Test")]
        )
        self.assertEqual(converted_ordered_list.to_html(), check_ordered_list.to_html())

    def test_markdown_to_html_node(self):
        mkdwn = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items

```
Creating
coding masterpiece
```

Why not"""
        converted_mkdwn = markdown_to_html_node(mkdwn)
        check_mkdwn = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode(value="This is "),
                        LeafNode("b", "bolded"),
                        LeafNode(value=" paragraph"),
                    ],
                ),
                ParentNode(
                    "p",
                    [
                        LeafNode(value="This is another paragraph with "),
                        LeafNode("i", "italic"),
                        LeafNode(value=" text and "),
                        LeafNode("code", "code"),
                        LeafNode(
                            value=" here This is the same paragraph on a new line"
                        ),
                    ],
                ),
                ParentNode(
                    "ul",
                    [LeafNode("li", "This is a list"), LeafNode("li", "with items")],
                ),
                ParentNode(
                    "pre",
                    [
                        ParentNode(
                            "code", [LeafNode(value="\nCreating\ncoding masterpiece")]
                        )
                    ],
                ),
                ParentNode("p", [LeafNode(value="Why not")]),
            ],
        )
        self.assertEqual(check_mkdwn.to_html(), converted_mkdwn.to_html())

    def test_extract_title(self):
        mkdwn = """
# This is the title

- Hello, hello"""
        self.assertEqual(extract_title(mkdwn), "This is the title")

    def test_extract_title_exception(self):
        mkdwn = """
### Not a title

- Hihi
        """
        self.assertRaises(Exception, extract_title, mkdwn)
