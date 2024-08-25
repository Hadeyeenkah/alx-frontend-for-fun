#!/usr/bin/python3
"""
Markdown to HTML converter script
"""

import sys
import os
import re

def convert_markdown_to_html(markdown_file, html_file):
    """
    Converts a Markdown file to an HTML file by parsing headings, unordered lists,
    ordered lists, paragraphs, and bold/emphasis text.
    """
    with open(markdown_file, 'r') as md_file:
        with open(html_file, 'w') as html_file:
            in_list = False
            list_type = None
            paragraph_lines = []

            for line in md_file:
                # Debug: Print the current line being processed
                print(f"Processing line: {line.strip()}")

                # Check for heading levels
                match_heading = re.match(r'^(#{1,6}) (.*)', line)
                if match_heading:
                    if in_list:
                        html_file.write(f"</{list_type}>\n")
                        in_list = False
                    if paragraph_lines:
                        paragraph_text = ''.join(paragraph_lines).replace('\n', '<br />\n')
                        html_file.write("<p>\n" + convert_text(paragraph_text) + "\n</p>\n")
                        paragraph_lines = []
                    heading_level = len(match_heading.group(1))
                    heading_text = match_heading.group(2)
                    html_file.write(f"<h{heading_level}>{convert_text(heading_text)}</h{heading_level}>\n")
                    continue

                # Check for unordered list items
                match_unordered_list = re.match(r'^- (.*)', line)
                if match_unordered_list:
                    if paragraph_lines:
                        paragraph_text = ''.join(paragraph_lines).replace('\n', '<br />\n')
                        html_file.write("<p>\n" + convert_text(paragraph_text) + "\n</p>\n")
                        paragraph_lines = []
                    if not in_list or list_type != 'ul':
                        if in_list:
                            html_file.write(f"</{list_type}>\n")
                        html_file.write("<ul>\n")
                        in_list = True
                        list_type = 'ul'
                    html_file.write(f"    <li>{convert_text(match_unordered_list.group(1))}</li>\n")
                    continue

                # Check for ordered list items
                match_ordered_list = re.match(r'^\* (.*)', line)
                if match_ordered_list:
                    if paragraph_lines:
                        paragraph_text = ''.join(paragraph_lines).replace('\n', '<br />\n')
                        html_file.write("<p>\n" + convert_text(paragraph_text) + "\n</p>\n")
                        paragraph_lines = []
                    if not in_list or list_type != 'ol':
                        if in_list:
                            html_file.write(f"</{list_type}>\n")
                        html_file.write("<ol>\n")
                        in_list = True
                        list_type = 'ol'
                    html_file.write(f"    <li>{convert_text(match_ordered_list.group(1))}</li>\n")
                    continue

                # Handle blank lines and paragraphs
                if line.strip() == "":
                    if paragraph_lines:
                        paragraph_text = ''.join(paragraph_lines).replace('\n', '<br />\n')
                        html_file.write("<p>\n" + convert_text(paragraph_text) + "\n</p>\n")
                        paragraph_lines = []
                    if in_list:
                        html_file.write(f"</{list_type}>\n")
                        in_list = False
                    continue

                # Collect paragraph lines
                paragraph_lines.append(line.rstrip())

            # Handle any remaining paragraph lines
            if paragraph_lines:
                paragraph_text = ''.join(paragraph_lines).replace('\n', '<br />\n')
                html_file.write("<p>\n" + convert_text(paragraph_text) + "\n</p>\n")

            # Close any open list
            if in_list:
                html_file.write(f"</{list_type}>\n")

def convert_text(text):
    """
    Converts Markdown syntax for bold and emphasis to HTML tags.
    """
    # Convert bold (**) to <b> tags
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    # Convert emphasis (__) to <em> tags
    text = re.sub(r'__(.*?)__', r'<em>\1</em>', text)
    return text

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]
    
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)
    
    # Convert markdown to HTML
    convert_markdown_to_html(markdown_file, html_file)
    
    # Successful execution
    sys.exit(0)

