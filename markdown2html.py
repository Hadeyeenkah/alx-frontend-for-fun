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
    ordered lists, and paragraphs.
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
                        html_file.write("<p>\n" + paragraph_text + "\n</p>\n")
                        paragraph_lines = []
                    heading_level = len(match_heading.group(1))
                    heading_text = match_heading.group(2)
                    html_file.write(f"<h{heading_level}>{heading_text}</h{heading_level}>\n")
                    continue

                # Check for unordered list items
                match_unordered_list = re.match(r'^- (.*)', line)
                if match_unordered_list:
                    if paragraph_lines:
                        paragraph_text = ''.join(paragraph_lines).replace('\n', '<br />\n')
                        html_file.write("<p>\n" + paragraph_text + "\n</p>\n")
                        paragraph_lines = []
                    if not in_list or list_type != 'ul':
                        if in_list:
                            html_file.write(f"</{list_type}>\n")
                        html_file.write("<ul>\n")
                        in_list = True
                        list_type = 'ul'
                    html_file.write(f"    <li>{match_unordered_list.group(1)}</li>\n")
                    continue

                # Check for ordered list items
                match_ordered_list = re.match(r'^\* (.*)', line)
                if match_ordered_list:
                    if paragraph
