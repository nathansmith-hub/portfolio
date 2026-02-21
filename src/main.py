import os

from copystatic import copy_static

from gencontent import generate_page
               
def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static = os.path.join(repo_root, "static")
    public = os.path.join(repo_root, "public")

    copy_static(static, public)

    source_index = os.path.join(repo_root, "content", "index.md")
    template = os.path.join(repo_root, "template.html")
    dest_index = os.path.join(repo_root, "public", "index.html")

    generate_page(source_index, template, dest_index)

if __name__ == "__main__":
    main()
