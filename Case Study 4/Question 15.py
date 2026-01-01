# Give an example of fsum and sum function of math library

import math
numbers = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
sum_result = sum(numbers)
fsum_result = math.fsum(numbers)

print(f"Numbers to sum: {numbers}")
print(f"Result using sum():   {sum_result}")
print(f"Result using fsum():  {fsum_result}")