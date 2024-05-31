class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f'Hi,I_am_{name}')

john=Person('John')
john.talk()