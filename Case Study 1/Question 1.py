# Write a program to find the factors of a given number and check whether the factor is even or odd.
# Hint: Use Loop with if-else statements

num = int(input("Enter Number :"))
print(f"Factor of {num} are :")
for n in range(1,num+1):
    if num % n == 0:
        if n % 2 == 0:
            print(f"{n} : Even Number")
        else:
            print(f"{n} : Odd Number")