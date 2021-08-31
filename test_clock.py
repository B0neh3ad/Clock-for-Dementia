from setting import BACKGROUND, FOREGROUND
from tkinter import *
from tkinter import ttk

def enable(childList):
    for child in childList:
        child.configure(state='enable')

root = Tk()
root.geometry("300x300")
root.title("test_clock.py")

label1 = ttk.Label(root, padding=(10,10,10,10), background=BACKGROUND, borderwidth=2)
label1.grid(column=0, row=0, padx=10, pady=10, sticky=N+S+E+W)
label2 = ttk.Label(label1, text="yes", foreground=FOREGROUND, background=BACKGROUND)
label2.pack(expand=True, fill=BOTH)

root.mainloop()