#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-30 22:33:37
# @Author  : lemondy
# @Link    : https://github.com/matter/didicompetition
# @Version : 
###########################

import datetime
import os

path = r'G:\didi\season_1\training_data\weather_data'
outpath = r'G:\didi\season_1\training_data\weather_new_data'

for root, dirs, files in os.walk(path):
	for name in files:

		#print name
		f = open(root+'/'+name,'r')
		out = open(outpath+'/'+name,'w')
		for line in f.readlines():
			elements = line.split('\t')
			t = datetime.datetime.strptime(elements[0], "%Y-%m-%d %H:%M:%S")
			if t.minute % 10 == 0:
				out.write(line)
		out.close()


