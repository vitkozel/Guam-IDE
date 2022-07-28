from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter
#import tkinter
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as mb
import tkinter.font as tkfont
import subprocess
import chardet
import glob
from imageio import save
import platform
from os.path import exists
import datetime
import webbrowser
from numpy import character
import os
import sys

# Options variables
options_CHECK_FILE_CODING = 1
options_DEFAULT_FILE_CODING = "utf-8"
options_DISPLAY_FONT_TYPEFACE = "consolas"
options_DISPLAY_FONT_SIZE = "13"
options_DISPLAY_FONT_FONTSTYLE = "Bold"
options_DISPLAY_FONT_FONTFACE = options_DISPLAY_FONT_TYPEFACE + " " + options_DISPLAY_FONT_SIZE + " "
options_DISPLAY_DEBUG_SIZE = 6

# Session variables
global session_FILE_CODING
session_FILE_CODING = "utf-8"
global session_DEFAULT_EXTENSION
session_DEFAULT_EXTENSION = ".txt"
global session_FILE_TYPE
session_FILE_TYPE = "unknown"
global session_FILE_TYPE_DISPLAY
session_FILE_TYPE_DISPLAY = "Not saved yet"
global session_FILE_RUN_SUPPORT
session_FILE_RUN_SUPPORT = 0
global session_OUTPUT_WINDOW
session_OUTPUT_WINDOW = 0
session_DIRECTORY_THISFILE = __file__
global session_DIRECTORY_THISFOLDER
session_DIRECTORY_THISFOLDER = session_DIRECTORY_THISFILE[:-7]
global session_CURRENT_LEFT_STATUS
session_CURRENT_LEFT_STATUS = "Not saved yet!"
global session_IS_SAVED
session_IS_SAVED = True
session_PLATFORM = platform.system()
session_PYTHO_VERSION = sys.version_info[0]

# Other variables
others_DEBUG_MESSAGE_PREFIX = "GUAM: "
others_TAB_VALUE = "   "
others_ICON_LOCATION_FILE = "pigeon.png"
others_ICON_LOCATION = session_DIRECTORY_THISFOLDER + others_ICON_LOCATION_FILE
others_ISSUES_FILE_LOCATION = session_DIRECTORY_THISFOLDER + "issues.txt"

# create an instance for window
window = Tk()
if session_PLATFORM == "Windows": # if windows, set the window icon
    #window.iconbitmap(others_ICON_LOCATION)
    window.iconphoto(True, tkinter.PhotoImage(file=others_ICON_LOCATION))
    print(":tf:")
else:
    window.iconphoto(True, tkinter.PhotoImage(file=others_ICON_LOCATION))
    #print("Skipping icon, the program will run without an icon (OS compatibility issues")
print(session_DIRECTORY_THISFOLDER)
print(others_ICON_LOCATION)

# set title for window
window.title("Guam IDE")

# create and configure menu
menu = Menu(window)
window.config(menu=menu)

# create editor window for writing code
text = Text(window)
font = tkfont.Font(font=text['font'])
editor = ScrolledText(window, font = (options_DISPLAY_FONT_FONTFACE), wrap=None)
editor.pack(fill = BOTH, expand = 1)
editor.focus()
move_tab = font.measure(others_TAB_VALUE)
editor.config(tabs = move_tab)
file_path = ""


# called when saving/opening a file to change the status bar and other variables
def side_file_operation(side_operation_type):
    global session_FILE_TYPE_DISPLAY
    global session_CURRENT_LEFT_STATUS
    global chararcter
    global word
    global session_IS_SAVED
    global file_path
    global file_file
    global file_filename

    print("side_operation_type: " + side_operation_type)

    # checks file coding
    if options_CHECK_FILE_CODING == 1:
        for filename in glob.glob(file_path):
            with open(filename, 'rb') as rawdata:
                encoding_detect_result = chardet.detect(rawdata.read())
            print(filename.ljust(45), encoding_detect_result['encoding'])
        session_FILE_CODING = encoding_detect_result["encoding"]
    else:
        session_FILE_CODING = options_DEFAULT_FILE_CODING
        print("Skipping file coding check, the file will be opened with " + options_DEFAULT_FILE_CODING)    


    file_file = file_path.split("/")
    print(file_file)
    file_filename = str(file_file[len(file_file) - 1])
    print(file_filename)

    if side_operation_type != "save":
        check_file_type(file_filename)
    

    session_CURRENT_LEFT_STATUS = session_FILE_TYPE_DISPLAY + "; " + session_FILE_CODING
    special_left_status = session_CURRENT_LEFT_STATUS
    if side_operation_type == "save" or "saveas":
        special_left_status = session_CURRENT_LEFT_STATUS + " SAVED"     
    status_bars.config(text = f"{special_left_status} \t\t\t\t\t\t characters: {chararcter} words: {word}")    
   
    session_IS_SAVED = True
    window.title(file_filename + " - Guam IDE")

