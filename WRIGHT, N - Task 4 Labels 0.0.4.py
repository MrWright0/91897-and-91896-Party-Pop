'''
Date: 22 June 2026
Author:  Mr Wright
Purpose: To experiment with labels
'''

import tkinter as tk
from tkinter import ttk

# -----------------------FUNCTIONS

# Function to open second window
def open_window():
    # My second window
    s_window = tk.Tk() 

# My first window
root = tk.Tk()

# -----------------------STYLING

root.geometry("800x600")
root.title("My First Window")
root.configure(bg="red")

# ---------------------Widgets

first_button = ttk.Button (root, text = "open window", command = open_window)
first_button.pack(pady = "50", padx = "50")

Name_Label = ttk.Label (root, text = "What is your name?", font = ("Times New Roman", 20, 'bold'))
Name_Label.pack()


root.mainloop()







