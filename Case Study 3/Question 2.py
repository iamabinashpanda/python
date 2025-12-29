# Demonstrate the working of Polymorphism by creating two classes - Car and
# Bike. Display the information like name, color, and number of wheels.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def name(self, owner, name):
        pass

    @abstractmethod
    def color(self,color):
        pass

    @abstractmethod
    def wheels(self):
        pass

class Car(Vehicle):

    def name(self, owner, name):
        print(owner, name)

    def color(self,color):
        print(color)

    def wheels(self):
        print("number of wheels = 4")

class Bike(Vehicle):

    def name(self, owner, name):
        print(owner, name)

    def color(self, color):
        print(color)

    def wheels(self):
        print("number of wheels = 2")

b = Bike()
b.name("Malay","Kawasaki Z1000")
b.color("Green")
b.wheels()

c = Car()
c.name("Abinash","BMW i10")
c.color("Blue")
c.wheels()