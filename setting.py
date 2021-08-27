from enum import Enum

# Title of program
TITLE = "Clock for Dementia patient"

# Size of window(unit: pixel)
WIDTH = 585
HEIGHT = 325

# Initial position of window in the screen
X = 0
Y = 0

# Font family
FONT_FAMILY = "Yu Gothic"

# Font size
H1_FONT_SIZE = 68
H2_FONT_SIZE = 50
H3_FONT_SIZE = 30

# Font style: "normal" or "blue"
H1_FONT_WEIGHT = "bold"
H2_FONT_WEIGHT = "bold"
H3_FONT_WEIGHT = "bold"

TOP_FONT = ("Yu Gothic", 60, 'bold')
CENTER_FONT = ("Yu Gothic", 50, 'bold')
BOTTOM_FONT = ("Yu Gothic", 30, 'bold')

BACKGROUND = "#000000"
FOREGROUND = "#ffffff"
BORDER_WIDTH = 25

CLOCK_HEIGHT_RATE = [5, 3, 2]

TOP_FRAME_HEIGHT = 5
CENTER_FRAME_HEIGHT = 3
BOTTOM_FRAME_HEIGHT = 2

SETTING_ROW_NUM = 2
SETTING_COLUNM_NUM = 3

WEEKDAY = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

class State(Enum):
    DATE_STATE = 0
    WDAY_STATE = 1
    PART_STATE = 2
    TIME_STATE = 3
    YEAR_STATE = 4
    SEASON_STATE = 5