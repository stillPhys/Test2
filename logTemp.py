import time
import socket
import MySQLdb
#import databaseUser, databasePassword, addrSensorTest
#from personalData.py
from personalData import *

# Open database connection
db = MySQLdb.connect("localhost", databaseUser, databasePassword,"temperature_log")
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Fetch a single row using fetchone() method.
#data = cursor.fetchone()

def writeValue():
	sock = socket.socket()
	sock.connect((addrSensorTest, 8080))
	sock.send('t')
	data = sock.recv(16)
	sock.close()

	s = "INSERT INTO  sensor_test (time, temperature) VALUES (NOW(), '" + data + "');"
	# execute SQL query using execute() method.
	try:
		cursor.execute(s)
		db.commit()
	except:
		db.rollback()
	print(s)
	print(cursor.fetchall())

try:
	while True:
		writeValue()
		time.sleep(10)
except Exception as e:
	print(e)

db.close()
