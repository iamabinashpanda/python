# Write a program that will find all the numbers between 1000 and 3000 (both excluded) such that each digit of a number is an odd number.
# Print the number of such elements

elements = list()
flag = True

for num in range(1001,3000):
    for c in str(num):
        if int(c)%2==0:
            flag = False
            break
        else:
            flag = True
    if flag:
        elements.append(str(num))
print(",".join(elements))