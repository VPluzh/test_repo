#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import RPi.GPIO as GPIO
import time
import numpy as np
import string

GPIO.setmode(GPIO.BCM)

LEDS=[26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(LEDS, GPIO.OUT)

def decToBinList(decNumber):
    binNumber1 = bin(decNumber)[2:]
    binNumber = list(string.zfill(binNumber1, 8))
    return binNumber

def num2dac(value):
    if value >255 or value < 0: 
        raise ValueError
    binNumber = decToBinList(value)
    for i in range(8):
        if binNumber[j] == '1' :
            GPIO.output(LEDS[j],1)
try:
    print("Введите число повторений:")
    repetitonsNumber = int(input())
    
    if repetitonsNumber < 0:
        raise ValueError
        
    for i in range(repetitionsNumber):
        for j in range(256):
            num2dac(j)
            timesleep(0.01)

except ValueError:
    print("Некорректное число")

finally:
GPIO.output(LEDS,0)   
GPIO.cleanup()

