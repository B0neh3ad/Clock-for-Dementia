import tkinter
import tkinter.ttk
import datetime
import platform
from setting import *
from math import *

def pos(width=WIDTH, height=HEIGHT, x=X, y=Y):
    return "x".join([str(width), "+".join([str(height), str(x), str(y)])]) 

app_window = tkinter.Tk()
app_window.title(TITLE)
app_window.geometry(pos())
app_window.resizable(False, False)

tabs_control = tkinter.ttk.Notebook(app_window)

# 1. 시계
clock_tab = tkinter.Frame(tabs_control, bg=BACKGROUND)
tabs_control.add(clock_tab, text="시계")

# 2. 알람
alarm_tab = tkinter.Frame(tabs_control)
tabs_control.add(alarm_tab, text="알람")

# 3. 설정
setting_tab = tkinter.Frame(tabs_control)
tabs_control.add(setting_tab, text="설정")

tabs_control.pack(expand=True, fill="both")
app_window.mainloop()

# TODO: label state option으로 active/disabled 설정하여 이에 따라 자동으로 레이아웃 조정되도록...
# TODO: 알람 시/분 active color 지정.
# TODO: 스위치/버튼 제어 공부 -> 함수랑 binding
# TODO: Bind 함수 이용해서 스위치/버튼 제어할 수 있나?
# TODO: 일단 탭으로 구현해보고... 실제로는 탭 말고 input에 따라 함수 호출을 통한 "화면" 전환으로 가야할 듯