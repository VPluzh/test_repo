#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import RPi.GPIO as GPIO
import time as TIME

import numpy as np
import matplotlib.pyplot as pyplot
import math
import scipy.io.wavfile as sc

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
            

            
try:
    rate, data = sc.read("file1.wav")
    
    length = data.shape[0] / rate
    channelsCount = data.shape[1]
    
    print("Channels:", channelsCount, "\n", "length:", length, )
    
    
    
except ValueError:
    print("Некорректное число")

finally:
GPIO.output(LEDS,0)   
GPIO.cleanup()

