# Write  a  program that accepts a  string from the  console and prints the  characters that have even indexes if the character is an alphabet.
# Concatenate the characters and print.
# Example
# If the following string is given as input to the program: Ed12ur3ka1Python12
# Then, the output of the program should be:EuaPto

words = input("Enter a string : ")
print("".join([word for index,word in enumerate(words) if index%2==0 and word.isalpha()]))