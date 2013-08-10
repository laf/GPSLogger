#!/usr/bin/python

# Script created by Neil Lathwood <neil@lathwood.co.uk>

import gps
import httplib, urllib, socket, os
from urllib2 import Request, urlopen, URLError, HTTPError
import shutil
from gpsFunctions import uploadData, checkAPI, currentSession
import tweepy
import sqlite3
import datetime
from config import config

################################################
# This script is simply to interface with gpsd #
# retrieve the data and then upload to the api #
################################################

# ok, lets write the pid of this script
pidfile = open('/tmp/gpslogger.pid', "w")
pidfile.write("%s" % os.getpid())
pidfile.close

print datetime.datetime.utcnow()

# Connect to Sqlite3 DB
conn = sqlite3.connect('/home/pi/GPSLogger/gpslog.db')
c = conn.cursor()

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])

api = tweepy.API(auth)

print api.me().name, datetime.datetime.utcnow()

sessionID = currentSession()
print 'Session',sessionID
now=datetime.datetime.now()
curTime = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
print curTime
if sessionID > 0:
	api.update_status("We've started a ride, keep a track online http://DOMAIN.co.uk/rides.php?id=%s %s" % (sessionID, curTime))
else:
	api.update_status('GPS logging started @ %s' % (curTime))
os.system('mpg321 /home/pi/GPSLogger/MP3/logging_started.mp3 &')
counter = 0
failCounter = 0

while True:
	try:
		report = session.next()
		# Wait for a 'TPV' report and display the current time
		# To see all report data, uncomment the line below
		#print report
		logged = 'NO'
		gpstime = ''
		gpslon = ''
		gpslat = ''
		gpsalt = ''
		gpsspeed = ''
		gpsmode = ''
		if report['class'] == 'TPV':
			if hasattr(report, 'time'):
				gpstime = report.time
			if hasattr(report, 'lon'):
				gpslon = report.lon
			if hasattr(report, 'lat'):
				gpslat = report.lat
			if hasattr(report, 'alt'):
				gpsalt = report.alt
			if hasattr(report, 'speed'):
				gpsspeed = report.speed
			if hasattr(report, 'mode'):
			 	gpssmode = report.mode

			if gpstime and gpslon and gpslat and gpsalt and gpsspeed and gpsmode >= config['allowedGPSmodes']:
				counter += 1

				uploadResponse = uploadData ( gpsdate=unicode(gpstime), gpslon=unicode(gpslon),gpslat=unicode(gpslat),gpsalt=unicode(gpsalt),gpsspeed=unicode(gpsspeed),gpssession=unicode(sessionID) )

				if counter >= config['tweetTime']:
					os.system('mpg321 /home/pi/GPSLogger/MP3/logging_data.mp3 &')
					print 'Updating twitter',datetime.datetime.utcnow()
					now=datetime.datetime.now()
					curTime = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
					api.update_status("Hey, see where we are riding right now http://www.DOMAIN.co.uk/rides.php?id=%s @ %s" % (sessionID,curTime))
					counter = 0

				if uploadResponse != 'OK':
					# Write data to local sqlitedb
					print uploadResponse,datetime.datetime.utcnow()
					gpsData = [gpstime, gpslon, gpslat, gpsalt, gpsspeed, 'N', sessionID]
					c.execute("INSERT INTO gpslog (datetime,lon,lat,alt,speed,uploaded,session_id) VALUES (?,?,?,?,?,?,?);", gpsData)
					conn.commit()
					#c.execute("create table gpslog (id INT primary key,datetime varchar(30),lon varchar(100),lat varchar(100),alt varchar(100),speed varchar(100),uploaded varchar(1));")
				else:
					print 'Data uploaded', uploadResponse,datetime.datetime.utcnow()
			else:
				failCounter += 1
				print 'Data error from gps',gpstime,gpslon,gpslat,gpsalt,gpsspeed,datetime.datetime.utcnow()
				if failCounter >= 60:
					print 'Playing gps error file',datetime.datetime.utcnow()
					os.system('mpg321 /home/pi/GPSLogger/MP3/gps_error.mp3 &')
					failCounter = 0

	except KeyError:
		pass
	except KeyboardInterrupt:
		os.remove('/tmp/gpslogger.pid')
		quit()
	except StopIteration:
		os.remove('/tmp/gpslogger.pid')
		session = None
		print "GPSD has terminated",datetime.datetime.utcnow()

