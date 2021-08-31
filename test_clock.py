from setting import BACKGROUND, FOREGROUND
from tkinter import *

def enable(childList):
    for child in childList:
        child.configure(state='enable')

root = Tk()
root.geometry("300x300")
root.title("test_clock.py")

'''
for row_index in range(len(ALARM_HEIGHT_RATE)):
    alarm_tab.rowconfigure(row_index, weight=ALARM_HEIGHT_RATE[row_index])
alarm_tab.columnconfigure(0, weight=1)
'''

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
label1 = Label(root, background="#AAAAAA", bd=2, relief="solid")
label1.grid(column=0, row=0, sticky=N+S+E+W)

label1.rowconfigure(0, weight=1)
label1.columnconfigure(0, weight=1)
label2 = Label(label1, foreground=FOREGROUND, background=BACKGROUND)
label2.grid(column=0, row=0, sticky=N+S+E+W, padx=10, pady=10)

root.mainloop()