# Script created by Chris Joyce <chris@joyce.id.au>

import httplib, urllib, socket, os, json, requests
from urllib2 import Request, urlopen, URLError, HTTPError
from config import config

def uploadData ( gpsData ):
	"Pass data to this function to upload to web api"

	payload = {"method": "position", "params": [], "id": 1}
	
	Response = 'Broken'
	try:
		headers = {'content-type': 'application/json'}
		payload['params'].append(config['deviceid'])

		gpsData['deviceid'] = config['deviceid']
		payload['params'].append(gpsData)

		r = requests.post(config['webAPI'], data=json.dumps(payload), headers=headers)
		json_data = json.loads(r.text)
		status = json_data.get('result', None)

		Response = status['posid']
		if status['status'] == 200:
			if status['posid'] == gpsData['posid']:
				Response = 'OK'
			else:
				Response = 'Bad upload of data',status
		else:
			Response = 'Bad response from API'

	except (httplib.HTTPException, socket.error) as ex:
		Response = 'BAD API gateway'

	return Response


def checkAPI ():
	"Check the API is up and running so we can remote log data"

	payload = {"method": "apiStatus", "params": [], "id": 1}
	Response = ''
	try:
		headers = {'content-type': 'application/json'}
		payload['params'].append(config['deviceid'])

		r = requests.post(config['webAPI'], data=json.dumps(payload), headers=headers)
		json_data = json.loads(r.text)
		status = json_data.get('result', None)

		if status == 'OK' :
			Response = 'OK'
		else:
			Response = 'BAD API response, moving on.'

	except URLError as e:
		print 'FAIL connecting to API'
	return Response

def currentSession ():
	"Get the current session id"

	payload = {"method": "sequence", "params": [], "id": 1}
	sessionID = 0
	try:
		headers = {'content-type': 'application/json'}
		payload['params'].append(config['deviceid'])

		r = requests.post(config['webAPI'], data=json.dumps(payload), headers=headers)
		json_data = json.loads(r.text)
		tmpSession = json_data.get('result', None)

#		if isinstance( tmpSession, int ) and tmpSession >= 1:
		sessionID = tmpSession

	except URLError as e:
		print 'FAIL connecting to session API'

	except HTTPError as he:
		print 'FAIL connecting to session API'

	return sessionID
