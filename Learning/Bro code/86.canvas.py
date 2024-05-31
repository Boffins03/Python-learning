from tkinter import *

window = Tk()

canvas = Canvas(window,height=520,width=520)

# canvas.create_line(0,0,500,500,width=5,fill='Red')
# canvas.create_line(0,500,500,0,width=5,fill='Blue')
# canvas.create_rectangle(50,50,250,250,fill='purple')
# canvas.create_arc(0,0,500,500,style=PIESLICE,start='270',width=5,fill='green')
# canvas.create_polygon(250,0,500,500,0,500,fill='Yellow',outline="Black",width=5)

# pockemon ball
canvas.create_arc(10,10,500,500,extent=180,width=10,fill='red')
canvas.create_arc(10,10,500,500,extent=180,start='180',width=10,fill='white')
canvas.create_oval(190,190,310,310,fill='White',width=10)
canvas.pack()

window.mainloop()