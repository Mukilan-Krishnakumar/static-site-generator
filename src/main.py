import os
from os.path import isdir, isfile
import re
import shutil
import pathlib
from markdown_to_html import markdown_to_html_node

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
    with open(from_path, "r") as file:
        from_text = file.read()
    with open(template_path, "r") as file:
        template_text = file.read()
    if from_path.startswith("content/"):
        split_list = from_path.split("/")[1:]
        print("Split List", split_list)
        filename = split_list[-1]
        if len(split_list) > 1:
            dest_path = "/".join([PUBLIC_PATH] + split_list[:-1])
            print("Dest path", dest_path)
            if os.path.isdir(dest_path) == False:
                print("True")
                os.makedirs(dest_path)
        # filename = filename.split("/")[-1].split(".")[0]
        # print("This is the filename", filename)
        print("Destination is the path", dest_path)
        filename = filename.split(".")[0] + ".html"
        print("This the filename", filename)
        dest_file = f"{dest_path}/{filename}"
        print("Destination path", dest_file)
        title = extract_title(from_text)
        template_text = template_text.replace("{{ Title }}", title)
        converted_html = markdown_to_html_node(from_text)
        template_text = template_text.replace("{{ Content }}", converted_html.to_html())
        with open(dest_file, "w") as dest_file:
            dest_file.write(template_text)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.isdir(dir_path_content) == True:
        print("File path", dir_path_content)
        for elem in os.listdir(dir_path_content):
            generate_pages_recursive(
                f"{dir_path_content}/{elem}", template_path, dest_dir_path
            )
    elif os.path.isfile(dir_path_content):
        print("File at", dir_path_content)
        copy_path = os.path.join(
            PUBLIC_PATH, "/".join(dir_path_content.split("/")[1:-1])
        )
        print("This is the destination", copy_path)
        generate_page_function(dir_path_content, template_path, dest_dir_path)


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
    # copy_static()
    from_dir = "content"
    template_path = "template.html"
    dest_dir = "public"
    generate_pages_recursive(from_dir, template_path, dest_dir)


main()
