from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive car")

    def stop(self):
        pass    

class MotorCycle(Vehicle):
    def go(self):
        print("You ride motorcycle")

    def stop(self):
        pass    


car=Car()
motorcycle=MotorCycle()
car.go()
motorcycle.go()