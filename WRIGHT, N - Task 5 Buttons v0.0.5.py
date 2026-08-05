

# importing only those functions
# which are needed
from tkinter import * 
from tkinter.ttk import *

# creating tkinter window
root = Tk()
# ---------------Function

def open_something():
    new_window = Tk()
    label_nw = Label (new_window, text = "Hi there, have a wonderful day!!!").pack()


# Adding widgets to the root window
Label(root, text = 'GeeksforGeeks', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)

# Creating a photoimage object to use image
photo = PhotoImage(file = r"Circle.png")

# here, image option is used to
# set image on button
Button(root, text = 'Click Me !', image = photo, command = open_something).pack(side = TOP)

mainloop()
