import threading
import time

def timer():
    print()
    print()
    count=0
    while True:
        time.sleep(1)
        count +=1
        print("You have log in for ",count,"second")


x=threading.Thread(target =timer,daemon=True)
x.start()

ans=input("Do you want to exit? ")