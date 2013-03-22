#!/usr/bin/python

# Script created by Neil Lathwood <neil@lathwood.co.uk>

import os.path

# This script will check that gpslogger.py is running
try:
	if os.path.isfile('/tmp/gpslogger.pid') == True:
		with open('/tmp/gpslogger.pid', 'rU') as f:
			for line in f:
				if os.path.exists("/proc/%s" % line) == False:
					print 'not running'
					os.system("/usr/bin/screen -c /home/pi/.screenrc -t logger -L -d -m -S logger -- /usr/bin/python /home/pi/GPSLogger/gpslogger.py")
except KeyError:
	pass
except KeyboardInterrupt:
	quit()
except StopIteration:
	quit()
