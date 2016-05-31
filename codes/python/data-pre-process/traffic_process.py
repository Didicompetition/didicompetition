#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-31 14:10:32
# @Author  : lemondy
# @Link    :  https://github.com/matter/didicompetition
# @Version : 
###########################
import os

traffic_path = r'G:\didi\season_1\training_data\traffic_data'
traffic_prefix = 'traffic_data'

outpath = r'G:\didi\season_1\training_data\traffic_new_data'


for root, dirnames, files in os.walk(traffic_path):
	for name in files:
		infile = open(traffic_path+'/'+name,'r')
		outfile = open(outpath+'/'+name,'w+')
		for line in infile:
			items = line.split('\t')
			outfile.write(items[0]+'\t'+items[1].split(':')[-1]+'\t'+items[2].split(':')[-1]+'\t'
							+items[3].split(':')[-1]+'\t'+items[4].split(':')[-1]+'\t'
							+items[5])

		outfile.close()
		infile.close()

