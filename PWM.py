#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

GPIO.setmode(GPIO.BCM)

LEDS=[24, 25, 8, 7, 12, 16, 20, 21]

GPIO.setup(LEDS, GPIO.OUT)


p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()

GPIO.output(LEDS,0)   

time.sleep(2)

GPIO.cleanup()

