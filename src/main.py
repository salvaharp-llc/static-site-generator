import os
import shutil
from copystatic import copy_contents

static_path = "./static"
public_path = "./public"

def main():
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    copy_contents(static_path, public_path)



main()