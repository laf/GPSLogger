#!/usr/bin/python

# Script created by Neil Lathwood <neil@lathwood.co.uk>

import sqlite3
from gpsFunctions import uploadData, checkAPI
from time import sleep

# We don't want to start uploading data until at least 5 minutes after we start
sleep(300)

while True:
	Response = checkAPI()
	if Response == 'OK':
		print 'API responding ok'
		conn = sqlite3.connect('/home/pi/GPSLogger/gpslog.db')
		c = conn.cursor()
		# Ok, now lets check if we have any data to process
		c.execute("SELECT * FROM gpslog WHERE uploaded='N'")
		rows = c.fetchall()
		for row in rows:
			
			print row
			tmpID = row[0]
			uploadResponse = uploadData ( gpsdate=row[1], gpslon=row[2],gpslat=row[3],gpsalt=row[4],gpsspeed=row[5],gpssession=row[7] )

			print 'API Response', uploadResponse
			if uploadResponse == 'OK':

				sqlQuery = [tmpID]
				c.execute("DELETE FROM gpslog WHERE id=?;", sqlQuery)
                                conn.commit()

		conn.close()
	else:
		print 'Bad API response'

	sleep(60)
