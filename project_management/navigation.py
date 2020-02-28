"""
    Author:Jarvis Lu
    Date: 2/27/2020

    This file contains some parsed interfereces for easier usage of pyautogui.
Given the situation it might not be nesscary to use pyautogui so this file would
not receive further support
"""
import pyautogui

def keyDown(lst):
    if isinstance(lst, list):
        for token in lst:
            pyautogui.keyDown(token)
    else:
        pyautogui.keyDown(lst)

def keyUp(lst):
    if isinstance(lst, list):
        for token in lst:
            pyautogui.keyUp(token)
    else:
        pyautogui.keyUp(lst)

def press(lst):
    if isinstance(lst, list):
        for token in lst:
            pyautogui.press(token)
    else:
        pyautogui.press(lst)

def command_list(lst):
    downed_keys = []
    for token in lst:
        if "down" in token:
            temp = token.split(" ")
            keyDown(temp[1])
            downed_keys.append(temp[1])
        else:
            press(token)
    for token in downed_keys:
        keyUp(token)

def go_to_line(desired_line):
    command_list(["down command", "p"])
    output = ":" + str(desired_line)
    write(output)

def remove_line(desired_line):
    go_to_line(desired_line)
    command_list(["down command", "down shift", "right", "delete", "delete"])

def write(output):
    if isinstance(output, list):
        for line in output:
            if "press" in line:
                lst = line.split()
                press(lst[1])
            else:
                pyautogui.typewrite(line)
    else:
        pyautogui.typewrite(str(output), pause=0.5)
    pyautogui.press("enter")

def write_without_enter(string):
    pyautogui.typewrite(str(string))