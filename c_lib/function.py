"""
    Author:Jarvis Lu
    Date: 3/2/2020

    This file contains the Funtion class. The function class can be used write
functions to the file. Functions will contain sub classes such as if_else statements
or variables or includes etc

"""

from .import variable
from .import calls
from .import if_else

""" 
    Initialization of the Function class

    @param file_path path to the file that this writer class is going to write to 
    @instance function_dict a dictionary to keep all functions so a specifc func can be 
        returned given a func name
    @instance current_action the last sub-class the user was editing. This is implemented 
        so the user can edit the same func without the need to specify it again
    @instance argument_dict a dictionary containing all the arguments that will be
        passed into this function. The keys will be the name of the argument and the value
        would be the type of the argument(e.g. {example:int})
    @instance variable_dict a dictionary containing all the variables that this function
    @instance output the content of this file. Changes will be made to the self.output list
        then it would be passed to writer to write to file
    @instance tracker keeps track of everything within the file. Whenever a new object is created
        it is placed in the tracker depending on its position in the file. When the output is 
        being generated, output will be generated sequencially from the first item in tracker 
        to the last 
"""
class Function(object):
    def __init__(self, func_name, return_type):
        self.current_action = None
        self.argument_dict = {}
        self.variable_dict = {}
        self.call_list = {}
        self.return_type = return_type
        self.func_name = func_name
        self.output = []
        self.tracker =[]

    """ 
        Generate the output base on the content within this function class.  
        @return return the output generated
        TODO generate output to many different ways of returning, be consistant
        @return a buffer containing the output of the function with its body 
    """ 
    def generate_output(self):
        arguments = self.argument_dict.keys()
        output = self.return_type + " " + self.func_name + "("
        if arguments:
            for arg in arguments:
                output += self.argument_dict.get(arg) + " " + arg + ","     
            output = output[:-1]
        output += ")"
        indent_level = 1
        self.output.clear()
        for token in self.tracker:
            token.generate_output(self.output, indent_level)
        return output

    """ 
        Return just the output generated since function declaration have
    no body
        TODO look into the possibility of having a separate function 
    declaration class and letting the function know which file it is in
        @return just the function header (e.g. int example ();)
    """ 
    def return_func_declaration(self):
        return self.generate_output() + ";"

    """ 
        return the output with the format for a function body

        @param output the output of the file passed in for this class to 
            add content
        @param starting_index the index in which the function can start adding
            its information 
    """ 
    def return_func_definition(self, output, starting_index):
        temp_output = self.generate_output()
        while(len(output) <= starting_index):
            output.append("")
        output.insert(starting_index, (temp_output + "{"))
        output.insert(starting_index + 1, "")
        output.insert(starting_index + 2, "}")
    
    """ 
        After a function class have been created and its content have been modified,
    this function can be used to add the content of the function to the output buffer
    of the file
        @param output the output of the file passed in for this class to 
            add content
        @param starting_index the index where this class can start adding its content
    """ 
    def return_modified_func(self, output, starting_index, original_body_length):
        self.generate_output()
        cur_body_len = len(self.output)
        iterator = 1
        while(cur_body_len > 0 and original_body_length > 0):
            output[iterator + starting_index] = self.output[iterator -1]
            cur_body_len -= 1
            original_body_length -= 1
            iterator += 1
        while(cur_body_len > 0):
            output.insert(iterator + starting_index, self.output[iterator -1])
            cur_body_len -= 1
            iterator += 1
        while(original_body_length > 0):
            del output[iterator + starting_index]
            original_body_length -= 1

    """ 
        Returns the number of lines this function class is taking up within
    the file. 
        @param line if no specific line is passed in, the function will return 
            the number of lines this functino will take up. If a line number is 
            specified, then the class at that line number will be returned.
        @return returns the number of lines this class will be or if line parameter
            is specified then return the object at line
    """ 
    def return_num_lines(self, line= None):
        num_line = 0
        last_line = 0
        for token in self.tracker:
            num_line += token.return_num_lines()
            if(line != None):
                if(line <= num_line + 1 and line >= last_line + 1):
                    return token
        if(self.variable_dict):
            num_line += 1
        return num_line

    """ 
        Add content to the body of a function
        @param action_type can be either add or modify 
        @param name can be add for adding content to a line inside a function
            or modify for change the content of an existing line inside a function
            or Variable to add a variable inside the function
            or call to add a call inside the function
        TODO current setup not logical enough, revise
        TODO current setup will not work for a nested statement
        @param line Use this parameter if a specific item at a line needs to be modified
        @param func_name this paramter can be used to change a function by its name 
    """
    def add_to_function_body(self, action_type, name= None, line= None, value= None):
        if line != None:
            self.current_action = self.return_num_lines(line)
        if action_type == "add":
            self.set_current_action(name, value)
        elif action_type == "modify":
            if self.variable_dict.get(value) != None:
                self.current_action.handle_command(name, self.variable_dict.get(value).name)
            else:
                self.current_action.handle_command(name, value)
        elif action_type == "remove":
            self.tracker.remove(self.current_action)

    """ 
        This function can be used to add classes such as the calls class or
    variable class or if else or loop etc.
        @param name when used in this function, it should only be the name of one of 
            the classes stated above
        @param value in this case would be the name that you wish to give to the
            class 
        TODO naming illogical 
    """ 
    def set_current_action(self, name, value):
        if name == "call":
            self.current_action = calls.Calls()
            self.call_list.update({value:self.current_action})
        elif name == "variable":
            self.current_action = variable.Variable()
            self.variable_dict.update({value:self.current_action})
        self.current_action.name = value
        self.tracker.append(self.current_action)
