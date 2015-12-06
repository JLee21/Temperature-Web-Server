#!/usr/bin/python --

import os

def main():
	print("Content-type: text/html\r\n\r\n")
	print("<font size=+1>Environment</font><br \>")
	for param in os.environ.keys():
        print("<b>%20s</b>: %s</br></hr>" % (param, os.environ[param]))
	  
if (__name__ == "__main__"):
    #while True:
    main()
