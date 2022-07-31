from tkinter import *

global result


#global result
def Scankey(event):
    val = event.widget.get()
    print(' Current input: "' + val + '"')

    if val == '':
        data = list
    else:
        data = []
        for item in list:
            if val.lower() in item.lower():
                data.append(item)				
    Update(data)
    #print(data)

def Update(data): # Update function
    listbox.delete(0, 'end')
    # put new data
    for item in data:
        listbox.insert('end', item)

def callback(event):
    global result
    callback = listbox.get(listbox.curselection())
    print(" Palette selected: " + callback)
    result = callback
    return callback


list = ('Change theme','DISPLAY_DEBUG_SIZE','DISPLAY_FONT_SIZE',
    'DISPLAY_FONT_TYPEFACE','DEFAULT_FILE_CODING',
    'CHECK_FILE_CODING','Save','Save As', 'Open' )

ws = Tk()
ws.title('Guam Command Palette')
ws.geometry('300x195')

entry = Entry(ws, width = 300)
entry.pack()
entry.bind('<KeyRelease>', Scankey)


listbox = Listbox(ws, width = 300)
listbox.pack()
Update(list)

callback = listbox.bind("<<ListboxSelect>>", callback)
#print(" Palette selected: " + callback)

ws.mainloop()

def main():
    global result
    palette()
    print(result)
    return result

main()
#palette()