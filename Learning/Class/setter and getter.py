class student:
    
    def __init__(self) -> None:
        self.__name =""
    
    def getter(self):
        return self.__name
    def setter(self,name):
        self.__name=name

        
name = student()
name.setter("hello")
n = name.getter()
print(n)