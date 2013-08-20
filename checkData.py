#!/usr/bin/python

# Script created by Neil Lathwood <neil@lathwood.co.uk>

import sqlite3
from config import config
if config['APIversion'] == 1 :
	print "New API in use"
	from webAPIfunctions  import uploadData, checkAPI
else :
	print "Old loaded"
	from gpsFunctions import uploadData, checkAPI

from time import sleep

# We don't want to start uploading data until at least 5 minutes after we start
sleep(300)

gpsData = dict()

while True:
	Response = checkAPI()

	if Response == 'OK':
		print 'API responding ok'
		conn = sqlite3.connect('/home/pi/GPSLogger/gpslog.db')
		conn.row_factory = sqlite3.Row
		c = conn.cursor()
		# Ok, now lets check if we have any data to process

		c.execute("SELECT id,event, sequence, trip, latitude, longitude, timeutc, systimeutc, altitude, eps, epx, epv, ept, speed, climb, track, mode, satellites, distance FROM gpslog ORDER BY ID LIMIT 1000")

		rows = c.fetchall()
		for row in rows:
			
			tmpID = row[0]
				  #event, sequence, trip, latitude, longitude, timeutc, systimeutc, altitude, eps, epx, epv, ept, speed, climb, track, mode, satellites, distance

			gpsData['posid'] = row['id']
			gpsData['event'] = row['event'] 
			gpsData['sequence'] = row['sequence'] 
			gpsData['trip'] = row['trip'] 
			gpsData['latitude'] = row['latitude']
			gpsData['longitude'] = row['longitude']
			gpsData['timeutc'] = row['timeutc']
			gpsData['systimeutc'] = row['systimeutc']
			gpsData['altitude'] = row['altitude']
			gpsData['eps'] = row['eps']
			gpsData['epx'] = row['epx']
			gpsData['epv'] = row['epv']
			gpsData['ept'] = row['ept']
			gpsData['speed'] = row['speed']
			gpsData['climb'] = row['climb']
			gpsData['track'] = row['track']
			gpsData['mode'] = row['mode']
			gpsData['satellites'] = row['satellites']
			gpsData['distance'] = row['distance']

			uploadResponse = uploadData (gpsData)
			print 'API Response', uploadResponse

			if uploadResponse == 'OK':
				sqlQuery = [tmpID]
				c.execute("DELETE FROM gpslog WHERE id=?;", sqlQuery)
                                conn.commit()

		conn.close()
	else:
		print 'Bad API response'

#	print "Deleting Records"
#	sqlQuery = [tmpID]
#	c.execute("DELETE FROM gpslog WHERE id <= ?;", sqlQuery)
#	conn.commit()
#	conn.close()

	sleep(60)
