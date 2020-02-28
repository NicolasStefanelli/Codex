"""
    Author:Jarvis Lu
    Date: 2/27/2020

    This file is just used to open vs code quickly, most likely will not 
receive further support

"""
import os

def open_vscode(path):
    os.system("code " + path)

def create_new_file(path, file_name):
    os.system("touch " + path + " " + file_name)