#!/usr/bin/python3
"""
Markdown to HTML converter script
"""

import sys
import os

def convert_markdown_to_html(markdown_file, html_file):
    # Function to convert markdown content to HTML
    # This is a placeholder and needs to be implemented
    pass

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]
    
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)
    
    # Convert markdown to HTML (to be implemented)
    convert_markdown_to_html(markdown_file, html_file)
    
    # Successful execution
    sys.exit(0)

