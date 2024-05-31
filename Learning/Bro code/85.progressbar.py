from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 100
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.05)
        progressbar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+'%')
        text.set(f'{download}/{GB} GB completed')
        window.update_idletasks()

window = Tk()
window.title("Progressbar")

percent = StringVar()
text = StringVar()

progressbar = Progressbar(window,orient=HORIZONTAL,length=300)
progressbar.pack()

percentlabel = Label(window,textvariable=percent).pack()
taskslabel = Label(window,textvariable=text).pack() 

button = Button(window,text="Download",command=start)
button.pack()

window.mainloop()