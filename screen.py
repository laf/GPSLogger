#!/usr/bin/python

import os.path

os.system("/usr/bin/screen -c /home/pi/.screenrc -t logger -L -d -m -S logger -- /usr/bin/python /home/pi/GPSLogger/gpslogger.py")

os.system("/usr/bin/screen -c /home/pi/.screenrc -t check -L -d -m -S check -- /usr/bin/python /home/pi/GPSLogger/checkData.py")
