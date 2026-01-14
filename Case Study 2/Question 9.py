# Please  write  a  program  to  randomly  generate  a  list  with 6numbers,
# which  are divisible by 5 and 7, between 1 and 1500 inclusive.
import random

div_list = [item for item in range(1,1501) if item%35==0]
random_list = random.sample(div_list,6)
print(random_list)
