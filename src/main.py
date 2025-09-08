import os
import shutil
from copystatic import copy_contents
from generatepage import generate_pages_recursive

static_path = "./static"
public_path = "./public"
content_path = "./content"
template_path = "./template.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    print("Copying static files to public directory...")
    copy_contents(static_path, public_path)

    print("Generating page...")
    generate_pages_recursive(content_path, template_path, public_path)


main()