# Write a program that accepts a sentence and calculate the number of upper-case letters and lower-case letters

word = "Hello world!"
print("UPPER CASE",[x.isupper() for x in word].count(True))
print("LOWER CASE",[x.islower() for x in word].count(True))

