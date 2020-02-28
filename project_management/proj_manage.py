from .import navigation
from c_lib import files
import pyautogui
import os
from open_app import open_apps

Unix_command = {"directory":"mkdir ", "file":"touch ", "slash":"/"}
windows_prompt = {"directory":"md ", "file":"type null > ", "slash":"\\"}
command_set = {"Darwin": Unix_command, "Windows":windows_prompt}

class Project(object):
    def __init__(self, path, platform):
        self.work_path = path
        self.current_directory = path
        self.num_file = 0
        self.cur_file = None
        self.file_dict = {}
        self.command = command_set.get(platform)
        
        os.system(self.command.get("directory") + self.work_path)
        open_apps.open_vscode(path)

    def open_file(self, filename):
        navigation.command_list(["down command", "p"])
        navigation.write(filename)

    def change_directory(self, directory):
        os.system("cd " + directory)
        self.current_directory = self.current_directory + self.command.get("slash") + directory
    
    def return_to_home_directory(self):
        os.system("cd " + self.work_path)
        self.current_directory = self.work_path

    def create_new_file(self, filename):
        self.num_file += 1
        os.system(self.command.get("file") + self.current_directory + self.command.get("slash") + filename)
        new_file_path = self.current_directory + self.command.get("slash") + filename
        new_file = files.File(filename, new_file_path)
        self.file_dict.update({filename:new_file})

    def remove_file(self, filename):
        command = "rm " + self.current_directory + self.command.get("slash") + filename
        os.system(command)
        del self.file_dict[filename]

    def add_file(self, filename):
        self.num_file += 1
        new_file = files.File(filename, self.current_directory)
        self.file_dict.update({filename:new_file})

    def return_file(self, filename = None):
        if filename == None:
            return self.cur_file
        else:
            return self.file_dict.get(filename)
    