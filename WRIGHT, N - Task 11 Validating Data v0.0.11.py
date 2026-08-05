import tkinter as tk
from tkinter import ttk

# --- Root window setup (implied in snippets) ---
root = tk.Tk()
root.title("Vowel Validator")  # Added for clarity

# --- STYLING (from snippet 1) ---
s = ttk.Style()
s.configure('Frame', background='#94B49F')

# --- WIDGETS (merged, removing duplicates) ---
mainFrame = ttk.Frame(root, style='Frame.TFrame', width=250, height=250)
mainFrame.grid(row=0, column=0, sticky='NEWS')

# region  ~~~~~~~~~~~~~~~~~~~~~~~~~~Validation 1
label1 = ttk.Label(mainFrame, text="1 Enter a vowel : ", font=('Helvetica', 10, 'bold'))
label1.grid(row=0, column=0, pady=15, padx=10, sticky="WE")  # using padx=10 from snippet 2

entry1 = ttk.Entry(mainFrame)
entry1.grid(row=0, column=1, pady=15, padx=10, sticky="NSEW")

button1 = ttk.Button(mainFrame, text="Validate")  # capitalized from snippet 2
button1.grid(row=0, column=2, padx=5, pady=15, sticky="NSEW")

status1 = ttk.Label(mainFrame, text="...Waiting for input")
status1.grid(row=0, column=3, padx=5, pady=15, sticky="NSEW")
# endregion

# --- Grid weight configuration (from snippet 2, essential for resizing) ---
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainFrame.columnconfigure(0, weight=1)
mainFrame.columnconfigure(1, weight=1)
mainFrame.columnconfigure(2, weight=1)

root.mainloop()
