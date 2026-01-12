# By using list comprehension,
# please write a program to print the list after removing the values which are divisible by 6 in [12,24,35,24,88,120,155].

listA = [12,24,35,24,88,120,155]
[listA.remove(x) for x in listA if x%6==0]
print(listA)