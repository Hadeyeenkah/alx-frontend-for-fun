#!/usr/bin/python3
"""
Markdown to HTML converter script
"""

import sys
import os
import re

def convert_markdown_to_html(markdown_file, html_file):
    """
    Converts a Markdown file to an HTML file by parsing headings.
    """
    with open(markdown_file, 'r') as md_file:
        with open(html_file, 'w') as html_file:
            for line in md_file:
                # Check for heading levels
                match = re.match(r'^(#{1,6}) (.*)', line)
                if match:
                    heading_level = len(match.group(1))
                    heading_text = match.group(2)
                    html_file.write(f"<h{heading_level}>{heading_text}</h{heading_level}>\n")

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

