#!/usr/bin/env python
#-*- encoding:utf-8 -*-

#Input x={是否是应答订单，出发地ID，目的地ID，发起时间，
#            价格，POI级别，拥堵级别，拥堵时间，天气，温度，PM2.5}

#replace the following path according to your computer
cluster_map_file = open('G:\\didi\season_1\\training_data\\cluster_map\\cluster_map','r')
poi_data_file = open('G:\\didi\\season_1\\training_data\\poi_data\\poi_data_new.txt','r')
timesplit_file = open('G:\\didi\\season_1\\test_set_1\\timesplit.txt','r')

