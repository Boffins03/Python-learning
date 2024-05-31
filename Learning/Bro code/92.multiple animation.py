from tkinter import *
import time


class ball():

    def __init__(self,canvas,x,y,diameter,xvelocity,yvelocity,color) -> None:
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)
        if (coordinates[2]>=(WIDTH) or coordinates[0]<0):
            self.xvelocity = - self.xvelocity
        if (coordinates[3]>=(HEIGHT) or coordinates[1]<0):
            self.yvelocity = - self.yvelocity
        self.canvas.move(self.image,self.xvelocity,self.yvelocity)    

HEIGHT = 500
WIDTH = 500
window = Tk()

canvas = Canvas(window,height=HEIGHT,width=WIDTH,bg="yellow")
canvas.pack()

vollyball = ball(canvas,0,0,100,1,1,'red')
baseball = ball(canvas,0,0,20,4,1,'orange')
tennisball = ball(canvas,0,0,30,3,2,'blue')
while True:
    baseball.move()
    tennisball.move()
    vollyball.move()
    window.update()
    time.sleep(0.01)


window.mainloop()