# Write a Python GUI program to create a Spin box widget using the Tkinter module.

from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Application 1")
window.geometry("500x500")

spin_val = IntVar()
Spinbox(from_=0,to=100,textvariable=spin_val).pack()

window.mainloop()