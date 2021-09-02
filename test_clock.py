from setting import BACKGROUND, FOREGROUND
from tkinter import *
from typing import Collection
root = Tk()
root.geometry("300x300")
root.title("test_clock.py")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

label1 = Label(root, text="1", background=BACKGROUND, foreground=FOREGROUND)
label2 = Label(root, text="2", background=BACKGROUND, foreground=FOREGROUND)
label3 = Label(root, text="3", background=BACKGROUND, foreground=FOREGROUND)
label4 = Label(root, text="4", background=BACKGROUND, foreground=FOREGROUND)

label1.grid(row=0, column=0, rowspan=1, sticky=N+S+E+W)
label2.grid(row=0, column=1, rowspan=1, sticky=N+S+E+W)
label3.grid(row=1, column=0, sticky=N+S+E+W)
label4.grid(row=1, column=1, sticky=N+S+E+W)

for widget in root.winfo_children():
    widget.destroy()

label1 = Label(root, text="1", background=BACKGROUND, foreground=FOREGROUND)
label2 = Label(root, text="2", background=BACKGROUND, foreground=FOREGROUND)
label3 = Label(root, text="3", background=BACKGROUND, foreground=FOREGROUND)
label4 = Label(root, text="4", background=BACKGROUND, foreground=FOREGROUND)

label1.grid(row=0, column=0, columnspan=2, sticky=N+S+E+W)
label3.grid(row=1, column=0, sticky=N+S+E+W)
label4.grid(row=1, column=1, sticky=N+S+E+W)

root.mainloop()
'''
from setting import BACKGROUND, FOREGROUND
from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("test_clock.py")


root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
label1 = Label(root, background="#AAAAAA", bd=2, relief="solid")
label1.grid(column=0, row=0, sticky=N+S+E+W)

label1.rowconfigure(0, weight=1)
label1.columnconfigure(0, weight=1)
label2 = Label(label1, foreground=FOREGROUND, background=BACKGROUND)
label2.grid(column=0, row=0, sticky=N+S+E+W, padx=10, pady=10)

root.mainloop()
'''