#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import datetime
import tkinter
import tkinter.ttk
from tkinter.constants import *
from time import sleep
from setting import *
from pyRPiRTC import *

# TODO: mode 변수 값에 따라 스크린 전환하는 쪽으로...
mode = 0

# TODO: 시작할 때 외부 파일 읽어서 menu_state 결정되도록.
menu_state = []

Button_input = {
    GPIO_NEXT : 1,
    GPIO_ALARM : 1,
    GPIO_SELECT : 1
}

def pos(width=WIDTH, height=HEIGHT, x=X, y=Y):
    '''
    Return string showing position of root window
    '''
    return "x".join([str(width), "+".join([str(height), str(x), str(y)])]) 

def select_tab(event):
    '''
    Change selected tab according to occured event
    '''
    if type(event) == int:
        if event == 0:
            tabs_control.select(clock_tab)
        elif event == 1:
            tabs_control.select(alarm_tab)
        elif event == 2:
            tabs_control.select(setting_tab)
    else:
        if event.char == '1':
            tabs_control.select(clock_tab)
        elif event.char == '2':
            tabs_control.select(alarm_tab)
        elif event.char == '3':
            tabs_control.select(setting_tab)


# GPIO setting
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_NEXT, GPIO.IN)
GPIO.setup(GPIO_ALARM, GPIO.IN)
GPIO.setup(GPIO_SELECT, GPIO.IN)

GPIO.setup(GPIO_TAB_PREV, GPIO.IN)
GPIO.setup(GPIO_TAB_NEXT, GPIO.IN)

GPIO.setup(GPIO_BUZZER, GPIO.OUT)


# Make datetime object from RTC module
real_time = DS1302()

# Initialize RTC time
real_time.write_datetime(datetime.datetime.now())

# Set root window
app_window = tkinter.Tk()
app_window.title(TITLE)
app_window.geometry(pos())
app_window.resizable(True, True)
app_window.rowconfigure(0, weight=1)
app_window.columnconfigure(0, weight=1)

# tab paging with key(button)
# app_window.bind("<Key>", select_tab)

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

# 1. 시계
clock_font_list = [H1_FONT, H2_FONT, H3_FONT]
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

def initialize_clock():
    '''
    Initialize clock tab
    '''
    global label_list
    for widget in clock_tab.winfo_children():
        widget.destroy()

    # 'label_list' should be initialized whenever this function is called
    # because destroyed objects still remain in this list
    label_list = []
    for _ in range(6):
        menu_state.append(NORMAL)
        label_list.append(tkinter.Label(
            clock_tab,
            fg=FOREGROUND,
            bg=BACKGROUND,
            disabledforeground=BACKGROUND
            ))

def clock(blink_state):
    '''
    Fetch time data using 'datatime' module
    and with this data, Set text of labels in clock tab
    Return value is time(24 hour)
    '''
    date_time = str(real_time.read_datetime())
    wday = WEEKDAY[real_time.read_datetime().weekday()]

    temp_date, temp_time = date_time.split()
    year, month, day = temp_date.split('-')
    year += "년"
    season = get_season(int(month))
    date = '/'.join([month, day])

    hour, minute = temp_time.split(':')[:-1]
    part = get_part(int(hour))

    ret = datetime.time(int(hour), int(minute))
    
    if int(hour) > 12 and int(hour) < 24:
        hour = str(int(hour) - 12)
        if len(hour) == 1:
            hour = '0' + hour
    time = (':' if blink_state else ' ').join([hour, minute])
    
    text_list = [date, wday, part, time, year, season]

    for i in range(len(label_list)):
        label_list[i].config(text = text_list[i])

    return ret
    
