# Author: Mr Wright
# Date: 10 June 26
# Purpose: Using Grid - Geometry Manager

import tkinter as tk
from tkinter import ttk

# -------------------FIRST WINDOW
root = tk.Tk()

# --------------------STYLING
root.geometry("800x600")

# --------------------WIDGETS

mainFrame = ttk.Frame(root, width = 250, height = 250)
mainFrame.grid()


# --------------------GRID



root.mainloop()
