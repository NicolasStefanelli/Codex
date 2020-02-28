"""
    Author:Jarvis Lu
    Date: 2/27/2020

    This file contains the Writer class. The Writer class is used for all file_io
within this project. 

"""
import pyautogui
import fileinput
import time

""" 
    Initialization of the Writer class

    @param file_path path to the file that this writer class is going to write to 
    @instance file_end the end of the file
        Since the module fileinput can only modify the lines already in the file
        if not enough lines are in the file, we need to add blank lines to the end 
        of the file 
    @instance file_path the writer class remembers the path to the file it wrote to
"""
class Writer(object):
    def __init__(self, file_path):
        self.file_end = 0
        self.get_file_line_num(file_path)
        self.file_path = file_path

    """ 
        Get the number of lines within a file, this can be used to read a file that 
    was already created and have content within it 
        @param file_path the path to the file to be opened
    """
    def get_file_line_num(self, file_path):
        self.file_end = 0
        f = open(file_path)
        while True:
            try:
                self.file_end += 1
                next(f)
            except StopIteration:
                break
        f.close()

    """ 
        As stated above, the module fileinput can only modify lines but can't add lines
    if not enough lines are within a file, we add lines by adding blank lines into it
    """
    def add_more_lines(self):
        f = open(self.file_path, "a+")
        f.write("\n\n\n")
        f.close()
        self.file_end += 3

    """ 
        Write the desire output to the file. Due to the limitation of the module
    we have to rewrite the entire file everytime. So the content on the file needs 
    to be saved and modified, then write back into the file
        @param output the output that would be written to the file
    """
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

    """ 
        Clears the content of the file
    """
    def clear_all(self):
        f = fileinput.input(self.file_path, inplace= True)
        for token in f:
            token = ""
            print(token, end="")
        fileinput.close()
        f.close()

