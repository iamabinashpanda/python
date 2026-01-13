# Write  a  program that can  compute  the  factorial of given  numbers.  Use recursion to find it.

def recursion(n):
    if n>0:
        return n * recursion(n-1)
    else:
        return 1
print(recursion(8))