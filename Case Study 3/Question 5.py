# Write a program to depict the use of multiple inheritance. The program should
# contain 4 classes - class 4 should inherit from class 2 and class 3. Similarly, class
# 2 should inherit from class 1. Class 3 should inherit from class 1. Each class
# should have its own print statement.

class One:
    print("class 1")

class Two(One):
    print("class 2")

class Three(One):
    print("class 3")

class Four(Two,Three):
    print("class 4")

f = Four()