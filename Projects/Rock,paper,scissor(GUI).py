from tkinter import *

def human():
    human = Tk() # independent of botton window
    human.title("Game")
    window.destroy()

    # Human window
    label1 = Label(human,text="Plater 1")
    label1.grid(row=0,column=0,columnspan=3)
    button1 = Button(human,text="Rock")
    button1.grid(row=1,column=0)
    button2 = Button(human,text="Paper")
    button2.grid(row=1,column=1)
    button3 = Button(human,text="Scissor")
    button3.grid(row=1,column=2)

    # line = Canvas.create_line(0,0)
    # line.grid(row=2,column=0)
    button4 = Button(human,text="Rock")
    button4.grid(row=3,column=0)
    button5 = Button(human,text="Paper")
    button5.grid(row=3,column=1)
    button6 = Button(human,text="Scissor")
    button6.grid(row=3,column=2)
    label2 = Label(human,text="Player 2")
    label2.grid(row=4,column=0,columnspan=3)

def computer():
    computer = Tk() # independent of botton window
    computer.title("Game")
    window.destroy()

# First window
window = Tk()
window.title("Game")
canvas1 = Canvas(window,height=1024,width=1024)

label1 = Label(canvas1,text="Play with Human",border=2)
label1.grid(row=0,column=0)
button = Button(canvas1,text="OK",command=human)
button.grid(row=0,column=1)
label2 = Label(canvas1,text="Play with Computer",border=2)
label2.grid(row=1,column=0)
button = Button(canvas1,text="OK",command=computer)
button.grid(row=1,column=1)
canvas1.pack(side="top",expand=True,fill='both')

window.mainloop()