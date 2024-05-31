class bikeshop:

    def __init__(self,stock):
        self.stock = stock

    def displaybike(self):
        print(f"Total bikes:{self.stock}")

    def rentforbike(self,q):
        if q <= 0:
            print("Positive No.")
        elif q > self.stock:
            print(f"Aviable bike are {self.stock}")
        else:
            print(f"Total price :{q*100}")
            print(f"Total bike {self.stock - q}")
            self.stock = self.stock - q 

while True:
    obj = bikeshop(100)
    a = int(input('''
1. Display bike
2.Rent a bike
3.Exit
''')) 
    if a == 1:
        obj.displaybike()
    elif a == 2:
        n = int(input("Enter the qty. :-"))
        obj.rentforbike(n)
    elif a == 3:
        break
    else:
        print("Enter the right option")                       