import os
from tkinter import *
from tkinter import filedialog , colorchooser,font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    color = colorchooser.askcolor(title="pick a color")
    text_area.config(fg=color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(),size_box.get()))

def new_file():
    window.title("Untitled")
    text_area.delete(1.0,END)

def open():
    file = askopenfilename(defaultextension=".txt",
                            title="Open a file",
                            files=[('All files','*.txt'),
                            ("Text Document", "*.txt")])
    
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0,END)

        with open(file,'r') as file:
            text_area.insert(1.0,file.read())
    
    except Exception:
        print("Error occur!")
                

def save():
    file = filedialog.asksaveasfilename(initialfile="Unititled.txt",
                                        defaultextension='.txt',
                                        filetypes=[('Text file','.txt'),
                                                   ('HTML','.html'),
                                                   ("All files",'.*')])
    filetext = str(text_area.get(1.0,END))
    with open(file,'w') as f:
        f.write(filetext)


def cut():
    text_area.event_generate("<< Cut >>")

def copy():
    text_area.event_generate("<< Copy >>")

def paste():
    text_area.event_generate("<< Paste >>")

window =Tk()
window.title("Text editor")
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window,font=(font_name.get(),font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky= N + E + S + W)
scroll_bar.pack(side=RIGHT , fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

color_button = Button(frame,text="color",command=change_color)
color_button.grid(row=0,column=0)

font_box = OptionMenu(frame,font_name,*font.families(),command=change_font)
font_box.grid(row=0,column=1)

size_box = Spinbox(frame,from_=1, to=100,textvariable=font_size,command=change_font)
size_box.grid(row=0,column=2)

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label="New file",command=new_file)
filemenu.add_separator()
filemenu.add_command(label="Open",command=open)
filemenu.add_separator()
filemenu.add_command(label="Save",command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)

editmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_separator()
editmenu.add_command(label="Copy",command=copy)
editmenu.add_separator()
editmenu.add_command(label="Paste",command=paste)




window.mainloop()