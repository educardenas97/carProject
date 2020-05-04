from time import sleep 
import RPi.GPIO as GPIO
import time
import serial
import MySQLdb
l=0
# Open database connection
db = MySQLdb.connect("localhost","root","root","raspberry_pi3" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
read_ser=0
mis_codigo1=0
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(17, GPIO.IN)    # set GPIO17 as input (button)  

while True:
   #/////////////////////////////////////////
   sql = "SELECT mis_codigo FROM mision \
             WHERE mis_estado = '%s'" % (1)
   try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:
               mis_codigo1 = row[0]
               # Now print fetched result
               
   except:
         print "Error: unable to fecth data"

   #/////////////////Registro de los movimientos////////////////////////////
   # Iniciando conexión serial
   sql = "SELECT * FROM dispositivos \
          WHERE dis_codigo > '%s'" % (0)
   try:
      # Execute the SQL command
      cursor.execute(sql)
      # Fetch all the rows in a list of lists.
      results = cursor.fetchall()
      for row in results:
         dis_codigo = row[0]
         dis_descripcion = row[1]
         # Now print fetched result
         arduinoPort = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
         flagCharacter = 'k'
         a=(str(dis_codigo))
         arduinoPort.write(a)
         #Retardo para establecer la conexión serial
         arduinoPort.write(flagCharacter)
         getSerialValue = arduinoPort.readline()
         #getSerialValue = arduinoPort.read()
         #getSerialValue = arduinoPort.read(6)
         time.strftime("%y/%m/%d,%H:%M:%S")
         sql = "INSERT INTO historial_dispositivo(hid_dato,mis_codigo,hid_hora,dis_codigo) \
             VALUES ('%s','%s','%s','%s')" % \
         (getSerialValue,mis_codigo1,time.strftime("%y/%m/%d,%H:%M:%S"),dis_codigo)
         
         try:
            # Execute the SQL command
            cursor.execute(sql)
            print "php acepted"
            # Commit your changes in the database
            db.commit()
         except:
            # Rollback in case there is any error
            db.rollback()
            print "error"
   except:
         print "Error: unable to fecth data"
   #///////////////////////////////////////////////////////////////////////////
         
   #/////////////////////////////Inicio del escaneo///////////////////////////
   if(GPIO.input(17)):
      l=l+1
      
        
      # Iniciando conexión serial
      sql = "SELECT * FROM sensor_mision \
             WHERE mis_codigo = '%s'" % (mis_codigo1)
      try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:
               mis_codigo = row[0]
               sen_codigo = row[1]
               # Now print fetched result
               print "mis_codigo=%s sen_codigo=%s" % \
                      (mis_codigo, sen_codigo)
              
               
               arduinoPort = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
               flagCharacter = 'k'
               a=(str(sen_codigo))
               arduinoPort.write(a)
               #Retardo para establecer la conexión serial
               arduinoPort.write(flagCharacter)
               getSerialValue = arduinoPort.readline()
               #getSerialValue = arduinoPort.read()
               #getSerialValue = arduinoPort.read(6)
               print '\nSerial: %s' % (getSerialValue)
               time.strftime("%y/%m/%d,%H:%M:%S")
               print time.strftime("%y-%m-%d %H:%M:%S")
               sql = "INSERT INTO historial(his_dato,his_hora,mis_codigo,sen_codigo) \
               VALUES ('%s','%s','%s','%s')" % \
               (getSerialValue,time.strftime("%y/%m/%d,%H:%M:%S"),mis_codigo,sen_codigo)
               try:
                  l=l+1
                   # Execute the SQL command
                  cursor.execute(sql)
                  print "-"
                  # Commit your changes in the database
                  db.commit()
               except:
                   # Rollback in case there is any error
                   db.rollback()
                   print "error"
             
               
      except:
         print "Error: unable to fecth data"
   #/////////////////////////////////////////////////////////////////////////////////
         
            
               
      

# disconnect from server
db.close()
