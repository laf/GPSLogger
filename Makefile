include Makefile_help.mak

install:$(call print-help,install           ,Installs all needed dependancies.)
	echo "Install meeded support systems"
	sudo apt-get install python-dev python-setuptools python-rpi.gpio sqlite3 screen gpsd gpsd-clients python-gps mpg321
	sudo easy_install tweepy

cleandb:$(call print-help,cleandb			,Drops and re-creates the databse files)
	./gpsmakedb.py

default: help
