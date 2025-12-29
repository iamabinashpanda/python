# Create a login page that will ask for input such as Name and Password.

from tkinter import *
from tkinter.ttk import *

def validate():
    if name.get() and password.get():
        print("validation successful")
    else:
        print("validation failed")

#app panel
window = Tk()
window.title("User Login")
window.geometry("400x150")
window.configure(background="white")

# Styling
style = Style()
style.configure("Login.TLabel", foreground="black", background="white")

#name
Label(window,text="Name :",style="Login.TLabel").grid(row=0,column=0,ipady=10,ipadx=10)
name = StringVar()
Entry(window,textvariable=name,width=50).grid(row=0,column=1)

#password
Label(window,text="Password :",style="Login.TLabel").grid(row=1,column=0,ipady=10,ipadx=10)
password = StringVar()
Entry(window,textvariable=password,width=50,show="*").grid(row=1,column=1)

#login button
Button(window,text="Login",width=50,command=lambda :validate()).grid(row=2,column=1,ipady=10)


window.mainloop()