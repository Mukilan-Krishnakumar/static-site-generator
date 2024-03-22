import unittest
from markdown_to_html import (
    convert_to_paragraph,
    convert_to_quote,
    convert_to_heading,
    convert_to_code,
    convert_to_unordered_list,
    convert_to_ordered_list,
)
from htmlnode import ParentNode
from leafnode import LeafNode


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
        blocks = ["- L1", "- L2", "- L3"]
        converted_unordered_list = convert_to_unordered_list(blocks)
        check_unordered_list = "<ul>\n<li>L1</li>\n<li>L2</li>\n<li>L3</li>\n</ul>"
        self.assertEqual(converted_unordered_list, check_unordered_list)

    def test_ordered_list_conversion(self):
        blocks = ["1. Testing", "2. Another Test"]
        converted_ordered_list = convert_to_ordered_list(blocks)
        check_ordered_list = "<ol>\n<li>Testing</li>\n<li>Another Test</li>\n</ol>"
        self.assertEqual(converted_ordered_list, check_ordered_list)
