#!/usr/bin/env python

import MySQLdb
import os
import time
import glob

# global variables
speriod = (15 * 60) - 1
dbname = '/var/www/templog.db'

# Is it good to connect to DB only once within the script?
db = MySQLdb.connect("localhost", "root", "jfkdls;a21!", "temps")

# get temerature
# returns None on error, or the temperature as a float
# This needs to be a thread that sleeps for 2 minutes
def get_temp(devicefile):
    try:
        fileobj = open(devicefile, 'r')
        lines = fileobj.readlines()
        fileobj.close()
    except:
        return None

    # get the status from the end of line 1 
    status = lines[0][-4:-1]

    # is the status is ok, get the temperature from line 2
    if status == "YES":
        print(status)
        tempstr = lines[1][-6:-1]
        tempvalue = float(tempstr) / 1000
        tempvalue = tempvalue * 9 / 5 + 32
        print(tempvalue)
        return tempvalue
    else:
        print("There was an error getting the temperature from temp device.")
        return None

def update_DB(temperature):
    #db = MySQLdb.connect("localhost", "root", "jfkdls;a21!", "temps")
    curs = db.cursor()
    try:
		print(temperature)
		#sql = """INSERT INTO tempdata(temperature) VALUES (%f)""", (temperature)
		#db.commit("""INSERT INTO tempdata
		#	VALUES (CURRENT_DATE(), NOW(), 'kitchen', %s)""" , [("c")])
		curs.execute("""INSERT INTO tempdata
            values(CURRENT_DATE() - INTERVAL 1 DAY, NOW(), 'poop', %6.4f)""" % (temperature))
		db.commit()
		print("Data committed")
		print("\nDate     	Time		Zone		Temperature")
		print("===========================================================")

		for reading in curs.fetchall():
			print(str(reading[0])+"	"+str(reading[1])+" 	"+ reading[2]+"  	"+str(reading[3]))
    except:
        print("Error: the database is being rolled back")
        db.rollback()
    db.close()


# main function
# This is where the program starts 
def main():
    # enable kernel modules
    os.system('sudo modprobe w1-gpio')
    os.system('sudo modprobe w1-therm')

    # search for a device file that starts with 28
    devicelist = glob.glob('/sys/bus/w1/devices/28*')
    if devicelist == '':
        print("No temp device exists...\n")
        return None
    else:
        # append /w1slave to the device file
        w1devicefile = devicelist[0] + '/w1_slave'
        # get the temperature from the device file
        temperature = get_temp(w1devicefile)
        if temperature != None:
            # store it in the temp_data DB
            update_DB(temperature)
        else:
            # Sometimes reads fail on the first attempt
            # so we need to retry
            temperature = get_temp(w1devicefile)
            # store it in the temp_data DB
            update_DB(temperature)
    time.sleep(1)

if __name__ == "__main__":
    #while True:
    main()
