# Write  a  program  that  accepts a sequence  of  lines  as  input  and
# prints  the  lines after making all characters in the sentence capitalized.

"""
Hello world
Practice makes perfect
"""
lines = list()
while(True):
    line = input("Enter Message :")
    if line == "":
        break
    lines.append(line.upper())
print(*lines,sep='\n')