#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import RPi.GPIO as GPIO
import time as TIME

import numpy as np
import matplotlib.pyplot as pyplot
import math

time = int(input("time:"))
frequency = int(input("frequency:"))
samplingFrequency = int(input("samplingFrequency:"))

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
            
# ndarray = numpy.sin(numpy.arrange(0, time, 1/samplingFrequency))      
            
try:
    ndarray = []
    
    t = 0
    while t < time:
        ndarray.append(128 + 127*math.sin(2*math.pi*frequency*t))
        t += 1/samplingFrequency
        
    pyplot.plot(ndarray)
    pyplot.show()
    
    if input("Continue?(no if no)") != 'no':
        
        ndarray = list(map(math.trunc, ndarray)) 
        
        for value in ndarray:
            num2dac(value)
            TIME.sleep(1/samplingFrequency)
            
        num2dac(0)
    
except ValueError:
    print("Некорректное число")

finally:
GPIO.output(LEDS,0)   
GPIO.cleanup()

