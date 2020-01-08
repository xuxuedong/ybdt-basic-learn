# -*- coding: utf-8 -*-

import csv
import random

file_obj = open('HisGLog_0001_20160808.csv', 'wb'); 
writer = csv.writer(file_obj); 
writer.writerow(['No', 'DN', 'UID', 'Name', 'Status', 'Action', 'APB', 'JobCode', 'DateTime']); 

# start day
n = 4; 

# clocking-in times for sign
m = 1; 

for i in range(80): 
	date = '2016/07/' + str(n); 
	j = int (random.random() * 10);
	time0 = '7:5' + str(j); 
	time1 = '11:1' + str(j);
	time2 = '12:1' + str(j);
	time3 = '17:0' + str(j);
	
	if ( (i+1) % 4 == 1): 
		writer.writerow([i, '1', '15041', '侯瑞', '0', '1', '0', '0', date + '  ' + time0]); 
	elif ( (i+1) % 4 == 2): 
		writer.writerow([i, '1', '15041', '侯瑞', '0', '1', '0', '0', date + '  ' + time1]);
	elif ( (i+1) % 4 == 3):
		writer.writerow([i, '1', '15041', '侯瑞', '0', '1', '0', '0', date + '  ' + time2]);
	else:
		writer.writerow([i, '1', '15041', '侯瑞', '0', '1', '0', '0', date + '  ' + time3]);
	
	# 4 times per day, so every 4 times add a day 
	if (m % 4 == 0): 
		n += 1; 
	
	# 20 times per week, there's a weekend per week, so every 20 times, add 2 days
	# 20's multiple must be 5's multiple, has add 1 before, so add 2 instead of 3
	if (m % 20 == 0):
		n += 2;
	
	m += 1; 
file_obj.close(); 
