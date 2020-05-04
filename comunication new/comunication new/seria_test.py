import serial
import time
ser = serial.Serial('/dev/ttyACM0',9600)
s=0
while True:
	read_serial=ser.readline()
	s = (ser.readline(),20)
	print read_serial