# function to open files
def open_file(event=None):
    global code, file_path
    global session_FILE_TYPE
    global session_FILE_RUN_SUPPORT
    global session_DEFAULT_EXTENSION
    global session_FILE_TYPE_DISPLAY
    global options_CHECK_FILE_CODING
    global session_FILE_CODING
    global file_path

    #code = editor.get(1.0, END)
    open_path = askopenfilename(filetypes=[("Any File", "*"), ("Python File", "*.py"), ("VKode Script", "*.vkode"), ("Text File", "*.txt")])
    if open_path == "":
        return
    file_path = open_path

    # finally opens the file
    with open(open_path, "r", encoding = session_FILE_CODING) as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)
        
    side_file_operation("open")
window.bind("<Control-o>", open_file)

# function to save files
def save_file(event=None):
    global code, file_path
    if file_path == '':
        save_path = asksaveasfilename(defaultextension = session_DEFAULT_EXTENSION, filetypes=[("Any File", "*"), ("Python File", "*.py"), ("VKode Script", "*.vkode"), ("Text File", "*.txt")])
        file_path = save_path
    else:
        save_path = file_path
    with open(save_path, "w", encoding = session_FILE_CODING) as file:
        code = editor.get(1.0, END)
        file.write(code)
    side_file_operation("save")
window.bind("<Control-s>", save_file)

# function to save files as specific name 
def save_as(event=None):
    global code, file_path
    #code = editor.get(1.0, END)
    save_path = asksaveasfilename(defaultextension = session_DEFAULT_EXTENSION, filetypes=[("Any File", "*"), ("Python File", "*.py"), ("VKode Script", "*.vkode"), ("Text File", "*.txt")])
    file_path = save_path
    with open(save_path, "w", encoding = session_FILE_CODING) as file:
        code = editor.get(1.0, END)
        file.write(code)
    side_file_operation("saveas")
window.bind("<Control-S>", save_as)

# function to execute the code and display its output
if 1 == 1:
    def run(event=None):
        global session_FILE_TYPE
        global code, file_path
        output_window.insert(1.0, others_DEBUG_MESSAGE_PREFIX + "Checking file, please wait")

        print("Running " + session_FILE_TYPE)

        # checks if the file is supported
        if session_FILE_RUN_SUPPORT == 1:

            # checks the file type
            if session_FILE_TYPE == "python":

                # checks if this python file is supported
                current_file_read_file = open(file_path, "r")
                current_file_read_content = current_file_read_file.read()
                if "input" not in current_file_read_content:
                    run_debug_target = 1
                else:
                    run_debug_target = 2
                
                '''
                code = editor.get(1.0, END)
                exec(code)
                '''    
                cmd = f"python {file_path}"

                if run_debug_target == 1: # run in internal debug console
                    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, shell=True)
                    output, error =  process.communicate()
                    # delete the previous text from output_windows
                    output_window.delete(1.0, END)
                    # insert the new output text in output_windows
                    output_window.insert(1.0, output)
                    # insert the error text in output_windows if there is error
                    output_window.insert(1.0, error)
                elif run_debug_target == 2: # run in new cmd window
                    subprocess.call(file_path, shell=True)
            else:
                if session_FILE_TYPE == "unknown":
                    mb.showerror("File not found", "Please save this file first before trying to run it.")
                else:
                    mb.showerror("File not supported", "It seems like this file is not supported in Guam IDE.")
        else:
            mb.showerror("File not supported", "It seems like this file is not supported in Guam IDE.")
    window.bind("<F5>", run)

# function to close IDE window
def close(event=None):
    global session_IS_SAVED

    if session_IS_SAVED == True:
        window.destroy()
    else:
        move_window = mb.askyesnocancel(title="File not saved", message="Do you want to save this file before exiting?")
        if move_window == True:
            print("Saving before exiting")
            save_file()
            window.destroy()
            exit(0)
        elif move_window == False:
            window.destroy()
            exit(0)
        else:
            return

window.bind("<Control-w>", close)

# define function to cut the selected text
def cut_text(event=None):
        editor.event_generate(("<<Cut>>"))

