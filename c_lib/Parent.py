# parent abstract class used by other classes that utilize return_current_action, 
# return_modified statement, and num_line
# for more information on how to create abstract classes in python, the following videos may help:
# https://www.youtube.com/watch?v=PDMe3wgAsWg and https://www.youtube.com/watch?v=rOaRMW8jYOo

# Rylee Bers 3/18/2020

from abc import ABC, abstractmethod

class Parent(ABC):
    # Do we create an __init__ method fro abstract classes???
    # self.current_action = None
    # self.body = []
    
    @abstractmethod
    def return_current_action(self, line= None):
        if line != None:
            self.current_action = self.num_line(line)
        return self.current_action


    def return_modified_statement(self, output, starting_index, original_body_length):
        @abstractmethod
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

#TODO this function needs to be modified since not every class using it has this exact implementation
#TODO in each class that uses Parent, indicate that it 
# inherits from this class and change the implementation 
# of the functions inheriting to utilize super() 
    def num_line(self, line= None):
        @abstractmethod
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

