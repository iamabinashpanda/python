# Write a code that accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
# Hint: Use split() to split the string into a list and then apply sort()

sequence = input("Enter a sequence of words : ")
sequence = sequence.strip()
words= sequence.split()
words = sorted(sequence)
print("".join(words))