# define function to copy the selected text
def copy_text(event=None):
        editor.event_generate(("<<Copy>>"))

# define function to paste the previously copied text
def paste_text(event=None):
        editor.event_generate(("<<Paste>>"))
     
# create menus
file_menu = Menu(menu, tearoff=0)
edit_menu = Menu(menu, tearoff=0)
run_menu = Menu(menu, tearoff=0)
view_menu = Menu(menu, tearoff=0)
#theme_menu = Menu(menu, tearoff=0)
view_menu_thees = Menu(view_menu, tearoff=0)

# add menu labels
menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Edit", menu=edit_menu)
menu.add_cascade(label="Debug", menu=run_menu)
menu.add_cascade(label ="View", menu=view_menu)
#menu.add_cascade(label ="Theme", menu=theme_menu)
view_menu.add_cascade(label ="Theme", menu=view_menu_thees)

# add commands in flie menu
file_menu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator="Ctrl+W", command=close)

# add commands in edit menu
edit_menu.add_command(label="Cut", command=cut_text) 
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_separator() # Separator
edit_menu.add_command(label="Preferences")

# add commands in debug menu
run_menu.add_command(label="Run", accelerator="F5", command=run)

# function to display and hide status bar
show_status_bar = BooleanVar()
show_status_bar.set(True)
def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar = False 
    else :
        status_bars.pack(side=BOTTOM)
        show_status_bar = True
        
view_menu.add_checkbutton(label = "Status Bar" , onvalue = True, offvalue = 0,variable = show_status_bar , command = hide_statusbar)

# create a label for status bar
status_bars = ttk.Label(window,text = "Thanks for using Guam! \t\t\t\t\t\t characters: 0 words: 0")
status_bars.pack(side = BOTTOM)

# function to display count and word characters
text_change = False
def change_word(event = None):
    global text_change
    global session_CURRENT_LEFT_STATUS
    global chararcter
    global word
    global session_IS_SAVED

    if editor.edit_modified():
        text_change = True
        word = len(editor.get(1.0, "end-1c").split())
        chararcter = len(editor.get(1.0, "end-1c"))
        status_bars.config(text = f"{session_CURRENT_LEFT_STATUS} \t\t\t\t\t\t characters: {chararcter} words: {word}")
        session_IS_SAVED = False
    editor.edit_modified(False)
editor.bind("<<Modified>>",change_word)

# function for light mode window
def light():
    editor.config(bg="white")
    output_window.config(bg="white")

# function for dark mode window
def dark():
    editor.config(fg="white", bg="#191919")
    output_window.config(fg="white", bg="#000000")

# add commands to change themes
view_menu_thees.add_command(label="light", command=light)
view_menu_thees.add_command(label="dark", command=dark)

# create output window to display output of written code
if session_FILE_RUN_SUPPORT == 1:
    output_window = ScrolledText(window, height = options_DISPLAY_DEBUG_SIZE)
    output_window.pack(fill = BOTH, expand = 1)

# alternative way (when called)
def force_show_debug():
    global output_window
    global session_OUTPUT_WINDOW
    output_window = ScrolledText(window, height = options_DISPLAY_DEBUG_SIZE)
    output_window.pack(fill = BOTH, expand = 1)
    session_OUTPUT_WINDOW = 1

# hide the output window
def try_hide_debug():
    global output_window
    global session_OUTPUT_WINDOW
    if session_OUTPUT_WINDOW == 1:
        output_window.pack_forget()
        session_OUTPUT_WINDOW = 0
    elif session_OUTPUT_WINDOW == 0:
        print("Output box already hidden.")
    
