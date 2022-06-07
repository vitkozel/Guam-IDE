# Guam PACKAGE MANAGER

print("Initiating...")
import sys
import os
clear = lambda: os.system('cls')

global terminal_input_toggle
commandlist = "up\tChecks for update\nun\tUninstall\n\ntd\tDeletes temporary files\ngh\tOpens Github repository in your browser\nwb\tOpens guam.xyz in your browser\ntt\tOpens @GuamXYZ at Twitter in your browser\n"

list_of_arguments = sys.argv

if len(list_of_arguments) > 1:
    task = list_of_arguments[1]


def task_update():
    print("Updating Guam!")
    print()
    


def terminal():
    global terminal_input_toggle
    print("Guam Package manager, how can I help you?")
    print(commandlist)
    while terminal_input_toggle == True:
        terminal_input = input()
        if terminal_input_toggle != "" or " ":
            execute(terminal_input)
        
    terminal_input_toggle = True

def execute(command):
    if command == "up":
        task_update()

clear()
terminal_input_toggle = True
terminal()