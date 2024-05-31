from tkinter import *
import time

HEIGHT = 500
WIDTH = 500
xvelocity = 3
yvelocity = 2
window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

bg_image = PhotoImage(file="E:\\Code\\Python\\Learning\\Bro code\\space.png")
image_bg = Canvas.create_image(0,0,image=bg_image,ANCHOR=NW)

my_image = PhotoImage(file="E:\\Code\\Python\\Learning\\Bro code\\ufo.png")
image = Canvas.create_image(0,0,image=my_image,ANCHOR=NW)

image_width = my_image.width()
image_height = my_image.height()

while True:
    coordinates = canvas.coords()
    print(coordinates)
    if (coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xvelocity = - xvelocity
    if (coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        yvelocity = - yvelocity
    canvas.move(image,xvelocity,yvelocity)        
    window.update()
    time.sleep(0.01)

window.mainloop()