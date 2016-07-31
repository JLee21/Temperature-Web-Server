#!/usr/bin/python


import cgi, cgitb
import sqlite3
import sys
import glob
import time
import threading

dbname='/var/www/templog.db'

def getDataFromDB():

    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    try:
        # expr = """SELECT * FROM temps LIMIT 1
        #        ORDER BY timestamp DESC;"""
        curs.execute("SELECT * FROM temps ORDER BY timestamp DESC LIMIT 1; ")
                     # "ORDER BY timestamp DESC;")
        temp = curs.fetchall()
        conn.close()
        return temp
    except:
        e = sys.exc_info()[0]
        print e
        raise
        return "shit"

    rows=curs.fetchall()
    conn.close()
    return rows


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
	# fileFound = True
	# open the file representing the sensor.
	# fileobj = open(devicefile,'r')
	# lines = fileobj.readlines()
	# fileobj.close()
	# cgitb.enable()
	# form = cgi.FieldStorage()
	#first_name = form.getvalue('first_name')
	#last_name  = form.getvalue('last_name')
	# tempstr = lines[1][-6:-1]
	# tempvalue = float(tempstr)/1000*5/3+32

    temp = getDataFromDB()
    print"Content-type: text/html\n\n"
    print temp
    cgi.print_exception()      # catch and print errors
	
if (__name__ == "__main__"):
    main()
