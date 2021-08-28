from tkinter import Label, Tk 
import time
from setting import *

app_window = Tk() 
app_window.title("My Digital Time") 
app_window.geometry("350x150") 
app_window.resizable(0,0)

label = Label(app_window, font=TEXT_FONT, bg=BACKGROUND, fg=FOREGROUND, bd=BORDER_WIDTH)
label.place(relwidth=1)

def digital_clock(): 
   time_live = time.strftime("%H:%M")
   label.config(text=time_live) 
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()