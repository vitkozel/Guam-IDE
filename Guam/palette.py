from tkinter import *

def palette():
    def Scankey(event):
        val = event.widget.get()
        print(val)

        if val == '':
            data = list
        else:
            data = []
            for item in list:
                if val.lower() in item.lower():
                    data.append(item)				
        Update(data)


    def Update(data): # Update function
        listbox.delete(0, 'end')
        # put new data
        for item in data:
            listbox.insert('end', item)



    list = ('Change theme','DISPLAY_DEBUG_SIZE','DISPLAY_FONT_SIZE',
        'DISPLAY_FONT_TYPEFACE','DEFAULT_FILE_CODING',
        'CHECK_FILE_CODING','Save','Save As', 'Open' )

    ws = Tk()
    ws.title('Guam Command Palette')
    ws.geometry('300x300')

    entry = Entry(ws)
    entry.pack()
    entry.bind('<KeyRelease>', Scankey)


    listbox = Listbox(ws)
    listbox.pack()
    Update(list)

    ws.mainloop()

palette()