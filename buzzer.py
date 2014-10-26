__author__ = 'Wojciech'
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

'''
    p = GPIO.PWM(18,524)
    p.start(1)
    time.sleep(1)
    p.stop()

    p = GPIO.PWM(18,587)
    p.start(1)
    time.sleep(1)
    p.stop()

    p = GPIO.PWM(18,662)
    p.start(1)
    time.sleep(1)
    p.stop()

    p = GPIO.PWM(18,701)
    p.start(1)
    time.sleep(1)
    p.stop()

    p = GPIO.PWM(18,787)
    p.start(1)
    time.sleep(1)
    p.stop()

    p = GPIO.PWM(18,878)
    p.start(1)
    time.sleep(1)
    p.stop()

    p = GPIO.PWM(18,1004)
    p.start(1)
    time.sleep(1)
    p.stop()


    p = GPIO.PWM(18,1048)
    p.start(1)
    time.sleep(5)
    p.stop()
'''






'''
    p = GPIO.PWM(18,523.25)
    p.start(1)
    time.sleep(.15)
    p.stop()
    time.sleep(.10)
    p = GPIO.PWM(18,523.25)
    p.start(1)
    time.sleep(.15)
    p.stop()
    time.sleep(.1)

    p = GPIO.PWM(18,466.16)
    p.start(1)
    time.sleep(.1)
    p.stop()

    p = GPIO.PWM(18,523.25)
    p.start(1)
    time.sleep(.15)
    p.stop()
    time.sleep(.1)
    p = GPIO.PWM(18,622.25)
    p.start(1)
    time.sleep(.20)
    p.stop()
    time.sleep(.1)
    p = GPIO.PWM(18,523.25)
    p.start(1)
    time.sleep(.15)
    p.stop()
'''

try:
    p = GPIO.PWM(18,739.99)
    p.start(10)
    time.sleep(.25)
    p.stop()

    p = GPIO.PWM(18,880)
    p.start(10)
    time.sleep(.25)
    p.stop()

    p = GPIO.PWM(18,739.99)
    p.start(10)
    time.sleep(.25)
    p.stop()

    p = GPIO.PWM(18,659.25)
    p.start(10)
    time.sleep(.5)
    p.stop()

    p = GPIO.PWM(18,880)
    p.start(10)
    time.sleep(.75)
    p.stop()

    p = GPIO.PWM(18,587.33)
    p.start(10)
    time.sleep(.25)
    p.stop()

    p = GPIO.PWM(18,659.25)
    p.start(10)
    time.sleep(.25)
    p.stop()


    p = GPIO.PWM(18,587.33)
    p.start(10)
    time.sleep(.25)
    p.stop()

    p = GPIO.PWM(18,554.37)
    p.start(10)
    time.sleep(.5)
    p.stop()

    p = GPIO.PWM(18,440)
    p.start(10)
    time.sleep(.75)
    p.stop()

    GPIO.cleanup()
except KeyboardInterrupt:
    GPIO.cleanup()