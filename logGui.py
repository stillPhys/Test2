import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

#Python 2 and 3 compatible!
import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

import MySQLdb
import gc

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

def updatePlot():
	temperatures = getAllTemps()
	time = []
	temp = []
	for i in temperatures:
		time.append(i[0])
		temp.append(i[1])
	plt.plot(time, temp, 'b-')
	gc.collect()
	

#It can be usefull!
def destroy(e):
	sys.exit()

root = Tk.Tk()
root.wm_title("Temperature")

fig = plt.figure(1)
#plt.ion()
updatePlot()

canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()

def updateCanvasWithPlot():
	plt.ion
	updatePlot()    
	fig.canvas.draw()
	plt.ioff

def updateTimer():
	try:
		updateCanvasWithPlot()
		root.after(60, updateTimer)
	except Exception as e:
		print (e)

plot_widget.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

frameButtons = Tk.Frame(root)
frameButtons.pack(side = Tk.BOTTOM)
buttonUpdate = Tk.Button(master = frameButtons, text='Update', command=updateCanvasWithPlot)
buttonUpdate.pack(side = Tk.LEFT)
buttonQuit = Tk.Button(master = frameButtons, text='Quit', command=sys.exit)
buttonQuit.pack(side = Tk.LEFT)

updateTimer()

Tk.mainloop()

