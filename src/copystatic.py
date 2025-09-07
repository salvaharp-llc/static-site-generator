import os
import shutil

def copy_contents(source, destination):
    if not os.path.exists(source):
        raise Exception("Error: Source directory does not exist")
    if os.path.isfile(source):
        raise Exception("Error: Source is a file, not a directory")
    
    if not os.path.exists(destination):
        os.mkdir(destination)
    
    for item in os.listdir(source):
        item_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)
        print(f" * {item_path} -> {destination_path}")
        if os.path.isfile(item_path):
            shutil.copy(item_path, destination)
        else:
            copy_contents(item_path, destination_path)