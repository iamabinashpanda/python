# Create a dog object that will inherit all the variables and methods of the parent
# class Animal and display it.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def breed(self):
        pass
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Dog(Animal):

    def breed(self):
        print("I'm Dog")

    def eat(self):
        print("I eat dog food")

    def sleep(self):
        print("I sleep less")

d = Dog()
d.eat()
d.breed()
d.sleep()
