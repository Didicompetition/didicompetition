#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import os
import datetime
#Input x={是否是应答订单，出发地ID，目的地ID，发起时间，
#            价格，POI级别，拥堵级别，拥堵时间，天气，温度，PM2.5}

#replace the following path according to your computer
cluster_map_file = open('G:\\didi\season_1\\training_data\\cluster_map\\cluster_map','r')
poi_data_file = open('G:\\didi\\season_1\\training_data\\poi_data\\poi_data_new.txt','r')
#timesplit_file = open('G:\\didi\\season_1\\test_set_1\\timesplit.txt','r')

weather_path = r'G:\didi\season_1\training_data\weather_data'
weather_prefix = 'weather_data'
order_path = r'G:\didi\season_1\training_data\order_data'
order_prefix = 'order_data'
traffic_path = r'G:\didi\season_1\training_data\traffic_new_data'
traffic_prefix = 'traffic_data'

outfile = open(r'G:\didi\season_1\training_data\newtrain\dataset.txt', 'w')

#district
dist_dict = dict()
poi_dict = dict()

##get district
for line in cluster_map_file.readlines():
	elements = line.split("\t")
	dist_dict[elements[0]] = elements[1]  #hashid id
#release file
cluster_map_file.close()

#get poi
for line in poi_data_file.readlines():
	elements = line.split('\t')
	poi_dict[elements[0]] = ( elements[2].split('#')[-1].strip('\n'),elements[1])
#release file
poi_data_file.close()


outfile.write('time'+'\t'+'isreply'+'\t'+'start_dist_id'+'\t'+'dest_dist_id'+'\t'+'price'
				+'\t'+'poi_level'+'\t'+'poi_number'+'\t'+'traffic_level_1'+'\t'+'traffic_level_2'+'\t'+'traffic_level_3'+'\t'
				+'traffic_level_4'+'\t'+'weather'+'\t'
				+'temperature'+'\t'+'pm'+'\n')
#count reply
count = 0

for root, dirnames, files in os.walk(order_path):
	for fname in files:
		names = fname.split('_')
		orderfile = open(root+'/'+fname,'r')
		weatherfile = open(weather_path+'/'+weather_prefix+'_'+names[-1],'r')
		trafficfile = open(traffic_path+'/'+traffic_prefix+'_'+names[-1],'r')

		#每次写入1000行，提高写入速度
		countLine = 0
		multi_lines = ''

		weather_dict = dict()
		#get weather info
		for line in weatherfile:
			items = line.split('\t')
			try:
				t = datetime.datetime.strptime(items[0], "%Y-%m-%d %H:%M:%S")
			except ValueError, v:
				print items[-1],'59'
			
			weather_dict[t] = items[1:]
		weatherfile.close()

		traffic_dict = dict()
		#get traffic info
		for line in trafficfile:
			items = line.split('\t')
			try:
				t = datetime.datetime.strptime(items[-1].strip('\n'), "%Y-%m-%d %H:%M:%S")
			except ValueError, v:
				print items[-1],'71'
			traffic_dict[(items[0],t)] = items[1:5]  # 路段拥堵情况
		trafficfile.close()

		#order_dict = dict()
		#get order info
		for line in orderfile:
			items = line.split('\t')   #order_id	driver_id	passenger_id	start_district_hash	dest_district_hash	Price	Time
			isreply = 0
			if items[1] != 'NULL':   #driverid
				isreply = 1
			if isreply == 0:
				count += 1
			#如果出发地不在分区中，就不考虑
			if dist_dict.has_key(items[3]) == False:
				continue
			start_dist_id = dist_dict[items[3]]
			try:
				dest_dist_id = dist_dict[items[4]]
			except KeyError, v:
				dest_dist_id = 'NULL'
			price = items[5]
			try:
				t = datetime.datetime.strptime(items[6].strip('\n'),"%Y-%m-%d %H:%M:%S")
			except ValueError, v:
				print items[6],'88'

			poi = poi_dict[items[3]]  #乘车位置的poi

			#traffic
			traffic_temp = filter(lambda x:x[0][0]==items[3], traffic_dict.items())
			for traf in traffic_temp:
				if (t-traf[0][1]).seconds < 600: #相差10分钟以内
					traffic = traffic_dict[(items[3],traf[0][1])]
					break


			#weather

			for key in weather_dict.keys():
				if (t-key).seconds < 600:  #10分钟内的天气情况
					weather = weather_dict[key]
					break
			#orderfile.close()
			countLine += 1
			multi_lines += (str(t)+'\t'+str(isreply)+'\t'+start_dist_id.strip('\n')+'\t'+dest_dist_id.strip('\n')+'\t'
				+str(price)+'\t'+'\t'.join(poi).strip('\n')+'\t'+'\t'.join(traffic).strip('\n')+'\t'+'\t'.join(weather).strip('\n')+'\n')
			if countLine == 1000:
				outfile.writelines(multi_lines)
				multi_lines = ''
				countLine = 0
		if countLine!=0:
			outfile.writelines(multi_lines)
		orderfile.close()


print 'count',count











