import tkinter
import tkinter.ttk
from tkinter.constants import *
import datetime
import platform
from setting import *
from math import *

# TODO: mode 변수 값에 따라 스크린 전환하는 쪽으로...
mode = 0

# TODO: 시작할 때 외부 파일 읽어서 menu_state 결정되도록.
menu_state = [NORMAL, NORMAL, NORMAL, NORMAL, NORMAL, NORMAL]

# TODO: 버저음은 따로 구현해야 됨

def get_part(hour):
    '''
    Return part of the day responding to the hour parameter
    '''
    res = ""
    if 0 <= hour < 5:
        res = "새벽"
    elif hour < 9:
        res = "아침"
    elif hour < 17:
        res = "낮"
    elif hour < 21:
        res = "저녁"
    else:
        res = "밤"
    
    return res

def get_season(month):
    '''
    Return season responding to the month parameter
    '''
    res = ""
    if 3 <= month <= 5:
        res = "봄"
    elif 6 <= month <= 8:
        res = "여름"
    elif 9 <= month <= 11:
        res = "가을"
    else:
        res = "겨울"
    
    return res

# TODO: Raspberry Pi에서 시간 fetch -> 변수에 시간 저장
def clock():
    '''
    Fetch time data using 'datatime' module
    and with this data, set text of labels in clock tab
    '''
    date_time = datetime.datetime.now().strftime("%Y년 %m/%d %H:%M")
    wday = WEEKDAY[datetime.datetime.now().weekday()]
    year, date, time1 = date_time.split()
    season = get_season(int(date.split("/")[0]))

    hour, minutes = time1.split(':')
    part = get_part(int(hour))
    
    if int(hour) > 12 and int(hour) < 24:
        hour = str(int(hour) - 12)
        if len(hour) == 1:
            hour = '0' + hour
    time = ":".join([hour, minutes])
    
    text_list = [date, wday, part, time, year, season]

    for i in range(6):
        label_list[i].config(text = text_list[i])

    label_list[0].after(1000, clock)

def pos(width=WIDTH, height=HEIGHT, x=X, y=Y):
    '''
    Return string showing position of root window
    '''
    return "x".join([str(width), "+".join([str(height), str(x), str(y)])]) 

def select_tab(event):
    '''
    Change selected tab according to occured event
    '''
    # TODO: Raspberry Pi input으로 tab 결정
    if event.char == '1':
        tabs_control.select(clock_tab)
    elif event.char == '2':
        tabs_control.select(alarm_tab)
    elif event.char == '3':
        tabs_control.select(setting_tab)

# Set root window
app_window = tkinter.Tk()
app_window.title(TITLE)
app_window.geometry(pos())
app_window.resizable(True, True)
app_window.bind("<Key>", select_tab)
tkinter.Grid.rowconfigure(app_window, 0, weight=1)
tkinter.Grid.columnconfigure(app_window, 0, weight=1)

# Set tabs
tabs_control = tkinter.ttk.Notebook(app_window)

clock_tab = tkinter.Frame(tabs_control, background=BACKGROUND)
alarm_tab = tkinter.Frame(tabs_control, background=BACKGROUND)
setting_tab = tkinter.Frame(tabs_control, background=BACKGROUND)

clock_tab.grid(row=0, column=0, sticky=N+S+E+W)
alarm_tab.grid(row=0, column=0, sticky=N+S+E+W)
setting_tab.grid(row=0, column=0, sticky=N+S+E+W)

tabs_control.add(clock_tab, text="시계")
tabs_control.add(alarm_tab, text="알람")
tabs_control.add(setting_tab, text="설정")

tabs_control.pack(expand=True, fill="both")

# 1. 시계
font_list = [
    (FONT_FAMILY, H1_FONT_SIZE, H1_FONT_WEIGHT),
    (FONT_FAMILY, H2_FONT_SIZE, H2_FONT_WEIGHT),
    (FONT_FAMILY, H3_FONT_SIZE, H3_FONT_WEIGHT)]
label_list = []

# Make Widgets(time, date, year, season, ...)
# TODO: settings에 따라서 결정

for row_index in range(3):
    clock_tab.rowconfigure(row_index, weight=CLOCK_HEIGHT_RATE[row_index])
    for column_index in range(2):
        clock_tab.columnconfigure(column_index, weight=1)
        label_list.append(tkinter.Label(clock_tab, font=font_list[row_index], bg=BACKGROUND, state=NORMAL, disabledforeground=BACKGROUND))
        label_list[-1].grid(row=row_index, column=column_index, sticky=N+S+E+W)

# Fetch and Show time data
clock()

# 2. 알람



# 3. 설정
menu = ["날짜", "요일", "시간대", "시간", "연도", "계절"]
buttons = []
button_font = (FONT_FAMILY, H2_FONT_SIZE, H2_FONT_WEIGHT)

for row_index in range(SETTING_ROW_NUM):
    tkinter.Grid.rowconfigure(setting_tab, row_index, weight=1)
for col_index in range(SETTING_COLUNM_NUM):
    tkinter.Grid.columnconfigure(setting_tab, col_index, weight=1)

for i in range(len(menu)):
    buttons.append(tkinter.Label(setting_tab, text=menu[i], font=button_font, fg=FOREGROUND, bg=BACKGROUND))
    buttons[-1].grid(row=i//3, column=i%3, sticky=N+S+E+W)

# TODO: select 시 테두리 생기게 하는 거
# TODO: bind 함수로 enter 쳤을 때 normal/disabled 왔다갔다 하게 하기

# 화면 갱신될 때 얘는 어카냐?
app_window.mainloop()

# TODO: label state option으로 active/disabled 설정하여 이에 따라 자동으로 레이아웃 조정되도록...
# TODO: 알람 시/분 active color 지정.
# TODO: 스위치/버튼 제어 공부 -> 함수랑 binding
# TODO: Bind 함수 이용해서 스위치/버튼 제어할 수 있나?
# TODO: 일단 탭으로 구현해보고... 실제로는 탭 말고 input에 따라 함수 호출을 통한 "화면" 전환으로 가야할 듯