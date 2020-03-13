"""
    Author:Jarvis Lu
    Date: 2/27/2020

    This file contains the Project class. Project class is used mainly 
keeping track of files and current working directory of the project

"""
from .import navigation
from c_lib import files
import pyautogui
import os
from os.path import expanduser
from open_app import open_apps

""" 
    For compatability across platforms, this set allows for specific command
set to be selected for the specific platform
"""
Unix_command = {"directory":"mkdir ", "file":"touch ", "slash":"/"}
windows_prompt = {"directory":"md ", "file":"type null > ", "slash":"\\"}
command_set = {"Darwin": Unix_command, "Windows":windows_prompt}

""" 
    Initialization of the Project class
    TODO Update current directory to accurately reflect the directory that
the user is actually in

    @param path the current work path of this project
    @param platform the platform of the device
    @instance work_path the current work path of this project
    @instance current_directory the directory the user is currently under
    @instance num_file the number of file within this project
    @instance current_file The last file the user was editing 
    @instance file_dict stores all the file and their file names for easy access
    @instance command the set of command that the program would use base on platform
"""
class Project(object):
    def __init__(self, path, platform):
        self.work_path = None
        self.current_directory = None
        self.num_file = 0
        self.current_file = None
        self.file_dict = {}
        self.command = command_set.get(platform)
        self.get_work_path(path)

        #creates the project directory
        os.system(self.command.get("directory") + self.work_path)
        #open the directory with vs code
        open_apps.open_vscode(self.work_path)

    """ 
        This function can be used to generate the correct path based on the 
    the plaform and checks whether Onedrive backup is set up. Can add additional
    cases to check for in the future in this function
        @param path The path passed in from the user. Passed in as a list of the name
            of the directories to change into.
    """
    def get_work_path(self, path):
        work_path = expanduser("~")
        if os.path.exists(work_path + self.command.get("slash") + "Onedrive") and path.count("disable") == 0:
            work_path = work_path + self.command.get("slash") + "Onedrive"
        for item in path:
            work_path = work_path + self.command.get("slash") + item
        self.work_path = work_path
        self.current_directory = work_path

    """ 
        Open a specific file using pyautogui, might delete
        @param filename name of the file to be opened
    """
    def open_file(self, filename):
        navigation.command_list(["down command", "p"])
        navigation.write(filename)

    """ 
        Changes the working directory
        @param directory the directory to change into
        TODO edge case ..
    """
    def change_directory(self, directory):
        os.system("cd " + directory)
        self.current_directory = self.current_directory + self.command.get("slash") + directory
    
    """ 
        Returns to the home directory of the project
    """
    def return_to_home_directory(self):
        os.system("cd " + self.work_path)
        self.current_directory = self.work_path

    """ 
        Create a new file and a new file object to be stored within Project
        @param filename name of the file to be created
    """
    def create_new_file(self, filename):
        self.num_file += 1
        os.system(self.command.get("file") + self.current_directory + self.command.get("slash") + filename)
        new_file = files.File(self.current_directory + self.command.get("slash") + filename)
        self.file_dict.update({filename:new_file})
        self.current_file = new_file

    """ 
        Remove a given file
        @param filename name of the file to be removed
    """
    def remove_file(self, filename):
        command = "rm " + self.current_directory + self.command.get("slash") + filename
        os.system(command)
        del self.file_dict[filename]

    """ 
        Adds an existing file to the project files dictionary
        @param filename name of the file to be added
    """
    def add_file(self, filename):
        self.num_file += 1
        new_file = files.File(filename, self.current_directory)
        self.file_dict.update({filename:new_file})

    """ 
        Returns a given file object or the last file object the user edited
        @param filename the name of the file to be returned
    """
    def return_file(self, filename = None):
        if filename == None:
            return self.current_file
        else:
            return self.file_dict.get(filename)
    