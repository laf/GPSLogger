GPSLogger
=========

GPS Logging code for use with Raspberry Pi

I created this code to help with a project to track a group ride from Manchester, UK to the Paris, France.
Rather than using our mobiles to track the adventure I decided to build a GPS logger with a Raspberry Pi that would send data back to a web server where people could then track us in real time.

I've run this and tested using Rasbian:
Linux raspberrypi 3.6.11+ #371 PREEMPT Thu Feb 7 16:31:35 GMT 2013 armv6l GNU/Linux

This code is the result.

###############################
# Dependencies needed         #
###############################

1. python 2.7.3 or greater (tested only on 2.7.3)
2. sqlite3 for local data logging
3. screen to run code in the background
4. gpsd,gpsd-clients and python-gps

###############################
# Installation steps          #
###############################

To install and setup, follow these instructions.

1. To follow...
