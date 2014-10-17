import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

is_high = False

while True:
    if(GPIO.input(12) == False):
        print("Button pressed")
        os.system('date')
        print GPIO.input(12)
        if(is_high):
            GPIO.output(17,GPIO.LOW)
            is_high=False
        else:
            GPIO.output(17,GPIO.HIGH)
            is_high=True
        time.sleep(1)

    else:
        os.system('clear')
        print("Waiting for you to press a button")

time.sleep(1)
            
