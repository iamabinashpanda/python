# Write a program that accepts a string and calculates the number of letters and digits.
# Suppose if the entered string is: Edureka123
# Then the output will be:
# LETTERS: -7
# DIGITS: -3

sentence = input("Enter a string :")
print(f"LETTERS : {len([x for x in sentence if x.isalpha()])}")
print(f"DIGITS : {len([x for x in sentence if x.isdigit()])}")
