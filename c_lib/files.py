"""
    Author:Jarvis Lu
    Date: 2/27/2020

    This file contains the File class. The majority of editing of a file's
content happens within the file class

"""
from .import include
from .import function
from .import variable
from file_io import writer

""" 
    Initialization of the File class

    @param file_path path to the file that this writer class is going to write to 
    @instance function_dict a dictionary to keep all functions so a specifc func can be 
        returned given a func name
    @instance current_function the last func the user was editing, so the user can edit the 
        same func without the need to specify it again
    @instance writer the writer class this file class uses to modify the actual file
    @instance include the include class that will host all the different includes needed 
        by this file
    @instance output the content of this file. Changes will be made to the self.output list
        then it would be passed to writer to write to file
    @instance tracker keeps track of everything within the file. Whenever a new object is created
        it is placed in the tracker depending on its position in the file. When the output is 
        being generated, output will be generated sequencially from the first item in tracker 
        to the last 
"""
class File(object):
    def __init__(self, file_path):
        self.function_dict = {}
        self.current_function = None
        self.writer = writer.Writer(file_path)
        self.include = include.Include()   
        self.output = []
        self.tracker = []
        
    """ 
        Writes the content of self.output to the file

        TODO when the file had error output at the very end, it is possible
    for the writer to miss the end, might need to clear the whole file before 
    writing again
    """  
    def write_output(self):
        self.writer.write(self.output)

    """ 
        Adds include to output

        TODO include doesn't work if another include is added later on during
    the editing process. 
        @param file_path the path to the file to be opened
    """
    def add_std_include(self, include):
        self.include.add_std_include(include, self.output, 0)
        if self.include not in self.tracker:
            print('added include')
            self.tracker.append(self.include)
        
    def add_function(self, func_name, return_type, func_type):
        new_func = function.Func(func_name, return_type)
        self.function_dict.update({new_func.func_name:new_func})
        if(func_type == "definition"):
            new_func.return_func_definition(self.output, self.return_write_line())
        elif(func_type == "declaration"):
            new_func.return_func_declaration(self.output, self.return_write_line())
        self.tracker.append(new_func)
        self.current_function = new_func

    def add_to_function_body(self, action_type, name= None, line= None, value= None, func_name= None):
        if func_name != None:
            self.current_function = self.function_dict.get(func_name)
        elif line != None:
            line = line - self.return_write_line(self.current_function)
        original_body_length = self.current_function.return_num_lines()
        self.current_function.add_to_function_body(action_type, name, line, value)
        self.current_function.return_modified_func(self.output, self.return_write_line(self.current_function), original_body_length)
        self.write_output()
        
    def return_write_line(self, element= None):
        if self.tracker:
                ret = 0
                for token in self.tracker:
                    if(element == token):
                        return ret
                    ret += token.return_num_lines() +1
                return ret
        else:
            return 1
    