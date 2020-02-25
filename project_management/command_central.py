from .import proj_manage
from file_io import writer
from c_lib import files
import time

class CommandCentral(object):
    def __init__(self):
        self.project = None
        self.language = None
        self.last_command = None

    def create_new_project(self, work_space_path):
        self.project = proj_manage.Project(work_space_path)
        time.sleep(1)

    def add_file(self, filename):
        self.project.create_new_file(filename)
        self.project.open_file(filename)
        self.current_file = self.project.return_file(filename)
    
    def clear_file(self):
        self.current_file.clear()        

    def remove_file(self, filename):
        self.project.remove_file(filename)
    
    def add_include(self, include_name):
        self.current_file.add_std_include(include_name)
        self.current_file.write_output()

    def add_func(self, func_name, return_type, func_type):
        self.current_file.add_function(func_name, return_type, func_type)
        self.current_file.write_output()
    
    def add_to_func_body(self, action_type, name= None, line= None, value= None, func_name= None):
        self.current_file.add_to_function_body(action_type, name, line, value, func_name)
        
    def modify_current_action(self, command, line= None):
        self.current_file.modify_current_action(command, line)