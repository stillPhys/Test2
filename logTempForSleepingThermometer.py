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

connected = 0
while(connected == 0):
	try:
		sock = socket.socket()
		sock.bind(('', 8080))
		sock.listen(16)
		connected = 1
	except Exception as e:
		print(e)
		time.sleep(1)

def writeValue(data):
	s = "INSERT INTO  sensor_test (time, temperature) VALUES (NOW(), '" + data + "');"
	# execute SQL query using execute() method.
	try:
		cursor.execute(s)
		db.commit()
	except:
		db.rollback()
	print(s)
	print 'answer:', cursor.fetchall(), '\n'

try:
	while True:
		conn, addr = sock.accept()
		print 'connected:', addr, time.asctime()
		data = conn.recv(16)
		writeValue(data)
except Exception as e:
	print(e)

sock.close()
db.close()
