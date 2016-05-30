#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-30 00:19:08
# @Author  : lemondy
# @Link    : https://github.com/matter/didicompetition
# @Version : 1.0
###########################
import datetime

timesplitfile = open('G:\\didi\season_1\\test_set_1\\read_me_1.txt','r')
timeout = open('G:\\didi\season_1\\test_set_1\\timesplit.txt','w')
timesplit = timesplitfile.readlines()



for item in timesplit[1:]:
	elements = item.split('-')
	#hours = round(int(elements[-1]) * 10 / 60.0,1)
	#print item.replace('-'+elements[-1], "")
	minutes = int(elements[-1])*10
	#print minutes
	starttime = datetime.datetime.strptime(item.replace('-'+elements[-1], '')+' '+'00:00:00',"%Y-%m-%d %H:%M:%S")
	#print starttime
	endtime = starttime + datetime.timedelta(minutes=minutes)
	timeout.write(str(endtime)+'\n')
	#print endtime




