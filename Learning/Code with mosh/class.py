class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1=Point()
point1.x=10
print(point1.x)
point1.draw()

# Creating a class of human with name attribute and talk fuction
class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"Hi, {self.name}")

name=input("Enter your name:")
person=Person(name)
# print(person.name)
person.talk()
