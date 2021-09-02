import RPi.GPIO as GPIO
from time import sleep
from setting import *

outp = GPIO_BUZZER
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outp, GPIO.OUT)

time_cnt = 0
try:
    while True:
        GPIO.output(outp, GPIO.HIGH)
        sleep(.1)
        GPIO.output(outp, GPIO.LOW)
        sleep(.1)
finally:
    GPIO.cleanup()


'''
#-*- coding:utf-8 -*-
from gpiozero import Buzzer
import RPi.GPIO as GPIO
from time import sleep

inp = 22
inp2 = 23
outp = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inp, GPIO.IN)
GPIO.setup(inp2, GPIO.IN)
GPIO.setup(outp, GPIO.OUT)

def buzz(port):
	GPIO.output(port, 0)
	sleep(.5)
	GPIO.output(port, 1)
	sleep(.5)

time_cnt = 0

try:
    while 1:
        if time_cnt < 5:
            GPIO.output(outp, 0)
            sleep(.1)
        else:
            GPIO.output(outp, 1)
            sleep(.1)
        button = GPIO.input(inp)
        button2 = GPIO.input(inp2)
        print("22: %d | 15: %d" % (button, button2))
        time_cnt += 1
        time_cnt %= 10
finally:
    GPIO.cleanup()
'''

'''
    내부 pull up / pull down 문제 있음...    
'''

'''
import tkinter as tk 
import RPi.GPIO as GPIO
from time import sleep

GPIO21 = 21
GPIO20 = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO21, GPIO.OUT)
GPIO.setup(GPIO20, GPIO.OUT)

master = tk.Tk()
master.title("GPIO Control")
master.geometry("300x100")

GPIO21_state = True
GPIO20_State = True

def GPIO21button():
	global GPIO21_state
	if GPIO21_state == True:
		GPIO.output(GPIO21, GPIO21_state)
		GPIO21_state = False
		ONlabel = tk.Label(master, text="Turned ON", fg="green")
		ONlabel.grid(row=0, column=1)
	else:
		GPIO.output(GPIO21, GPIO21_state)
		GPIO21_state = True
		ONlabel = tk.Label(master, text="Turned OFF", fg="red")
		ONlabel.grid(row=0, column=1)


def GPIO20button():
	global GPIO20_State
	if GPIO20_State == True:
		GPIO.output(GPIO20, GPIO20_State)
		GPIO20_State = False
		OFFlabel = tk.Label(master, text="Turned ON", fg="green")
		OFFlabel.grid(row=1, column=1)
	else:
		GPIO.output(GPIO20, GPIO20_State)
		GPIO20_State = True
		OFFlabel = tk.Label(master, text="Turned OFF", fg="red")
		OFFlabel.grid(row=1, column=1)

ONbutton = tk.Button(master, text="GPIO 21", bg="blue", command=GPIO21button)
ONbutton.grid(row=0, column=0)

OFFbutton = tk.Button(master, text="GPIO 20",bg="blue" , command=GPIO20button)
OFFbutton.grid(row=1, column=0)

Exitbutton = tk.Button(master, text="Exit",bg="red", command=master.destroy)
Exitbutton.grid(row=2, column=0)
master.mainloop()
'''
