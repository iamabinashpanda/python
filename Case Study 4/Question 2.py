# Data of XYZ company is stored in a sorted list. Write a program to search for specific data from that list.

sorted_list = ['Computer', 'Desk', 'Notebooks', 'Paper', 'Pen']
specific_data = 'Paper'
for index,item in enumerate(sorted_list):
    if(specific_data == item):
        print(f"'{item}' found in the list at position {index+1}")