## Temperature-Web-Server
Take temperature readings from a MySQL database and live-stream them to a web page.
Note that a preceding ** means that this has yet to be started or is a work in progress.

====================================================================
B A C K - E N D
====================================================================
A Raspberry Pi Linux copmuter is connected to the home network.
It has a simple temperature sensor connected to it.
A Python script is responsible for inserting the temperature, timestamp, location at a specified interval (every 5 seconds) into a MySQL database.
The Raspberry is running an Apache server in order to process requests from a webpage.
**A Python script will handle HTTP requests from a webpage by pulling the needed data from the MySQL database.

====================================================================
F R O N T - E N D
====================================================================
**A web page with AJAX will be used to periodically request data from the database.
**Eventual goal is to have numerous sensors strategically placed and to have a UI that easily displays current conditions, past conditions, etc.
