
#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","raspberry_pi3" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
s = raw_input("Ingrese sensor")
# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO dispositivos(dis_descripcion) \
       VALUES ('%s')" % \
      (s)
try:
   # Execute the SQL command
   cursor.execute(sql)
   print "ok"
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
   print "error"
# disconnect from server
db.close()
