from .import variable
from .import calls
from .import if_else

lines_by_class = {"<class 'c_lib.calls.Calls'>":1,
                    "<class 'c_lib.variable.Variable'>":1}

class Func(object):
    def __init__(self, func_name, return_type):
        self.current_action = None
        self.argument_list = {}
        self.variable_list = {}
        self.call_list = {}
        self.return_type = return_type
        self.func_name = func_name
        self.body = []
        self.actions =[]

    def generate_output(self):
        arguments = self.argument_list.keys()
        output = self.return_type + " " + self.func_name + "("
        if arguments:
            for arg in arguments:
                output += self.argument_list.get(arg) + " " + arg + ","     
            output = output[:-1]
        output += ")"
        indent_level = 1
        self.body.clear()
        for token in self.actions:
            token.generate_output(self.body, indent_level)
        return output

    def return_func_declaration(self, output, starting_index):
        return self.generate_output() + ";"

    def return_func_definition(self, output, starting_index):
        temp_output = self.generate_output()
        while(len(output) <= starting_index):
            output.append("")
        output.insert(starting_index, (temp_output + "{"))
        output.insert(starting_index + 1, "")
        output.insert(starting_index + 2, "}")
    
    def return_modified_func(self, output, starting_index, original_body_length):
        self.generate_output()
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

    def return_num_lines(self, line= None):
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

    def add_to_function_body(self, action_type, name= None, line= None, value= None):
        if line != None:
            self.current_action = self.return_num_lines(line)
        if action_type == "add":
            self.set_current_action(name, value)
        elif action_type == "modify":
            if self.variable_list.get(value) != None:
                self.current_action.handle_command(name, self.variable_list.get(value).name)
            else:
                self.current_action.handle_command(name, value)
        elif action_type == "remove":
            self.actions.remove(self.current_action)

    def set_current_action(self, name, value):
        if name == "call":
            self.current_action = calls.Calls()
            self.call_list.update({value:self.current_action})
        elif name == "variable":
            self.current_action = variable.Variable()
            self.variable_list.update({value:self.current_action})
        self.current_action.name = value
        self.actions.append(self.current_action)
