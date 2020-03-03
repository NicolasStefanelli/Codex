"""
    Author:Jarvis Lu
    Date: 2/27/2020

    The file contains the variable class. Use this class to create variables
within a function
"""


""" 
    Initialization of the Variable class

    @instance type the type of value this variable will hold
    @instance name the name of the variable
    @instance value the value that this variable will hold, doesn't need to be specified
"""
class Variable(object):
    def __init__(self):
        self.type = "void "
        self.name = None
        self.value = None

    """ 
        handles the command passed in by the file. All subclass have a function
    name handle_command so we can call this function without a clear idea of what 
    the subclass is

        @param action when function calls this class the parameter was called
            name, will change in the future
        TODO stop being stuipd
        @param value the value that the user wish to assign to the variable
    """  
    def handle_command(self, action, value):
        value = str(value)
        if action == "add":
            self.name = value
        elif action == "type":
            self.type = value + " "
        elif action == "value":
            self.value = value + ";"
        
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
        if "" not in output:
            output.insert(0,"")
        index = output.index("")
        temp_out += self.type + self.name
        if self.value:
            temp_out += " = " + self.value
        else:
            temp_out += ";"
        output.insert(index, temp_out)

    """ 
        Returns how many lines this class is taking up, which for variables
            are always going to be one
    """
    def return_num_lines(self):
        return 1