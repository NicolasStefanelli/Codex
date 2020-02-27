from .import include
from .import function
from .import variable
from file_io import writer

class File(object):
    def __init__(self, file_name, file_path):
        self.num_func = 0
        self.name = file_name
        self.file_path = file_path + "/" + file_name
        self.function_list = {}
        self.current_function = None
        self.indent_level = 0
        self.writer = writer.Writer(file_name, file_path)
        self.include = include.Include()   
        self.function_list = {}
        self.output = []
        self.tracker = []
        
    def write_output(self):
        self.writer.write(self.output)

    def add_std_include(self, include):
        self.include.add_std_include(include, self.output, self.return_write_line())
        self.tracker.append(self.include)
        
    def add_function(self, func_name, return_type, func_type):
        new_func = function.Func(func_name, return_type)
        self.function_list.update({new_func.func_name:new_func})
        if(func_type == "definition"):
            new_func.return_func_definition(self.output, self.return_write_line())
        elif(func_type == "declaration"):
            new_func.return_func_declaration(self.output, self.return_write_line())
        self.tracker.append(new_func)
        self.current_function = new_func

    def add_to_function_body(self, action_type, name= None, line= None, value= None, func_name= None):
        if func_name != None:
            self.current_function = self.function_list.get(func_name)
        if line != None:
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
        
    


# Garbage that I haven't thrown out but most likely will--Jarvis 2/26/2020
    # def write_function(self, func_name):
    #     self.current_function = self.function_list.get(func_name)
    #     if(".h" in self.name):
    #         output = self.current_function.return_func_declaration()
    #         self.writer.write(output)
    #         self.next_func_line = self.current_function.end
    #     else:
    #         output = self.current_function.return_func_definition()
    #         self.writer.write(output)
    #         self.next_func_line = self.current_function.end
    #     self.indent_level += 1

    # def add_to_function_body(self, command, name, type_of= None, line= None, func_name = None):
    #     if func_name != None:
    #         self.current_function = self.function_list.get(func_name)
    #     if command == "variable":
    #         self.current_function.add_variable(type_of, name)
    #     elif command == "argument":
    #         self.current_function.add_argument(type_of, name)
    #     elif command == "call":
    #         if line != None:
    #             self.get_indentation_at_line(line)
    #         output = self.current_function.add_call(line, name, self.indent_level)
    #         self.writer.write(output)
    #     else:
    #         pass

    # def modify_current_action(self, command, line= None):
    #     output = self.current_function.modify_current_action(command, line)
    #     self.writer.write(output)

    # def get_indentation_at_line(self, line):
    #     functions = self.function_list.keys()
    #     for func in functions:
    #         ret = func.return_indent_level(line)
    #         if (ret != 0):
    #             self.indent_level = ret

    # def clear(self):
    #     self.writer.clear_all()
