# Write a program that takes 2 digits, X, Yas input and generates a 2-dimensional array.
# The element value in the ith row and jth column of the array should be i*j.

val = input("Enter dimension :")
a,b = val.split(',')
print([[x*y for x in range(int(b))] for y in range(int(a))])