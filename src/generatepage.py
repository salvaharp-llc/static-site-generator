from block_markdown import markdown_to_blocks, markdown_to_html_node
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        md = f.read()
    with open(template_path, "r") as f:
        template = f.read()  
    html_content = markdown_to_html_node(md).to_html()
    title = extract_title(md)

    html_page = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(html_page)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block[2:]
    raise Exception("Error: no title found")
    