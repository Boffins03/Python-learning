class area:
    def __init__(self) -> None:
        pass

    def area(self, a = None, b = None):
        if a != None and b != None:
            print(a*b)
        elif a != None:
            print(a*a)
        else:
            print("nothing")

class square(area):
    def area(self, a=None):
        print(a*a)

a = area()
b = square
a.area()
a.area(4)                    
a.area(4,5)
b.area(5)