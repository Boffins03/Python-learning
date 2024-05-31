class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self):
        print('move')

    def draw(self):
        print('draw')


a=Point(10,30)
a.draw()
a.x=10
a.y=20
print(a.x)
b=Point()
b.x=10
print(b.x)