import serial
arduinoPort = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

getSerialValue = arduinoPort.readline()
print '\nSerial: %s' % (getSerialValue)
