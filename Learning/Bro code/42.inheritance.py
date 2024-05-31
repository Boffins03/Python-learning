class Animal:

    alive=True
    def sleep(self):
        print("This animal is sleep")
        return self
    def eat(self):
        print("This animal is eating")
        return self    

class Rabbit(Animal):
    def run(self):
        print("rabbit can run")
        return self

class Fish(Animal):
    def swim(self):
        print("fish can swim")

class Hawk(Animal):
    def fly(self):
        print("hawk can fly")

rabbit=Rabbit()
fish=Fish()
hawk=Hawk()

#multi chain
rabbit.eat()\
    .sleep()\
    .run()


