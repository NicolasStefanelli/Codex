
class Include(object):
    def __init__(self):
        self.num_of_std_includes = 0
        self.num_of_user_def_includes = 0
        self.std_include_list = []
        self.std_user_def_list = []

    def add_std_include(self, string, output, starting_index):
        self.std_include_list.append(string)
        self.generate_output(output, starting_index)
        self.num_of_std_includes += 1

    def remove_std_include(self, str):
        del self.std_include_list[str]
        self.num_of_std_includes -= 1

    def generate_output(self, output, starting_index):
        print(self.std_include_list)
        index = 0
        for token in self.std_include_list:
            token = "#include <" + token + ">"
            output.insert(starting_index + index, token)
            index += 1
        
        # user_def_output = self.std_user_def_list.keys()
        # for tokens in user_def_output:
        #     lines.append(self.std_user_def_list.get(tokens))
        #     tokens = "#include \"" + tokens + "\""
        return output

    def return_num_lines(self):
        return self.num_of_std_includes + self.num_of_user_def_includes + 1

    # def add_user_def_list(self, str, bool):
    #     self.std_user_def_list.update({str:self.std_start + self.num_of_std_includes + 1})
    #     self.num_of_user_def_includes += 1

    # def remove_user_def_list(self, str, bool):
    #     del self.std_user_def_list[str]
    #     self.num_of_std_includes -= 1

