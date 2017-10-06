import matplotlib.pyplot as plt
import MySQLdb
#import databaseUser, databasePassword, addrSensorTest
#from personalData.py
from personalData import *

def getAllTemps():
	db = MySQLdb.connect("localhost", databaseUser, databasePassword, "temperature_log")
	cursor = db.cursor()
	cursor.execute("SELECT * FROM sensor_test")
	res = cursor.fetchall()
	db.close()
	return res

temperatures = getAllTemps()
time = []
temp = []
for i in temperatures:
	time.append(i[0])
	temp.append(i[1])
plt.plot(time, temp)
plt.show()
