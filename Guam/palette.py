from tkinter import *

def palette():
    global pass_f
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
        global callback
        callback = listbox.get(listbox.curselection())
        print(" Palette selected: " + callback)
        ws.destroy()

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

    ws.mainloop()

def main():
    global callback
    palette()
    print("Returning " + callback)
    return callback

#main()
#palette()