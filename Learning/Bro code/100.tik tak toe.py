from tkinter import *

count = 0
def print():
    global count 
    

window = Tk()
button1 = Button(window,bd=5,width=6,height=2,text="",command=print)
button1.grid(row=0,column=0)
button2 = Button(window,bd=5,width=6,height=2,text="",command=print)
button2.grid(row=0,column=1)
button3 = Button(window,bd=5,width=6,height=2,text="",command=print)
button3.grid(row=0,column=2)
button4 = Button(window,bd=5,width=6,height=2,text="",command=print)
button4.grid(row=1,column=0)
button5 = Button(window,bd=5,width=6,height=2,text="",command=print)
button5.grid(row=1,column=1)
button6 = Button(window,bd=5,width=6,height=2,text="",command=print)
button6.grid(row=1,column=2)
button7 = Button(window,bd=5,width=6,height=2,text="",command=print)
button7.grid(row=2,column=0)
button8 = Button(window,bd=5,width=6,height=2,text="",command=print)
button8.grid(row=2,column=1)
button9 = Button(window,bd=5,width=6,height=2,text="",command=print)
button9.grid(row=2,column=2)

window.mainloop()