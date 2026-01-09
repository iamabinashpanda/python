# With  two  given  lists  [1,5,10,12,34,13]  and  [4,7,8,10,5,13,24],
# write  a  program  to create a new list whose elements are the intersection of the above-given lists.

list1 = [1,5,10,12,34,13]
list2 = [4,7,8,10,5,13,24]
print(list(set(list1).intersection(set(list2))))