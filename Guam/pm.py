# Guam PACKAGE MANAGER

print("Initiating...")
from distutils.log import error
import sys
import os
clear = lambda: os.system('cls')
from os.path import exists
import yaml

list_of_arguments = sys.argv

pm_location = __file__[:-5]
yml_location = pm_location + "version.yml"
does_yaml_exist = exists(yml_location)

# load YAML
if does_yaml_exist == True:
    with open(yml_location) as file:
        yaml_content = yaml.load(file, Loader=yaml.FullLoader)

    local_build = yaml_content["LOCAL_VERSION_BUILD"]
    local_version = yaml_content["LOCAL_VERSION_VERSION"]
    local_distribution = yaml_content["LOCAL_VERSION_DISTRIBUTION"]
    local_isalpha = yaml_content["LOCAL_VERSION_ISALPHA"]
    local_firstsetup = yaml_content["INITIAL_SETUP"]

    print("Local build: " + str(local_build))
    print("YAML Initiated!")
else:
    print("YML not initiated!")

global terminal_input_toggle
commandlist = "up\tChecks for update\nun\tUninstall\n\ntd\tDeletes temporary files\ngh\tOpens Github repository in your browser\nwb\tOpens guam.xyz in your browser\ntt\tOpens @GuamXYZ at Twitter in your browser\n"

# Error function
def print_error(error):
    erro_r = "ERROR:   " + error
    print(erro_r)
    print()
    print()




# TASKS:

# Update task
def task_update():
    print("Updating Guam!")

    if does_yaml_exist == False:
        print_error("version.yaml not found; you may have to reinstall Guam or download version.yaml from Git (command: 'gh')")
        return
    if local_distribution != "windowsnt-standalone":
        print_error("Sorry, it seems like you dont't have a ditribution supported by Package Manager updater.")
        return

    print("Current version:", local_build, local_version, local_distribution)

    

    print()


# Catching arguments
if len(list_of_arguments) > 1:
    task = list_of_arguments[1]
    if task == "up":
        task_update()

# Terminal
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