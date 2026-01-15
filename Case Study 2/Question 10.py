# Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0).
# Example
# If the following n is given as input to the program:5
# Then, the output of the program should be:3.55


def cal(n):
    return float((n)/(n+1))

num = int(input("Enter a number: "))
total = 0.0
for i in range(1,num+1):
    total += cal(i)
print(round(total,2))