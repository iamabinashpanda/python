# Create three radio buttons that will include 3 fields : First,Second,and Third.

from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Radio Button App")
window.geometry("400x300")
options = {
    "First":1,
    "Second":2,
    "Third":3
}
choice = IntVar()
for option,value in options.items():
    Radiobutton(window,text=option,variable=choice,value=value,padding=10).pack(side=LEFT)

window.mainloop()