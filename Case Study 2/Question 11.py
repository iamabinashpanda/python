# FinBank is the latest entrant in the banking market of Thailand.
# The verification process for opening a bank account is done manually by reviewing the photocopy of the approved ID card.
# However, they have recently introduced a system where the customers’
# fingerprints will be mapped with the newly introduced Unique ID for citizens of Thailand by the government.
# FinBank should implement a system that verifies customers against their fingerprints and Unique Id.

# Key issues :
# Build a system where when a user enters a Unique ID,it gets
# encrypted so that hackers cannot view the mapping of the Unique ID and fingerprint.

# Approach to solve :
# 1.Read the input from the command line –UniqueID.
# 2.Check for validity of Unique ID–
#   it should be 10 digits and must contain only numbers.
# 3.Encrypt the UniqueID and print it.Enhancements for code

# You can try these enhancements in code.
# 1. Allow alphabets and some special characters in Unique ID
# 2.Provide the option for decryption to the user.

from cryptography.fernet import Fernet
from re import search

uniqueId = input("Enter a unique ID : ")

# this is the enhancement of the code -
# previous code could be found in different version of commit


if not ((search(r'[0-9]', uniqueId)) and (len(uniqueId) == 10) and (search(r'[a-zA-Z]',uniqueId)) and (search(r'[a]',uniqueId))):
    print("ID is invalid")
else:
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encoded_id = cipher_suite.encrypt(uniqueId.encode())
    print("Encrypted ID :",encoded_id)
    choice = input("Do you want to decrypt? (y/n): ")
    if choice.upper() == "Y":
        decoded_id = cipher_suite.decrypt(encoded_id).decode()
        print("Decrypted ID :",decoded_id)
    elif choice.upper() == "N":
        print("Thank You.")
    else:
        print("Invalid option. Please try again.")