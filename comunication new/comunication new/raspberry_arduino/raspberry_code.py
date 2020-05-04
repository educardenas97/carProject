import RPi.GPIO as GPIO
from time import sleep 
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(17, GPIO.IN)    # set GPIO17 as input (button)  
try:  
    while True:   
        if GPIO.input(17): # if port 25 == 1  
            print "Scan on"
        sleep(0.1)
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  
