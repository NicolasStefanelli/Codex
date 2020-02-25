from .import variable

class Calls(object):
    def __init__(self):
        self.variable_list = []
        self.name = None

    def handle_command(self, name, value):
        if name == "add":
            self.variable_list.append(str(value))
        elif name == "delete":
            self.variable_list.remove(value)

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
        
    def num_line(self):
        return 1