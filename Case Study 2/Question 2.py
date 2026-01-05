# Write a program for printing all elements of a list and their indexes in the list.
# Take the list as user input.

sentence = input("Enter elements in sequences of spaces :")
sentence = sentence.split()

for index,element in enumerate(sentence):
    print(f"{index}. {element}")