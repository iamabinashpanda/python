# 1.Read FairDealCustomerData.csv
# 2.Name field contains full name –use a regular expression to separate title, first name, last name
# 3.Store the data in Customer Class
# 4.Create Custom Exception –CustomerNotAllowedException
# 5.Pass a customer to function "createOrder" and throw CustomerNotAllowedException in case of blacklisted value is 1
# Enhancement for code :
# 1.Change function createOrder to take productname and product code as input
# 2.Create Class OrderReturn object of type Order in case customer is eligible

import csv
import re
class Customer:
    def __init__(self,title,fname,lname,blacklisted):
        self.title = title
        self.fname = fname
        self.lname = lname
        self.blacklisted = blacklisted
customers = []
with open('./files/FairDealCustomerData.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        #[' Braund', ' Mr. Owen Harris ', '1']
        customer = Customer(
            title = re.findall(r'(.*\.) (.*.)',row[1])[0][0].strip(),
            fname = re.findall(r'(.*\.) (.*.)',row[1])[0][1].strip(),
            lname = row[0].strip(),
            blacklisted = row[2].strip()
        )
        customers.append(customer)
class CustomerException(Exception):
    """Base class for exceptions in this module."""
    pass

class BlacklistedException(CustomerException):
    """Raised when a blacklisted customer attempts an action."""
    pass

class BlacklistedException(Exception):
    def __init__(self, name, message="Customer Not Allowed"):
        self.name = name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.name} -> {self.message}"


def create_order(title, fname, lname):
    for customer in customers:
        if customer.title + customer.fname.strip() + customer.lname.strip() == title.strip() + fname.strip() + lname.strip():
            try:
                if int(customer.blacklisted) == 1:
                    raise BlacklistedException(customer.title + customer.fname.strip() + customer.lname.strip())
                    break
            except BlacklistedException as e:
                print(e)
            except Exception as e:
                print(e)


create_order('Don.', 'Manuel E ', 'Uruchurtu')