from tkinter import *
from tkinter import filedialog

def Save():
    file = filedialog.asksaveasfilename(defaultextension='.txt',
                                        filetypes=[('Text file','.txt'),
                                                   ('HTML','.html'),
                                                   ("All files",'.*')])
    filetext = str(text.get(1.0,END))
    with open(file,'a') as f:
        f.write(filetext)
    

window = Tk()

text= Text(window,
           font=("Arial",20),
           bg='light yellow',
           fg='purple',
           height=8,
           width=20,
           padx=20,pady=20)
text.pack()

button = Button(window,text="Save",command=Save)
button.pack()

window.mainloop()