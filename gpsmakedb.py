#!/usr/bin/python
# -*- coding: utf-8 -*-

# Script created by Chris Joyce <chris@joyce.id.au>

import sqlite3 as lite
import sys
from config import config

con = lite.connect(config['DB_NAME'])

with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS extra")
	cur.execute("DROP TABLE IF EXISTS gpslog")
	cur.execute("CREATE TABLE extra (id INT, name varchar(32), value varchar(100), casttype varchar(32))")
	cur.execute("CREATE TABLE gpslog (id INTEGER PRIMARY KEY, datetime varchar(30), lon varchar(100), lat varchar(100), alt varchar(100), speed varchar(100), uploaded varchar(1), session_id INT)")
	cur.execute("INSERT INTO extra VALUES(1,'dbversion', '2', 'INT')")
	cur.execute("INSERT INTO extra VALUES(2, 'hasrunonce', 'true', 'BOOL')")
