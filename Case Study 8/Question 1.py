# Write a Python GUI program to add a button in your application using the Tkinter module
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Application 1")
window.geometry("500x500")
Button(text="Button",command=lambda : print("Button clicked")).pack()
window.mainloop()