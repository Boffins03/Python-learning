import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You finish breakfast")

def drink_coffee():
    time.sleep(3)
    print("You drink coffee")

def study():
    time.sleep(5)
    print("You finish studying")

x=threading.Thread(target=eat_breakfast,argu=())
x.start()

y=threading.Thread(target=drink_coffee,argu=())
y.start()

z=threading.Thread(target=study,argu=())
z.start()

eat_breakfast()
drink_coffee()
study()            

print(threading.active_count())
print(threading.enumerate())