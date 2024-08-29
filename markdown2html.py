#!/usr/bin/env python3
"""
markdown2html.py: Converts a Markdown file to an HTML file.
"""

import sys
import re

def parse_markdown(markdown_file):
    html_lines = []
    with open(markdown_file, 'r') as file:
        lines = file.readlines()

    in_paragraph = False
    paragraph_lines = []

    for line in lines:
        line = line.rstrip()  # Remove trailing whitespace
        
        if re.match(r'^# ', line):  # Heading level 1
            html_lines.append(f"<h1>{line[2:]}</h1>")
        elif re.match(r'^\- ', line):  # Unordered list item
            if not html_lines or not html_lines[-1].startswith('<ul>'):
                html_lines.append("<ul>")
            html_lines.append(f"<li>{line[2:]}</li>")
        elif line.strip() == "":  # Empty line
            if in_paragraph:
                if paragraph_lines:
                    html_lines.append("<p>")
                    html_lines.append("<br/>".join(paragraph_lines))
                    html_lines.append("</p>")
                in_paragraph = False
                paragraph_lines = []
            elif html_lines and html_lines[-1] == "</ul>":
                html_lines.pop()  # Remove the extra closing tag
                html_lines.append("</ul>")
        else:
            if not in_paragraph:
                in_paragraph = True
            paragraph_lines.append(line)

    # If any paragraph is still open, close it
    if in_paragraph and paragraph_lines:
        html_lines.append("<p>")
        html_lines.append("<br/>".join(paragraph_lines))
        html_lines.append("</p>")

    return html_lines

def convert_markdown_to_html(markdown_file, output_file):
    html_lines = parse_markdown(markdown_file)
    with open(output_file, 'w') as file:
        for line in html_lines:
            file.write(line + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        convert_markdown_to_html(markdown_file, output_file)
    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        sys.exit(1)

