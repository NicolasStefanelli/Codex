"""
    Author:Nicolas Stefanelli and Jarvis Liu
    Date: 3/17/2020

    This file contains the IfElse class. This class can be used to implement 
if else statements within the file.

    TODO finish the IfElse class

"""
class loops_and_conditionals_parent:
    def __init__(self):
        self.variable_list = []
        self.argument_list = []
        self.call_list = []
        self.body = []
        self.actions = []
        self.current_action = None

    def return_current_action(self, line= None):
        if line != None:
            self.current_action = self.num_line(line)
        return self.current_action

    def generate_output(self):
        pass

    def return_modified_statement(self, output, starting_index, original_body_length):
        self.body.append(self.generate_output())
        cur_body_len = len(self.body)
        iterator = 1
        while(cur_body_len > 0 and original_body_length > 0):
            output[iterator + starting_index] = self.body[iterator -1]
            cur_body_len -= 1
            original_body_length -= 1
            iterator += 1
        while(cur_body_len > 0):
            output.insert(iterator + starting_index, self.body[iterator -1])
            cur_body_len -= 1
            iterator += 1
        while(original_body_length > 0):
            del output[iterator + starting_index]
            original_body_length -= 1

    def num_line(self, line= None):
        num_line = 0
        last_line = 0
        for token in self.actions:
            num_line += token.num_line()
            if(line != None):
                if(line <= num_line + 1 and line >= last_line + 1):
                    return token
        if(self.variable_list):
            num_line += 1
        return num_line
        
class If(loops_and_conditionals_parent):
    def __init__(self):
        super().__init__()

    def generate_output(self,output,indent_level):
        output = ""
        count_indents = 0
        while(count_indents < indent_level):
            output += "\t"
            count_indents += 1
        output += "if("
        for token in self.argument_list:
            output += token + " "
        output += "){"
        
        return output

class Elif(loops_and_conditionals_parent):
    def __init__(self):
        super().__init__()
    
    def generate_output(self,output,indent_level):
        output = ""
        count_indents = 0
        while(count_indents < indent_level):
            output += "\t"
            count_indents += 1
        output += "else if("
        for token in self.argument_list:
            output += token + " "
        output += "){"
        
        return output

class Else(loops_and_conditionals_parent):
    def __init__(self):
        super().__init__()

    def generate_output(self,output,indent_level):
        output = ""
        count_indents = 0
        while(count_indents < indent_level):
            output += "\t"
            count_indents += 1
        output += "else{"
        for token in self.argument_list:
            output += token + " "
        output += "}"

        return output

class While(loops_and_conditionals_parent):
    def __init__(self):
        super().__init__()
    
    def generate_output(self,output,indent_level):
        output = ""
        count_indents = 0
        while(count_indents < indent_level):
            output += "\t"
            count_indents += 1
        output += "while("
        for token in self.argument_list:
            output += token + " "
        output += "){"
        
        return output

class For(loops_and_conditionals_parent):
    def __init__(self):
        super().__init__()

    def generate_output(self,output,indent_level):
        output = ""
        count_indents = 0
        while(count_indents < indent_level):
            output += "\t"
            count_indents += 1
        output += "for("
        for token in self.argument_list:
            # The ";" would have to be included in argument_list between the 3 parts the way this is set up
            output += token + " "
        output += "){"

        return output


    class Do_while(While):
        def __init__(self):
            super().__init__()

        def generate_output(self,output,indent_level):
            output = ""
            count_indents = 0
            while(count_indents < indent_level):
                output += "\t"
                count_indents += 1
            output += "do{"
            for token in self.argument_list:
                output += token + " "
            output += "}"

            # argument_list only contains the arguments for the "do" part until 
            # While's generate output is called
            output += (While.__init__(self)).generate_output(self,output,indent_level)
            output = output[:-1] # remove the un-needed "{"

            return output
    
    

    


