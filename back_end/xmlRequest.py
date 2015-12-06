#!/usr/bin/python --

import cgi, cgitb
import os
import glob
import time
import threading

def checkFile():
	global fileFound, devicefile
	if fileFound:
			return
	# find the path of a sensor directory that starts with 28
	devicelist = glob.glob('/sys/bus/w1/devices/28*')
	# append the device file name to get the absolute path of the sensor 
	devicefile = devicelist[0] + '/w1_slave'
	fileFound = True
		
def main():
	fileFound = True
	# open the file representing the sensor.
	fileobj = open(devicefile,'r')
	lines = fileobj.readlines()
	fileobj.close()

	#cgitb.enable()
	#form = cgi.FieldStorage()
	#first_name = form.getvalue('first_name')
	#last_name  = form.getvalue('last_name')
	tempstr = lines[1][-6:-1]
	tempvalue = float(tempstr)/1000*5/3+32
	print("Content-type: text/html\r\n\r\n")
	print(tempvalue)
	#print("<br>")
	#cgi.print_exception()      # catch and print errors
	time.sleep(1)
	
if (__name__ == "__main__"):
	fileFound = False
	checkFile()
	while True:
		main()
