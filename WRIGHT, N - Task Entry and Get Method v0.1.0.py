'''
Date: 30 June 2026
Author: Mr Wright
Purpose: Experiement with the entry widgets and get method
'''

import tkinter as tk
from tkinter import ttk

# -------- Windows
root = tk.Tk()
root.title("Entry Widget")

# ------- Styling

s = ttk.Style()
s.configure('Frame.TFrame', background = '#41707A')

# -------Widgets

mainFrame = ttk.Frame(root, width = 250, height = 250, style = 'Frame.TFrame')
mainFrame.grid(row = 0, column = 0, sticky = "NSEW")

entry1 = ttk.Entry(mainFrame)
entry1.grid(row = 0, column = 0, padx = 10, pady =10)

# -------- Grid Configuration







root.mainloop()
