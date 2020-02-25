import os

def open_vscode(path):
    os.system("code " + path)

def create_new_file(path, file_name):
    os.system("touch " + path + " " + file_name)