import os
import sys
import shutil

from copystatic import copy_static

from gencontent import generate_pages_recursive
               
def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static = os.path.join(repo_root, "static")
    docs = os.path.join(repo_root, "docs")

    if os.path.exists(docs):
        shutil.rmtree(docs)

    copy_static(static, docs)

    source_index = os.path.join(repo_root, "content")
    template = os.path.join(repo_root, "template.html")

    generate_pages_recursive(source_index, template, docs, basepath)

if __name__ == "__main__":
    main()
