import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","raspberry_pi3" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Iniciando conexión serial

sql = "SELECT * FROM mision \
       WHERE mis_estado = '%d'" % (1)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      mis_codigo = row[0]
      # Now print fetched result
      print "mis_codigo=%s" % \
             (mis_codigo)
      
except:
   print "Error: unable to fecth data"
