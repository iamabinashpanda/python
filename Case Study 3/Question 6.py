# Use Getter and Setter method to set the name and age of a person. Moreover,
# get the name and age of the same person.

class Person:

    def getter(self):
        return (self.name, self.age)

    def setter(self, name, age):
        self.name = name
        self.age = age

p = Person()
p.setter("Abinash Panda",28)
print(p.getter())
