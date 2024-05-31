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

a = area()
a.area()
a.area(4)                    
a.area(4,5)