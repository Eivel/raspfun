import RPi.GPIO as GPIO
import time, math
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
 
r_int = 100
g_int = 100
b_int = 100
 
r = GPIO.PWM(27, 60)
g = GPIO.PWM(18, 60)
b = GPIO.PWM(17, 60)
 
r.start(r_int)
g.start(g_int)
b.start(b_int)
 
sa = 0
 
for x in range(0, 1000):
        r_int = 90 * (math.sin(sa) + 1) / 2 + 10
        g_int = 80 * (math.sin(sa - 3.141592) + 1) / 2 + 20
        b_int = 100 * (math.sin(sa - 1.570796) + 1) / 2
        sa += 0.04
        r.ChangeDutyCycle(r_int)
        g.ChangeDutyCycle(g_int)
        b.ChangeDutyCycle(b_int)
        time.sleep(0.05)
time.sleep(2)
 
GPIO.cleanup()