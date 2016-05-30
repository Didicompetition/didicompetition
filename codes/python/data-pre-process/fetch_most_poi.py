#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-29 23:16:34
# @Author  : lemondy
# @Version : 0.1
###########################

#import os
poi_data_file = open('G:\\didi\season_1\\training_data\\poi_data\\poi_data','r')
poi_data_out = open('G:\\didi\season_1\\training_data\\poi_data\\poi_data_new.txt','w')

poi_data = poi_data_file.readlines()
poi_data_file.close()

poidict = dict()



for poi in poi_data:
	items = poi.split("\t")
	tempDict = dict()
	for item in items[1:]:
		#print item
		elements = item.split(":")
		#print len(elements)
		tempDict[int(elements[1])] = elements[0]   #must convert into int, so as to can compare with each other

	#poidict[items[0]] = max(tempDict, key=tempDict.get)  #the key who has the max value
	maxKey = max(tempDict)
	poi_data_out.write(items[0]+'\t'+str(maxKey)+'\t'+tempDict[maxKey].strip("\n")+'\n')


