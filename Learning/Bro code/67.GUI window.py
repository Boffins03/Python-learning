from tkinter import *
window=Tk()# instantiate an instance of window
window.geometry("420x420")
window.title("Image")
icon=PhotoImage(file="E:\\Code\\images.png")
window.iconphoto(True,icon)
window.config(background="#5cfcff")
window.mainloop()# lauch window
