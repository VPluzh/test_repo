#!/usr/bin/env python
# coding: utf-8

# In[1]:


import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BCM)

LEDS=[24, 25, 8, 7, 12, 16, 20, 21]

GPIO.setup(LEDS, GPIO.OUT)

def decToBinList(decNumber):
    binNumber0 = bin(decNumber)[2:]
    size = len(binNumber0)
    binNumber = list(binNumber0)

    binNumber = map(int, binNumber)

    a = np.zeros(8-size, dtype=int)

    return joined = np.concatenate((a, binNumber), axis=None)
    
def lightNumber(number):
    joined = decToBinList(number)
    for i in range(8):
        if joined[j] == 1:
            GPIO.output(LEDS[j],1)
            time.sleep(2)
            
GPIO.output(LEDS,0)           
GPIO.cleanup()


# In[ ]:




