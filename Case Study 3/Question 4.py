# Create two functions - fillup and use, which uses a global variable as tank. Use
# the global variable in both the functions to return the quantity of fuel present
# in the tank after filling up the tank and after using the fuel of the tank. Show
# the working of two functions only. It is not necessary to display the outputs
from astropy.units import quantity

tank = 0

def fillup(quantity):
    global tank
    tank += quantity
    print(f"filled tank:{tank}")

def use(quantity):
    global tank
    tank -= quantity
    print(f"filled tank:{tank}")

fillup(10)
use(2)

fillup(10)
use(2)
