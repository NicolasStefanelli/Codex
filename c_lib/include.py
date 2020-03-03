"""
    Author:Jarvis Lu
    Date: 3/1/2020

    This file contains the Include class. Use this class for user define
and standard library include. 
"""

""" 
    Initialization of the include class

    @instance num_of_std_includes how many includes from the standard library within this file
    @instance num_of_user_def_includes numbers of user defined libraries (such as main.h)
    @instance std_include_list list containing the standard includes
    @instance std_user_def_list list of all user defined external libraries 
"""
class Include(object):
    def __init__(self):
        self.num_of_std_includes = 0
        self.num_of_user_def_includes = 0
        self.std_include_list = []
        self.std_user_def_list = []

    """ 
        Add a standard include to the class. The output of this class
    will be generated based on the includes within the class
        @param name name of the function to be added
        @param output the output of the file passed in for this class to 
            add content
        @param starting_index the index where the information will be placed
    """  
    def add_std_include(self, name, output, starting_index):
        self.std_include_list.append(name)
        self.generate_output(output, starting_index)
        self.num_of_std_includes += 1

    """ 
        Remove an existing include withing the class
        @param name name of the function to be added
    """  
    def remove_std_include(self, name):
        del self.std_include_list[name]
        self.num_of_std_includes -= 1


    """ 
        Generates the output based content within this class and place the 
    information within the output of the file so it could be printed later
        @param output the output of the file passed in for this class to 
            add content
        @param starting_index the index where the information will be placed
    """  
    def generate_output(self, output, starting_index):
        print(self.std_include_list)
        index = 0
        for token in self.std_include_list:
            token = "#include <" + token + ">"
            output.insert(starting_index + index, token)
            index += 1
        return output


    """ 
        Returns teh number of lines this class would be taking up
    """  
    def return_num_lines(self):
        return self.num_of_std_includes + self.num_of_user_def_includes + 1

