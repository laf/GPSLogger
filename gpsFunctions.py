# Script created by Neil Lathwood <neil@lathwood.co.uk>

import httplib, urllib, socket, os
from urllib2 import Request, urlopen, URLError, HTTPError
from config import config

def uploadData ( gpsdate,gpslon,gpslat,gpsalt,gpsspeed,gpssession ):
	"Pass data to this function to upload to web api"

	Response = ''

	apiURL = config['website']
	gps_json = {'timelog': gpsdate, 'lon':  gpslon, 'lat': gpslat, 'alt': gpsalt, 'speed': gpsspeed, 'session': gpssession}
	params = urllib.urlencode(gps_json)
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	conn = httplib.HTTPConnection(apiURL, timeout=1)
	try:
		conn.request("POST", "/gps.php?key=APIKEY", params, headers)
		response = conn.getresponse()
		if response.status == 200:
			data = response.read()
			if data == 'DONE':
				Response = 'OK'
			else:
				Response = 'Bad upload of data',data
		else:
			Response = 'Bad response from API'

		conn.close()
	except (httplib.HTTPException, socket.error) as ex:
		Response = 'BAD API gateway'

	return Response


def checkAPI ():
	"Check the API is up and running so we can remote log data"

	statusURL = string.join('http://',config['website'],'/gps_status.php')
	Response = ''
	req = Request(statusURL)
	try:
		response_status = urlopen(req)
		if response_status.read() == 'OK':
			Response = 'OK'
		else:
			Response = 'BAD API response, moving on.'

	except URLError as e:
		print 'FAIL connecting to API'
	return Response

def currentSession ():
	"Get the current session id"
	socket.setdefaulttimeout(1)

	sessionID = 0
	sessionURL = string.join('http://',config['website'],'/gps_session.php')
	ResponseSession = ''
	reqSession = Request(sessionURL)
	try:
		session_response = urlopen(reqSession)
		tmpSession = session_response.read()
		if tmpSession >= 1:
			sessionID = tmpSession

	except URLError as e:
		print 'FAIL connecting to session API'

	return sessionID

