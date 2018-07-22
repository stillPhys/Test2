import matplotlib.pyplot as plt
import MySQLdb
#import databaseUser, databasePassword, addrSensorTest
#from personalData.py
from personalData import *

def request(s):
	db = MySQLdb.connect("localhost", databaseUser, databasePassword, "temperature_log")
	cursor = db.cursor()
	cursor.execute(s)
	res = cursor.fetchall()
	db.close()
	return res

def getAllTemps():
	return request("SELECT * FROM sensor_test")

def getLastDayTemps():
	return request("SELECT * FROM sensor_test WHERE time >= DATE_SUB(NOW(),INTERVAL 1 day)")

temperatures = getLastDayTemps()
time = []
temp = []
averageTemp = 0
for i in temperatures:
	time.append(i[0])
	temp.append(i[1])
	averageTemp += i[1]
ppd = len(temperatures)
if (ppd > 0):
	averageTemp /= ppd
	print "points per day: ", ppd
	print "lost: ", (1-float(ppd)/(24*30))*100, "%"
	print "average: ", averageTemp
	plt.plot(time, temp)
	plt.show()
else:
	print ("There is no points today!")
