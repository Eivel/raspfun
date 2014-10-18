__author__ = 'Wojciech'
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def button_pushed(channel):
    GPIO.output(18,1)

def button_released(channel):
    GPIO.output(18,0)

GPIO.add_event_detect(21, GPIO.RISING, callback=button_pushed, bouncetime=300)
GPIO.add_event_detect(16, GPIO.FALLING, callback=button_released, bouncetime=300)

time.sleep(10)
GPIO.cleanup()