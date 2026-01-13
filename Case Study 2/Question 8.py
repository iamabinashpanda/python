# By using list comprehension, please write a program to
# print the list after removing the 1st,3rd,and 5th numbers in [12,24,35,70,88,120,155].

listA = [12,24,35,70,88,120,155]
index_to_remove = [1,3,5]

print([item for index,item in enumerate(listA) if index not in index_to_remove ])