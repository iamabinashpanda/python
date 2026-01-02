# Smith wishes to register ona ticket booking website for booking bus tickets.
# To authenticate the registration, he needs to provide a user-id and password.
# There are some built-in rules for checking the validity of the passwords entered by the users.
# Following are the rules for checking the validity of a password:
# i.At least 1 alphabet
# ii.At least 1 digit between [0–9]
# iii.At least 1 character from [@&]
# iv.Minimum length of transaction password: 5
# v.Maximum length of transaction password: 10

import re

def validate(id,pwd):
    if not (len(pwd) >=5) and (len(pwd)<=10):
        print("Minimum length of transaction password should be between : 5 to 10")
        return False
    elif not re.search(r'[0-9]',id):
        print("At least 1 digit between [0–9]")
        return False
    elif not re.search(r'[a-zA-Z]',id):
        print("At least 1 alphabet")
        return False
    elif not re.search(r'[@&]',id):
        print("At least 1 character from [@&]")
        return False
    else:
        return True

user_id = input("Enter User ID : ")
user_password = input("Enter User Password : ")

if validate(user_id,user_password):
    print("Registration Successfull")
else:
    print("Registration Failed ! Please try Again.")