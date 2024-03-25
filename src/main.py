import os
import re
import shutil

STATIC_PATH = "./static"
PUBLIC_PATH = "./public"


def extract_title(markdown):
    lines = markdown.splitlines()
    for text in lines:
        if re.match(r"(?<!#)# {1}", text):
            return text[2:]
    raise Exception("No Title given")


def generate_page_function(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")


def recursive_copy(path):
    if os.path.isdir(path):
        if path != STATIC_PATH:
            directory_path = "/".join(path.split("/")[2:])
            os.mkdir(os.path.join(PUBLIC_PATH, directory_path))
        for elem in os.listdir(path):
            recursive_copy(os.path.join(path, elem))
    elif os.path.isfile(path):
        copy_path = os.path.join(PUBLIC_PATH, "/".join(path.split("/")[2:]))
        print(f"Copying file from {path} to {copy_path}")
        shutil.copy(path, copy_path)


def copy_static():
    if os.path.exists(STATIC_PATH):
        shutil.rmtree(PUBLIC_PATH)
        os.mkdir(PUBLIC_PATH)
        recursive_copy(STATIC_PATH)


def main():
    copy_static()


main()
