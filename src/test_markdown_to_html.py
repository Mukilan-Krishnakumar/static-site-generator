import unittest
from markdown_to_html import (
    convert_to_paragraph,
    convert_to_quote,
    convert_to_heading,
    convert_to_code,
    convert_to_unordered_list,
    convert_to_ordered_list,
)


class TestMarkdownToHtml(unittest.TestCase):
    def test_paragraph_conversion(self):
        blocks = ["This is a paragraph block", "with multiple lines"]
        converted_paragraphs = convert_to_paragraph(blocks)
        check_paragraphs = "<p>\nThis is a paragraph block\nwith multiple lines\n</p>"
        self.assertEqual(converted_paragraphs, check_paragraphs)

    def test_quote_conversion(self):
        blocks = ["> This is one quote", "> This is another quote"]
        converted_quotes = convert_to_quote(blocks)
        check_quotes = (
            "<blockquote>\nThis is one quote\nThis is another quote\n</blockquote>"
        )
        self.assertEqual(converted_quotes, check_quotes)

    def test_heading_conversion(self):
        blocks = ["# Heading 1", "## Heading 2", "### Heading 3", "####### Heading 7"]
        converted_headings = convert_to_heading(blocks)
        check_headings = "<h1>Heading 1</h1>\n<h2>Heading 2</h2>\n<h3>Heading 3</h3>\n<p>####### Heading 7</p>\n"
        self.assertEqual(converted_headings, check_headings)

    def test_code_conversion(self):
        blocks = ["```This is a code block", "across multiple lines```"]
        converted_code = convert_to_code(blocks)
        check_code = "<pre>\n<code>\nThis is a code block\nacross multiple lines\n</code>\n</pre>"
        self.assertEqual(converted_code, check_code)

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
