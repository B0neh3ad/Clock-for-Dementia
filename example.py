from tkinter import *
import tkinter

col_cnt = [1,2,1]

#Create & Configure root 
root = Tk()
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#Create & Configure frame 
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

label1 = Label(frame, text="yy")
label2 = Label(frame, text="dd")
label3 = Label(frame, text="dd")
label4 = Label(frame, text="dd")

label1.grid(row=0, column=0, columnspan=2)
label2.grid(row=1, column=0)
label3.grid(row=1, column=1)
label4.grid(row=2, column=0, columnspan=2)

for row_index in range(3):
    Grid.rowconfigure(frame, row_index, weight=1)
for col_index in range(2):
    Grid.columnconfigure(frame, col_index, weight=1)

'''
#Create a 5x10 (rows x columns) grid of buttons inside the frame
for row_index in range(3):
    Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(col_cnt[row_index]):
        Grid.columnconfigure(frame, col_index, weight=2//col_cnt[row_index])
        btn = Button(frame) #create a button inside frame 
        btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)  
'''

root.mainloop()
'''
import tkinter
import tkinter.ttk
from tkinter.constants import *
from setting import *
from math import *

def pos(width=WIDTH, height=HEIGHT, x=X, y=Y):
    return "x".join([str(width), "+".join([str(height), str(x), str(y)])]) 

window = tkinter.Tk()
window.title(TITLE)
window.geometry(pos())
window.resizable(True, True)

width=1

print(TOP, BOTTOM, CENTER)
s=tkinter.ttk.Separator(window, orient="vertical")
s.place(relx=1/3, relheight=1)

s=tkinter.ttk.Separator(window, orient="vertical")
s.place(relx=2/3, relheight=1)


def drawing(event):
    if width>0:
        x1=event.x-1
        y1=event.y-1
        x2=event.x+1
        y2=event.y+1
        canvas.create_oval(x1, y1, x2, y2, fill="blue", width=width)

def scroll(event):
    global width
    if event.delta==120:
        width+=1
    if event.delta==-120:
        width-=1
    label.config(text=str(width))

canvas=tkinter.Canvas(window, relief="solid", bd=2)
canvas.pack(expand=True, fill="both")
canvas.bind("<B1-Motion>", drawing)
canvas.bind("<MouseWheel>", scroll)

label=tkinter.Label(window, text=str(width))
label.pack()
'''
'''
def close():
    window.quit()
    window.destroy()

frame2=tkinter.Frame(window, relief="solid", bd=2)
frame2.place(relwidth=1, relheight=0.5)

frame3=tkinter.Frame(window, relief="solid", bd=2)
frame3.place(rely=0.5, relwidth=1, relheight=0.3)

frame4=tkinter.Frame(window, relief="solid", bd=2)
frame4.place(rely=0.8, relwidth=1, relheight=0.2)

label2_1=tkinter.Label(frame2, text="8/25")
label2_1.place(relwidth=0.5, relheight=1)

label2_2=tkinter.Label(frame2, text="수요일")
label2_2.place(relx=0.5, relwidth=0.5, relheight=1)

label4_1=tkinter.Label(frame4, text="아침")
label4_1.place(relwidth=0.5, relheight=1)

label4_2=tkinter.Label(frame4, text="12:08")
label4_2.place(relx=0.5, relwidth=0.5, relheight=1)

label3_1=tkinter.Label(frame3, text="2021년")
label3_1.place(relwidth=0.5, relheight=1)

label3_2=tkinter.Label(frame3, text="여름")
label3_2.place(relx=0.5, relwidth=0.5, relheight=1)

def select(self):
    value="값 : "+str(scale.get())
    label.config(text=value)

var=tkinter.IntVar()

scale=tkinter.Scale(window, variable=var, command=select, orient="horizontal", showvalue=False, tickinterval=50, to=500, length=300)
scale.pack()

label=tkinter.Label(window, text="값 : 0")
label.pack()

def check():
    label.config(text=RadioVariety_1.get())
    
labelframe=tkinter.LabelFrame(window, text="플랫폼 선택")
labelframe.pack()

RadioVariety_1=tkinter.StringVar()
RadioVariety_1.set("미선택")

radio1=tkinter.Radiobutton(labelframe, text="Python", value="가능", variable=RadioVariety_1, command=check)
radio1.pack()
radio2=tkinter.Radiobutton(labelframe, text="C/C++", value="부분 가능", variable=RadioVariety_1, command=check)
radio2.pack()
radio3=tkinter.Radiobutton(labelframe, text="JSON", value="불가능", variable=RadioVariety_1, command=check)
radio3.pack()
label=tkinter.Label(labelframe, text="None")
label.pack()

    1. 위에처럼 place()로 위젯 배치
    2. 조건 분기해서 frame 다르게 주고 각각에 따라 pack()으로 위젯 배치

# 요 밑에처럼 똑같은 변수로 해도 pack() 이후에는 영향 안 받으니까 해도 됨
button3=tkinter.Label(frame3, text="2021년")
button3.pack(side="left")

button3=tkinter.Label(frame3, text="여름")
button3.pack(side="right")

label = tkinter.Label(window, text="0")
label.pack()

button = tkinter.Button(window, text="a", anchor="e", overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100)
button.pack()

menubar=tkinter.Menu(window)

menu_1=tkinter.Menu(menubar, tearoff=0)
menu_1.add_command(label="하위 메뉴 1-1")
menu_1.add_command(label="하위 메뉴 1-2")
menu_1.add_separator()
menu_1.add_command(label="하위 메뉴 1-3", command=close)
menubar.add_cascade(label="상위 메뉴 1", menu=menu_1)

menu_2=tkinter.Menu(menubar, tearoff=0, selectcolor="red")
menu_2.add_radiobutton(label="하위 메뉴 2-1", state="disable")
menu_2.add_radiobutton(label="하위 메뉴 2-2")
menu_2.add_radiobutton(label="하위 메뉴 2-3")
menubar.add_cascade(label="상위 메뉴 2", menu=menu_2)

menu_3=tkinter.Menu(menubar, tearoff=0)
menu_3.add_checkbutton(label="하위 메뉴 3-1")
menu_3.add_checkbutton(label="하위 메뉴 3-2")
menubar.add_cascade(label="상위 메뉴 3", menu=menu_3)

window.config(menu=menubar)

message=tkinter.Message(window, text="메세지입니다.\n메세지\n메", width=100, relief="solid", justify="center")
message.pack()
'''
# 화면 갱신될 때 얘는 어카냐?
window.mainloop()

print("Window Close")