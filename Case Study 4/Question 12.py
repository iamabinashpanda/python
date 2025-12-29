# Write  a  program  that  accepts  a  sequence  of whitespace-separated words  as input and
# prints the words after removing all duplicate words and sorting them alphanumerically.

word = "hello world and practice makes perfect and hello world again"
print(" ".join(sorted(set(word.split()))))