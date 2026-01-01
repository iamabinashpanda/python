# Design a code which will find whether the given number is Palindrome number or not

num = input("Enter a number: ")

if int(num) == int(num[::-1]):
    print("It\'s a Palindrome number")
else:
    print("It\'s not a Palindrome number")