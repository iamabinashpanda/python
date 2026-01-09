# Design a banking system software with options like cash withdrawal, cash credit,and change password.
# The software must display appropriate results based on user inputs.

# banking system
class user:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    def change_password(self, pwd):
        print("\nInitiating Password Change ------")
        self.old = self.pwd
        self.new = pwd
        if (self.old == self.new):
            print("Old Password cannot be used again")
        else:
            self.pwd = self.new
            self.new = ''
            print("Password Changed")

    def display(self):
        print("Username :", self.name)
        print("Password :", self.pwd)


class bank(user):
    def __init__(self, name, pwd):
        super().__init__(name, pwd)
        self.current = 0

    def credit(self, amount):
        print("\nInitiating Deposit --------------")
        self.current += amount
        bank.balance(self)

    def withdrawal(self, amount):
        print("\nInitiating Withdrawal -----------")
        if self.current < amount:
            print("Insufficient Amount !!!")
        else:
            self.current -= amount
            bank.balance(self)

    def balance(self):
        print(f"your current balance is : ${self.current}")

    def display(self):
        print("\nProfile -------------------------")
        super().display()
        print(f"balance : ${self.current}")


username = input("Enter Username :")
password = input("Enter Password :")

user = bank(username, password)
print("\nWELCOME -------------------------------")
user.display()

while (True):
    print(
        ''' 
        1. Credit
        2. Withdrawal
        3. Change Password
        4. Exit
        '''
    )
    choice = int(input("Enter your choice :"))
    match choice:
        case 1:
            amount = int(input('Enter your amount :'))
            user.credit(amount)
        case 2:
            amount = int(input('Enter your amount :'))
            user.withdrawal(amount)
        case 3:
            amount = input('Enter new password :')
            user.change_password(amount)
        case 4:
            print("Thank You for using our system")
            break
        case _:
            print("Invalid option ! Try Again.")