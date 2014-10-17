import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

while True:
    if(GPIO.input(12) == False):
        print("Button pressed")
        os.system('date')
        print GPIO.input(12)
        time.sleep(5)

    else:
        os.system('clear')
        print("Waiting for you to press a button")

time.sleep(1)
            
