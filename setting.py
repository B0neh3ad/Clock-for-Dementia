from enum import Enum

# Title of program
TITLE = "Clock for Dementia patient"

# Size of window(unit: pixel)
WIDTH = 585
HEIGHT = 325

# Initial position of window in the screen
X = 0
Y = 0

TAB_NAME = ["시계", "알람", "설정"]

# Font family
FONT_FAMILY = "Yu Gothic"

H1_FONT = (FONT_FAMILY, 68, "bold")
H2_FONT = (FONT_FAMILY, 50, "bold")
H3_FONT = (FONT_FAMILY, 30, "bold")

BACKGROUND = "#000000"
FOREGROUND = "#ffffff"
DISABLED_FG = "#444444"
BORDER_WIDTH = 25

CLOCK_HEIGHT_RATE = [[], [1], [1, 1], [5, 3, 2]]
ALARM_HEIGHT_RATE = [3, 7]

SETTING_ROW_NUM = 2
SETTING_COLUNM_NUM = 3

SELECT_BORDERWIDTH = 8

WEEKDAY = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

MENU = ["날짜", "요일", "시간대", "시간", "연도", "계절"]

# GPIO input/output
GPIO_LEFT = 0
GPIO_RIGHT = 0
GPIO_HOUR = 0
GPIO_MINUTE = 0
GPIO_SELECT = 0

GPIO_CLOCK = 0
GPIO_ALARM = 0
GPIO_SETTING = 0

GPIO_TAB_LIST = [GPIO_CLOCK, GPIO_ALARM, GPIO_SETTING]

GPIO_BUZZER = 0
