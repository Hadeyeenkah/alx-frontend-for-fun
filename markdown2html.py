#!/usr/bin/env python3
"""
markdown2html.py - A simple markdown to HTML converter.
"""

import sys
import re

def markdown_to_html(markdown_text):
    html_output = []
    in_paragraph = False

    for line in markdown_text.splitlines():
        stripped_line = line.strip()

        if stripped_line == "":
            if in_paragraph:
                html_output.append("</p>")
                in_paragraph = False
            continue

        if not in_paragraph:
            html_output.append("<p>")
            in_paragraph = True

        # Add <br/> for lines within the same paragraph
        if len(html_output) > 0 and html_output[-1].endswith("</p>") is False and html_output[-1] != "<p>":
            html_output[-1] += "<br/>"

        html_output.append(stripped_line)

    if in_paragraph:
        html_output.append("</p>")

    return "\n".join(html_output)

def main():
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <markdown file> <html file>")
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    try:
        with open(markdown_file, 'r') as md_file:
            markdown_text = md_file.read()

        html_content = markdown_to_html(markdown_text)

        with open(html_file, 'w') as html_file:
            html_file.write(html_content)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
