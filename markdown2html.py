#!/usr/bin/python3
"""
Markdown to HTML converter script
"""

import sys
import os
import re

def convert_markdown_to_html(markdown_file, html_file):
    """
    Converts a Markdown file to an HTML file by parsing headings and unordered lists.
    """
    with open(markdown_file, 'r') as md_file:
        with open(html_file, 'w') as html_file:
            in_list = False
            for line in md_file:
                # Check for heading levels
                match_heading = re.match(r'^(#{1,6}) (.*)', line)
                if match_heading:
                    heading_level = len(match_heading.group(1))
                    heading_text = match_heading.group(2)
                    if in_list:
                        html_file.write("</ul>\n")
                        in_list = False
                    html_file.write(f"<h{heading_level}>{heading_text}</h{heading_level}>\n")
                    continue

                # Check for unordered list items
                match_list = re.match(r'^- (.*)', line)
                if match_list:
                    list_item = match_list.group(1)
                    if not in_list:
                        html_file.write("<ul>\n")
                        in_list = True
                    html_file.write(f"    <li>{list_item}</li>\n")
                else:
                    if in_list:
                        html_file.write("</ul>\n")
                        in_list = False

            if in_list:
                html_file.write("</ul>\n")

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

