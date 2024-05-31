from tkinter import *


def Submit():
    input_text = text.get("1.0",END)
    print(input_text)

window = Tk()

text= Text(window,
           font=("Arial",20),
           bg='light yellow',
           fg='purple',
           height=8,
           width=20,
           padx=20,pady=20)
text.pack()

button = Button(window,text="Submit",command=Submit)
button.pack()

window.mainloop()