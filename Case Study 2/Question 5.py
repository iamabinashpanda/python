# Please write a program that counts and prints the numbers of each character in a string input by the console.
# Example
# If the following string is given as input to the program:abcdefgabc
# Then, the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

word = input("Enter a word :")
word = list(word.strip())
unique_word = dict().fromkeys(set(word),0)

for letter in word:
    unique_word[letter] += 1

for letter,count in zip(unique_word.keys(),unique_word.values()):
    print(f"{letter},{count}")
