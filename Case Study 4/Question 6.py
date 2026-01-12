# Write a prograthatch will find all numbers which are divisible by 7 but are not a multiple of 5, between 2,000 and 3,200(both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

print(",".join([str(x) for x in range(2000,3201) if x%7==0 and x%5 !=0]))