def check_file_type(file_filename):
    global session_FILE_TYPE
    global session_FILE_RUN_SUPPORT
    global session_DEFAULT_EXTENSION
    global session_FILE_TYPE_DISPLAY
    global options_CHECK_FILE_CODING
    global session_FILE_CODING

    fileTypeSplit = file_filename.split(".")
    fileTypeIs = fileTypeSplit[-1]

    print("File type is: " + fileTypeIs)

    # COMPAIBILITY ISSUE: Match does not work on older versions of python (older than 3.10)
    # IF YOU ARE USING AN OLDER VERSION OF PYTHON, PLEASE FOLLOW QUICK TUTORIAL ON https://github.com/vitkozel/Guam-IDE/issues/6#issuecomment-1198041980
    """
    if session_PYTHO_VERSION > 3.10:
        match fileTypeIs:
            case "py":
                session_FILE_TYPE = "python"
                session_FILE_TYPE_DISPLAY = "Python script"
                session_FILE_RUN_SUPPORT = 1
            case "vkode":
                session_FILE_TYPE = "vkode"
                session_FILE_TYPE_DISPLAY = "VKode script"
                session_FILE_RUN_SUPPORT = 1
            case "txt":
                session_FILE_TYPE_DISPLAY = "TXT Plain text file"
                session_FILE_RUN_SUPPORT = 0
            case _:
                session_FILE_TYPE = "unsupported"
                session_FILE_TYPE_DISPLAY = "Unsupported file type"
                window_error("File not supported", "This file type is not supported. Guam will try to open it without a debug system.", True)
    else:
        if fileTypeIs == "py":
            session_FILE_TYPE = "python"
            session_FILE_TYPE_DISPLAY = "Python script"
            session_FILE_RUN_SUPPORT = 1
        elif fileTypeIs == "vkode":
            session_FILE_TYPE = "vkode"
            session_FILE_TYPE_DISPLAY = "VKode script"
            session_FILE_RUN_SUPPORT = 1
        elif fileTypeIs == "txt":
            session_FILE_TYPE_DISPLAY = "TXT Plain text file"
            session_FILE_RUN_SUPPORT = 0
        else:
            session_FILE_TYPE = "unsupported"
            session_FILE_TYPE_DISPLAY = "Unsupported file type"
            window_error("File not supported", "This file type is not supported. Guam will try to open it without a debug system.", True)
    # END OF COMMENT, remove comment below
    """
    if fileTypeIs == "py":
        session_FILE_TYPE = "python"
        session_FILE_TYPE_DISPLAY = "Python script"
        session_FILE_RUN_SUPPORT = 1
    elif fileTypeIs == "vkode":
        session_FILE_TYPE = "vkode"
        session_FILE_TYPE_DISPLAY = "VKode script"
        session_FILE_RUN_SUPPORT = 1
    elif fileTypeIs == "txt":
        session_FILE_TYPE_DISPLAY = "TXT Plain text file"
        session_FILE_RUN_SUPPORT = 0
    else:
        session_FILE_TYPE = "unsupported"
        session_FILE_TYPE_DISPLAY = "Unsupported file type"
        window_error("File not supported", "This file type is not supported. Guam will try to open it without a debug system.", True)
    #"""


    try_hide_debug()
    if session_FILE_RUN_SUPPORT == 1:
        print("Opening supported file")
        force_show_debug()
        session_DEFAULT_EXTENSION = "." + session_FILE_TYPE

    print("check_file_type results:\n session_FILE_TYPE: " + session_FILE_TYPE + "\n session_FILE_TYPE_DISPLAY: " + session_FILE_TYPE_DISPLAY + "\n session_FILE_RUN_SUPPORT: " + str(session_FILE_RUN_SUPPORT) + "\n session_DEFAULT_EXTENSION: " + session_DEFAULT_EXTENSION + "\n session_FILE_CODING: " + session_FILE_CODING)

def window_error(title, message, openIssues): # function to display error windows
    print("WARNING: " + title + ":\n " + message)
    mb.showerror(title, message)

    if openIssues:
        print("Opening issues window")

        if exists(others_ISSUES_FILE_LOCATION) == False:
            print("Creating issues file")
            isseFile = open(others_ISSUES_FILE_LOCATION, "w")
            isseFile.write("Guam for " + session_PLATFORM + "\nThis file location: " + others_ISSUES_FILE_LOCATION + "\n\n\n")
            isseFile.close()
        
        isseFile = open(others_ISSUES_FILE_LOCATION, "a")
        isseFile.write("Bug ocurred at: " + str(datetime.datetime.now()) + "\n " + title + ":\n " + message + "\n " + session_FILE_TYPE + "\n " + session_FILE_TYPE_DISPLAY + "\n " + str(session_FILE_RUN_SUPPORT) + "\n " + session_DEFAULT_EXTENSION + "\n " + session_FILE_CODING + "\n Python version: " + session_PYTHO_VERSION + "\n\n")
        isseFile.close()

        if mb.askyesno('Please report issue', 'Bug report was saved to /issues.txt\nDo you wish to report this bug to the developer?', icon='question'):
            print("Reporting issue")
            webbrowser.open("https://github.com/vitkozel/Guam-IDE/issues", new=1, autoraise=True)
            if session_PLATFORM == "Windows":
                os.startfile(session_DIRECTORY_THISFOLDER)
            elif session_PLATFORM == "Linux":
                subprocess.call(('xdg-open ', others_ISSUES_FILE_LOCATION))

window.mainloop()