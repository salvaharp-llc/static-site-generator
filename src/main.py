import os
import shutil
from copystatic import copy_contents
from generatepage import generate_page

static_path = "./static"
public_path = "./public"
content_path = "./content"
template_path = "./template.html"
public_path = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    print("Copying static files to public directory...")
    copy_contents(static_path, public_path)

    print("Generating page...")
    generate_page(
        os.path.join(content_path, "index.md"), 
        template_path, 
        os.path.join(public_path, "index.html")
        )


main()