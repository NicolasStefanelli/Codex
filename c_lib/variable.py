
class Variable(object):
    def __init__(self):
        self.type = "void "
        self.name = None
        self.value = None
        self.num_times_used = 0

    def handle_command(self, name, value):
        value = str(value)
        if name == "add":
            self.name = value
        elif name == "type":
            self.type = value + " "
        elif name == "value":
            self.value = value + ";"
        
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

    def num_line(self):
        return 1