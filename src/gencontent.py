import os

from pathlib import Path

from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode,
)

from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.splitlines()

    for line in lines:
        head = "# "
        if line.startswith(head):
            return line[len(head):].strip()
        
    raise Exception("markdown must have a title")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as file:
        markdown = file.read()

    with open(template_path) as file:
        template = file.read()

    html_content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    html_page = template.replace("{{ Title }}", title)
    html_page = html_page.replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(html_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path) == True:
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
