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
menu_state = []

# TODO: 버저음은 따로 구현해야 됨

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

tabs_control.pack(expand=True, fill=BOTH)

# TODO: 알람 창은 어떻게 띄울까? -> 그냥 소리만 울리는 걸로...
# (대충 알람 체크하고 울리는 코드)

# 1. 시계
clock_font_list = [
    (FONT_FAMILY, H1_FONT_SIZE, H1_FONT_WEIGHT),
    (FONT_FAMILY, H2_FONT_SIZE, H2_FONT_WEIGHT),
    (FONT_FAMILY, H3_FONT_SIZE, H3_FONT_WEIGHT)]
label_list = []

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

    for i in range(len(label_list)):
        label_list[i].config(text = text_list[i])

    label_list[0].after(1000, clock)

def refresh_clock():
    for i in range(len(label_list)):
        label_list[i].config(state = menu_state[i])

# Make Widgets(time, date, year, season, ...)
# TODO: settings에 따라서 결정

for row_index in range(len(CLOCK_HEIGHT_RATE)):
    clock_tab.rowconfigure(row_index, weight=CLOCK_HEIGHT_RATE[row_index])
    for column_index in range(2):
        clock_tab.columnconfigure(column_index, weight=1)
        label_list.append(tkinter.Label(clock_tab, font=clock_font_list[row_index],
                                        fg=FOREGROUND, bg=BACKGROUND, state=NORMAL, disabledforeground=BACKGROUND))
        label_list[-1].grid(row=row_index, column=column_index, sticky=N+S+E+W)

# Fetch and Show time data
clock()

# 2. 알람
selected_alarm = 0
# TODO: 외부에 알람 시간 저장해두고 불러오기
alarm_time = []
alarm_state = []

# Set font style
alarm_title_font = (FONT_FAMILY, H3_FONT_SIZE, H3_FONT_WEIGHT)
alarm_time_font = (FONT_FAMILY, H1_FONT_SIZE, H1_FONT_WEIGHT)

def refresh_alarm():
    '''
    Reload and show updated alarm data
    '''
    global selected_alarm
    alarm_title_label.config(text = "알람 %d" % (selected_alarm+1))
    alarm_time_label.config(text = "%02d:%02d" % (alarm_time[selected_alarm].hour, alarm_time[selected_alarm].minute), state=alarm_state[selected_alarm])

def change_selected_alarm(event):
    '''
    Change selected alarm according to occured event
    '''
    global selected_alarm
    if event.keysym == "Left":
        selected_alarm = (selected_alarm-1)%3
    elif event.keysym == "Right":
        selected_alarm = (selected_alarm+1)%3
    refresh_alarm()

def change_alarm_state(event):
    '''
    Activate/Deactivate selected alarm
    '''
    alarm_state[selected_alarm] = NORMAL if alarm_state[selected_alarm] == DISABLED else DISABLED
    refresh_alarm()

def update_alarm(event):
    '''
    Set alarm time according to user's input
    '''
    global selected_alarm
    hour = alarm_time[selected_alarm].hour
    minute = alarm_time[selected_alarm].minute
    if event.keysym == "Up":
        hour = (hour+1) % 24
    elif event.keysym == "Down":
        minute = (minute+1) % 60
    alarm_time[selected_alarm] = datetime.time(hour, minute)
    refresh_alarm()

# Initialize alarm data
# TODO: 외부 데이터를 받아서 Initialize 하도록
for i in range(3):
    alarm_time.append(datetime.time(0, 0))
    alarm_state.append(DISABLED)

# Set grid
for row_index in range(len(ALARM_HEIGHT_RATE)):
    alarm_tab.rowconfigure(row_index, weight=ALARM_HEIGHT_RATE[row_index])
alarm_tab.columnconfigure(0, weight=1)

# Bind event functions - 알람 탭에 있는 경우만
app_window.bind("<Left>", change_selected_alarm)
app_window.bind("<Right>", change_selected_alarm)
app_window.bind("<Return>", change_alarm_state)
app_window.bind("<Up>", update_alarm)
app_window.bind("<Down>", update_alarm)

alarm_title_label = tkinter.Label(alarm_tab, text="알람 1", font=alarm_title_font, fg=FOREGROUND, bg=BACKGROUND, )
# TODO: 알람 활성화 여부를 텍스트로 보여줄 수 있으면 좋겠다
alarm_time_label = tkinter.Label(alarm_tab, text="%02d:%02d" % (alarm_time[0].hour, alarm_time[1].minute), font=alarm_time_font, fg=FOREGROUND, bg=BACKGROUND, state=alarm_state[0])

alarm_title_label.grid(row=0, column=0, sticky=N+S+E+W)
alarm_time_label.grid(row=1, column=0, sticky=N+S+E+W)

# 3. 설정
selected_button = 0
buttons = []

button_font = (FONT_FAMILY, H2_FONT_SIZE, H2_FONT_WEIGHT)

def refresh_button():
    for i in range(len(MENU)):
        buttons[i].config(state = menu_state[i])

def change_selected_button(event):
    print("1")
    global selected_button
    if event.keysym == "Left":
        selected_button = (selected_button-1)%len(MENU)
    elif event.keysym == "Right":
        selected_button = (selected_button+1)%len(MENU)

def change_button_state(event):
    menu_state[selected_button] = NORMAL if menu_state[selected_button] == DISABLED else DISABLED
    refresh_clock()
    refresh_button()

# Set grid
for row_index in range(SETTING_ROW_NUM):
    tkinter.Grid.rowconfigure(setting_tab, row_index, weight=1)
for col_index in range(SETTING_COLUNM_NUM):
    tkinter.Grid.columnconfigure(setting_tab, col_index, weight=1)

# Initialize button data
for i in range(len(MENU)):
    buttons.append(tkinter.Label(setting_tab, text=MENU[i], font=button_font, fg=FOREGROUND, bg=BACKGROUND))
    menu_state.append(NORMAL)
    buttons[-1].grid(row=i//3, column=i%3, sticky=N+S+E+W)

# TODO: select 시 테두리 생기게 하는 거
# TODO: bind 함수로 enter 쳤을 때 normal/disabled 왔다갔다 하게 하기
app_window.bind("<Left>", change_selected_button)
app_window.bind("<Right>", change_selected_button)
app_window.bind("<Return>", change_button_state)

# 화면 갱신될 때 얘는 어카냐?
app_window.mainloop()

# TODO: label state option으로 active/disabled 설정하여 이에 따라 자동으로 레이아웃 조정되도록...
# TODO: 알람 시/분 active color 지정.
# TODO: 스위치/버튼 제어 공부 -> 함수랑 binding
# TODO: Bind 함수 이용해서 스위치/버튼 제어할 수 있나?
# TODO: 일단 탭으로 구현해보고... 실제로는 탭 말고 input에 따라 함수 호출을 통한 "화면" 전환으로 가야할 듯

# TODO: 외부에 저장해야 하는 데이터
#       - 설정에서 포함/배제 하기로 결정한 위젯
#       - 알람 시간, 활성화 여부