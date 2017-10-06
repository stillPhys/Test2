import socket
#import databaseUser, databasePassword, addrSensorTest
#from personalData.py
from personalData import *

sock = socket.socket()
sock.connect((addrSensorTest, 8080))
sock.send('t')
data = sock.recv(16)
sock.close()
print data