def refresh_clock():
    initialize_clock()

    # Count rows and columns
    row_count = 0
    column_count = [0, 0, 0]
    for i in range(len(MENU)):
        if menu_state[i] == NORMAL:
            column_count[i//2] += 1
        if i % 2 == 1 and column_count[i//2]:
            row_count += 1

    # Refresh Widgets(time, date, year, season, ...)
    for i in range(3):
        for j in range(2):
            label_list[i*2+j].config(
                font = clock_font_list[i if row_count == 3 else 1],
                state = menu_state[i*2+j]
                )

    for j in range(2):
        clock_tab.columnconfigure(j, weight=1)
    for i in range(row_count):
        clock_tab.rowconfigure(i, weight=CLOCK_HEIGHT_RATE[row_count][i])
    
    # Edit grid
    row_index = 0
    for i in range(3):
        if column_count[i]:
            column_index = 0
            for j in range(2):
                if menu_state[i*2+j] == NORMAL:
                    label_list[i*2+j].grid(
                        row=row_index,
                        column=column_index,
                        columnspan=(2 if column_count[i] == 1 else 1),
                        sticky=N+S+E+W
                        )
                    column_index += 1
            row_index += 1


# Set grid and Make widgets
refresh_clock()


# 2. 알람
selected_alarm = 0
alarm_time = []
alarm_state = []
# 0 - DISABLED / 1 - NORMAL(시 조정 가능) / 2 - NORMAL(분 조정 가능)
alarm_mode = []

# Set font style
alarm_title_font = H3_FONT
alarm_time_font = H1_FONT

def check_alarm(now):
    # Turn on/off alarm
    flag = False
    for i in range(len(alarm_time)):
        if alarm_state[i] == NORMAL and alarm_time[i] == now:
            flag = True
    return flag

def refresh_alarm():
    '''
    Reload and show updated alarm data
    '''
    global selected_alarm
    alarm_title_label.config(text = "알람 %d" % (selected_alarm+1))
    alarm_text = TIME_PART[alarm_time[selected_alarm].strftime("%p")]
    alarm_text = ' '.join([alarm_text, alarm_time[selected_alarm].strftime("%I:%M")])
    alarm_time_label.config(text = alarm_text, state = alarm_state[selected_alarm])

def change_selected_alarm(event = None):
    '''
    Change selected alarm according to occured event
    '''
    global selected_alarm
    if event:
        if (event.keysym == "Left"):
            selected_alarm = (selected_alarm-1)%ALARM_COUNT
        elif (event.keysym == "Right"):
            selected_alarm = (selected_alarm+1)%ALARM_COUNT
    else:
        selected_alarm = (selected_alarm+1)%ALARM_COUNT
    refresh_alarm()

def change_alarm_state(event = None):
    '''
    Activate/Deactivate selected alarm
    '''
    alarm_mode[selected_alarm] += 1
    alarm_mode[selected_alarm] %= 3
    alarm_state[selected_alarm] = DISABLED if alarm_mode[selected_alarm] == 0 else NORMAL
    refresh_alarm()

def update_alarm(event = None):
    '''
    Set alarm time according to user's input
    '''
    global selected_alarm
    hour = alarm_time[selected_alarm].hour
    minute = alarm_time[selected_alarm].minute
    if event:
        if (event.keysym == "Up"):
            hour = (hour+1) % 24
        elif (event.keysym == "Down"):
            minute = (minute+1) % 60
    else:
        if alarm_mode[selected_alarm] == 1:
            hour = (hour+1) % 24
        elif alarm_mode[selected_alarm] == 2:
            minute = (minute+1) % 60

    alarm_time[selected_alarm] = datetime.time(hour, minute)
    refresh_alarm()

# Initialize alarm data
# TODO: 외부 데이터를 받아서 Initialize 하도록
for i in range(ALARM_COUNT):
<<<<<<< HEAD
    alarm_time.append(datetime.time(0, 0))
    alarm_state.append(DISABLED)
    alarm_mode.append(1)
=======
    alarm_time.append(datetime.time(14, 54))
    alarm_state.append(NORMAL)
    alarm_state.append(1)
>>>>>>> 15ea38904e5d61723ba12ff0fde494aff0f4711c

# Set grid
for row_index in range(len(ALARM_HEIGHT_RATE)):
    alarm_tab.rowconfigure(row_index, weight=ALARM_HEIGHT_RATE[row_index])
alarm_tab.columnconfigure(0, weight=1)

# TODO: 알람 활성화 여부를 텍스트로 보여줄 수 있으면 좋겠다
alarm_title_label = tkinter.Label(alarm_tab, font=alarm_title_font, fg=FOREGROUND, bg=BACKGROUND)
alarm_time_label = tkinter.Label(alarm_tab, font=alarm_time_font, fg=FOREGROUND, bg=BACKGROUND)
refresh_alarm()

alarm_title_label.grid(row=0, column=0, sticky=N+S+E+W)
alarm_time_label.grid(row=1, column=0, sticky=N+S+E+W)

# 3. 설정
selected_button = 0
buttons = []
borders = []

button_font = H2_FONT

def refresh_button():
    for i in range(len(MENU)):
        buttons[i].config(state = menu_state[i])

def change_selected_button(event = None):
    global selected_button
    borders[selected_button].config(state=NORMAL)
    if event:
        if (event.keysym == "Left"):
            selected_button = (selected_button-1)%len(MENU)
        elif (event.keysym == "Right"):
            selected_button = (selected_button+1)%len(MENU)
    else:
<<<<<<< HEAD
        selected_button = (selected_button+1)%len(MENU)
=======
        selected_button = (selected_button+1)%len(MENU)s
>>>>>>> 15ea38904e5d61723ba12ff0fde494aff0f4711c
    borders[selected_button].config(state=ACTIVE)

def change_button_state(event = None):
    menu_state[selected_button] = NORMAL if menu_state[selected_button] == DISABLED else DISABLED
    refresh_clock()
    refresh_button()

# Set grid
for row_index in range(SETTING_ROW_NUM):
    setting_tab.rowconfigure(row_index, weight=1)
for col_index in range(SETTING_COLUNM_NUM):
    setting_tab.columnconfigure(col_index, weight=1)

# Initialize button data
for i in range(len(MENU)):
    borders.append(tkinter.Label(
        setting_tab,
        bg=BACKGROUND,
        activebackground=FOREGROUND,
        state=(ACTIVE if i == selected_button else NORMAL)
    ))
    borders[-1].rowconfigure(0, weight=1)
    borders[-1].columnconfigure(0, weight=1)
    buttons.append(tkinter.Label(
        borders[-1],
        text=MENU[i],
        font=button_font,
        fg=FOREGROUND,
        bg=BACKGROUND,
        disabledforeground=DISABLED_FG
    ))
    borders[-1].grid(row=i//SETTING_COLUNM_NUM, column=i%SETTING_COLUNM_NUM, sticky=N+S+E+W)
    buttons[-1].grid(row=0, column=0, sticky=N+S+E+W, padx=SELECT_BORDERWIDTH, pady=SELECT_BORDERWIDTH)

app_window.update()

# Represent n
# (time after program started: about m X 100ms, n == m % 10)
time_cnt = 0

# Represent whether any button has been pressed (for judging to turn on/off alarm)
pressed = False

current_tab = 0

# Mainloop
try:
    while True:
        # Fetch and Show time data(span: 500ms)
        if time_cnt % 5 == 0:
            now_time = clock(time_cnt // 5)
        
        # Turn on/off alarm
        if check_alarm(now_time):
            alarm_flag = True
        else:
            pressed = False
            alarm_flag = False
        
        # Get GPIO button input
        for pin in Button_input.keys():
            Button_input[pin] = GPIO.input(pin)
            if Button_input[pin] == 0: # if pressed
                pressed = True
                
        # Get GPIO tab select input
        if GPIO.input(GPIO_TAB_PREV) == 0:
            current_tab = (current_tab-1)%3
        elif GPIO.input(GPIO_TAB_NEXT) == 0:
            current_tab = (current_tab+1)%3
        
        if tabs_control.index('current') != current_tab:
            select_tab(current_tab)
        '''
        # Get keyboard tab select input
        current_tab = tabs_control.index('current')
        '''

        # if alarm is ringing and button was just pressed
        if pressed and alarm_flag:
            alarm_flag = False
        
        if current_tab == 1: # 알람
            # button should be recognized in each function
            # and parameter of functions should be removed
            if Button_input[GPIO_NEXT] == 0:
                change_selected_alarm()
            elif Button_input[GPIO_SELECT] == 0:
                change_alarm_state()
            elif Button_input[GPIO_ALARM] == 0:
<<<<<<< HEAD
                if alarm_state[selected_alarm] == NORMAL:
=======
                if alarm_state[select_tab] == NORMAL:
>>>>>>> 15ea38904e5d61723ba12ff0fde494aff0f4711c
                    update_alarm()

            '''
            # Bind event functions - only if current tab is alarm one
            app_window.bind("<Left>", change_selected_alarm)
            app_window.bind("<Right>", change_selected_alarm)
            app_window.bind("<Return>", change_alarm_state)
            if alarm_state[selected_alarm] == NORMAL:
                app_window.bind("<Up>", update_alarm)
                app_window.bind("<Down>", update_alarm)
            '''

        elif current_tab == 2: # setting
            # button should be recognized in each function
            # and parameter of functions should be removed
            if Button_input[GPIO_NEXT] == 0:
                change_selected_button()
            elif Button_input[GPIO_SELECT] == 0:
                change_button_state()
            
            '''
            app_window.bind("<Left>", change_selected_button)
            app_window.bind("<Right>", change_selected_button)
            app_window.bind("<Return>", change_button_state)
            app_window.unbind("<Up>")
            app_window.unbind("<Down>")
            '''
        '''
        else:
            app_window.unbind("<Left>")
            app_window.unbind("<Right>")
            app_window.unbind("<Return>")
            app_window.unbind("<Up>")
            app_window.unbind("<Down>")
        '''

        app_window.update()
        time_cnt += 1
        time_cnt %= 10

        GPIO.output(GPIO_BUZZER, GPIO.HIGH if alarm_flag and time_cnt < 5 else GPIO.LOW)
        sleep(.1)
finally:
    GPIO.cleanup()


# TODO: 일단 탭으로 구현해보고... 실제로는 탭 말고 input에 따라 함수 호출을 통한 "화면" 전환으로 가야할 듯

# TODO: 외부에 저장해야 하는 데이터
#       - 설정에서 포함/배제 하기로 결정한 위젯
#       - 알람 시간, 활성화 여부