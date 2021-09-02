from enum import Enum

# Title of program
TITLE = "Clock for Dementia patient"

# Size of window(unit: pixel)
WIDTH = 585
HEIGHT = 325

# Initial position of window in the screen
# (0, 0) is recommended because this application is designed to be full-screen
X = 0
Y = 0

# Name of each tap
TAB_NAME = ["시계", "알람", "설정"]

# Font family
FONT_FAMILY = "Yu Gothic"

# Font setting(Specific)
# Means of H1, H2, H3, ... are similar to ones in HTML
H1_FONT = (FONT_FAMILY, 68, "bold")
H2_FONT = (FONT_FAMILY, 50, "bold")
H3_FONT = (FONT_FAMILY, 30, "bold")

# BG, FG of Clock
BACKGROUND = "#000000"
FOREGROUND = "#ffffff"

# Color of Font in clock menu when disabled
DISABLED_FG = "#444444"

# This decides the height rate of each element in clock tab
# because the number of rows is variable in clock tab, there are 4 list(for 0~3 rows) in this constant
CLOCK_HEIGHT_RATE = [[], [1], [1, 1], [5, 3, 2]]

# This decides how many alarms are available to set
ALARM_COUNT = 3

# This decides the height rate of each element in alarm tab
ALARM_HEIGHT_RATE = [3, 7]

# These constants decide the number of rows and columns of setting tab
SETTING_ROW_NUM = 2
SETTING_COLUNM_NUM = 3

# Borderwidth when a menu is selected in setting tab
SELECT_BORDERWIDTH = 8

# Constants needed to represent clock in Korean
WEEKDAY = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
MENU = ["날짜", "요일", "시간대", "시간", "연도", "계절"]
TIME_PART = {"AM": "오전", "PM": "오후"}

# GPIO input/output
GPIO_LEFT = 23
GPIO_RIGHT = 32
GPIO_HOUR = 33
GPIO_MINUTE = 35
GPIO_SELECT = 36

GPIO_CLOCK = 40
GPIO_ALARM = 38
GPIO_SETTING = 37

GPIO_TAB_LIST = [GPIO_CLOCK, GPIO_ALARM, GPIO_SETTING]

GPIO_BUZZER = 21
