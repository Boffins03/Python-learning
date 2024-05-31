class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length*self.width
            
    
class Cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height=height

    def volume(self):
        return self.length*self.height*self.width

square=Square(4,4)
cube=Cube(2,4,6)

print(square.area())
print(cube.volume())
