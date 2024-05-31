class Duck:
    def walk(self):
        print("The duck in walking")
    def talk(self):
        print("The duck in talking")

class Chicken:
    def walk(self):
        print("The chicken is walking")
    def talk(self):
        print("The chicken is talking")

class Person:
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You catch a critter!")

duck=Duck()
chicken=Chicken()
person=Person() 

person.catch(chicken)