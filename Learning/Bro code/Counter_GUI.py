# import tkinter as tk

# class CounterApp:
#     def __init__(self, master):
#         self.master = master
#         self.count = 0

#         self.canvas = tk.Canvas(master, width=100, height=100)
#         self.canvas.pack(pady=10)

#         self.update_circle()

#         self.inc_button = tk.Button(master, text="Increment", command=self.increment)
#         self.inc_button.pack(side=tk.LEFT, padx=5)

#         self.dec_button = tk.Button(master, text="Decrement", command=self.decrement)
#         self.dec_button.pack(side=tk.RIGHT, padx=5)

#     def increment(self):
#         self.count += 1
#         self.update_circle()

#     def decrement(self):
#         self.count -= 1
#         self.update_circle()

#     def update_circle(self):
#         self.canvas.delete("all")
#         # Draw circle
#         self.canvas.create_oval(10, 10, 90, 90, outline="black", fill="white")
#         # Display count in the center of the circle
#         self.canvas.create_text(50, 50, text=str(self.count), font=("Helvetica", 18))

# def main():
#     root = tk.Tk()
#     root.title("Counter App")
#     app = CounterApp(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()






from tkinter import *

count = 0
def add():
    global count
    count += 1
    canvas.update()

def subtract():
    global count
    count -= 1
    canvas.update()

window = Tk()

# title
window.title("Counter APP")

# window height and weight
window.geometry(f'{500}x{500}')

# background
window.configure(background = 'black',border=True)

# label
label = Label(window,text="Counter App",font='Ariel',padx=5,pady=5)
label.pack(side=TOP)

# Circle draw
canvas = Canvas(window,height=200,width=200,background='black',border=False)
canvas.create_oval(0,0,202,202,fill='white',width=5)
canvas.create_text(100,100,text=count)

canvas.pack(side=TOP)


# buttons
button1 = Button(window,text="-",command=subtract)
button2 = Button(window,text="+",command=add)
button1.pack()
button2.pack()

window.mainloop()