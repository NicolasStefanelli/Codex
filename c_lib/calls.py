"""
    Author:Jarvis Lu
    Date: 3/2/2020

    This file contains the Calls class. The Calls class can be used to initiate
a call to a function within a file(e.g. printf(); or htons(); etc)

"""
from .import variable

""" 
    Initialization of the Calls class

    @instance variable_list a dictionary containing all the variables that this function
    TODO implement self checking for parameter type
    TODO might need to differentiate between calls to user defined function and standard functions
    @instance name name of the call(e.g. for printf() the name would be jus printf)
"""
class Calls(object):
    def __init__(self):
        self.variable_list = []
        self.name = None

    """ 
        handles the command passed in by the file. All subclass have a function
    name handle command so we can call this function without a clear idea of what 
    the subclass is

        @param action when function calls this class the parameter was called
            name, will change in the future
        @param value the value that the user wish to assign to the variable
    """  
    def handle_command(self, name, value):
        if name == "add":
            self.variable_list.append(str(value))
        elif name == "delete":
            self.variable_list.remove(value)

    """ 
        Generate the output base on the content within this variable. All subclass have a function
    name generate_output so we can call this function without a clear idea of what 
    the subclass is 
    
        @param output the output of the file passed in for this class to 
            add content
        @param indent_level how much this variable would need to be indented
    """ 
    def generate_output(self, output, indent_level):
        temp_out = ""
        iterator = 0
        while(iterator < indent_level):
            temp_out += "\t"
            iterator += 1
        temp_out = temp_out + self.name + "("
        if self.variable_list:
            for token in self.variable_list:
                temp_out = temp_out + token + ","
            temp_out = temp_out[:-1]
        temp_out += ");"
        output.append(temp_out)
        
    
    """ 
        Returns how many lines this class is taking up, which for function calls
            are always going to be one
    """
    def return_num_lines(self):
        return 1