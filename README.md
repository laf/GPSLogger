GPSLogger
=========

GPS Logging code for use with Raspberry Pi

This is my first attempt at python so please go easy on any bad coding practices or mistakes, feel free to feedback though so I can update and improve the code.

I created this code to help with a project to track a group ride from Manchester, UK to the Paris, France.
Rather than using our mobiles to track the adventure I decided to build a GPS logger with a Raspberry Pi that would send data back to a web server where people could then track us in real time.

I've run this and tested using Rasbian:
Linux raspberrypi 3.6.11+ #371 PREEMPT Thu Feb 7 16:31:35 GMT 2013 armv6l GNU/Linux

Excuse the mp3 files, I use these to track if the unit is working when out and about :)

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

1.  cd /home/pi
    git clone git://github.com/laf/GPSLogger.git
    cd GPSLogger


## Automatic dependencies installation

```
make install
make cleandb
```

## Manual dependencies installation

#### Install GPS modules for pythong and Raspbian:

```
apt-get install gpsd
apt-get install gpsd-clients
apt-get install python-dev
apt-get install python-setuptools
apt-get install python-rpi.gpio
apt-get install python-gps
```

#### Install sqlite3 for storing local data:

````
apt-get install sqlite3
````

#### Install screen to allow for monitoring
````
apt-get install screen
````

#### Install mpeg321 to allow for audio alersts and monitoring
````
apt-get install mpeg321
````

#### Create the sqlite3 database and relevant table:

````    
sqlite3 /home/pi/GPSLogger/gpslog.db
create table gpslog (id INTEGER PRIMARY KEY,datetime varchar(30),lon varchar(100),lat varchar(100),alt varchar(100),speed varchar(100),uploaded varchar(1),session_id INT);
````

###############################
# Configure the application   #
###############################

### Edit config.py

#### Set the following variables with your twitter API keys
```
'consumer_key':"CONSUMER_KEY",
'consumer_secret':"CONSUMER_SECRET",
'access_token':"ACCESS_TOKEN",
'access_token_secret':"ACCESS_TOKEN_SECRET",
```

You can also adjust the tweetTime variable to set how often the code will post an update to twitter. Value is in seconds and defaults to 900

#### Set the lowest GPS modes 

Set the quality of GPS fix that you will accpet a position for
````
'allowedGPSmodes':2
````
* mode 1 - no valid data
* mode 2 - 2D fix, do not use mode 2 if you are intrested in climb or alt
* mode 3 - 3D-Fix, for a 3D-Fix you must have a minimum of 4 satellites

### Edit gpsFunctions.py and set the following:
    apiURL = '' # Set this to the website you want to post data to. This is just in the format  www.DOMAIN.TLD (i.e www.google.co.uk)
    APIKEY # Set this to the KEY in the web code to stop people posting data.
    statusURL = '' # Set this to the full url that returns a status response.
    sessionURL = '' # Set this to the full url for where session ID's are retrieved from.
    

### Twitter status
If you want to edit the twitter statuses that are posted then look for lines with api.update_status

### Cron
 Add this line to crontab, this wil monitor the main logging script and restart if it fails:
````
* * * * * /usr/bin/python /home/pi/GPSLogger/monitor.py
````
### Autostart
 To /etc/rc.local add the following before any exit line:
````
/usr/bin/python /home/pi/GPSLogger/screen.py
````

Reboot the pi and it should now start, gpsd and two screen sessions which you can connect to keep an eye on the status of things:
```
    screen -r logging
    screen -r check
```

The logging session is what does the majority of the data logging and uploading. The check session keeps an eye on any failed data that doesn't upload and trys again.

If you get a "gpsd:ERROR: device open fail: Permission denied - retrying read-only" you may be able to resolve this by updatingthe permissions on the device

Add the following to you /var/udev/gpsd.hotplug
```
chmod a+rw $DEVNAME
```
At the end of the file just above "gpsdctl $ACTION $DEVNAME"
