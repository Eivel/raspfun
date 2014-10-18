__author__ = 'Wojciech'
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if(GPIO.input(16) == 1):
        print("Button pressed")