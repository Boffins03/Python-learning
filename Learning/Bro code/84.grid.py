from tkinter import *

window = Tk()

firstnamelabe = Label(window,text='Firstname',width=20,background='red').grid(row=0,column=0)
firstnameentry = Entry(window).grid(row=0,column=1)

lastnamelabe = Label(window,text='Lastname',width=15,background='green').grid(row=1,column=0)
lastnameentry = Entry(window).grid(row=1,column=1)

emaillabe = Label(window,text='Email',width=10,background='blue').grid(row=2,column=0)
emailentry = Entry(window).grid(row=2,column=1)

Button(window,text="Submit").grid(row=3,column=0,columnspan=2)
window.mainloop()