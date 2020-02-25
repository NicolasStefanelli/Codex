import pyautogui
import fileinput
import time

class Writer(object):
    def __init__(self, file_name, file_path):
        self.current_file = file_name
        self.file_end = 0
        self.get_file_line_num(file_path)
        self.file_path = file_path

    def get_file_line_num(self, file_path):
        f = open(file_path)
        while True:
            try:
                self.file_end += 1
                next(f)
            except StopIteration:
                break
        f.close()

    def add_more_lines(self):
        f = open(self.file_path, "a+")
        f.write("\n\n\n")
        f.close()
        self.file_end += 3

    def write(self, output):
        f = fileinput.input(self.file_path, inplace= True)
        while(self.file_end < len(output)):
            self.add_more_lines()
        iterator = 1
        for token in f:
            if(iterator <= len(output)):
                token = output[iterator - 1]
                iterator += 1
            else:
                token = token.strip()
            print(token)
        fileinput.close()
        f.close()

    def clear_all(self):
        f = fileinput.input(self.file_path, inplace= True)
        for token in f:
            token = ""
            print(token, end="")
        fileinput.close()
        f.close()

