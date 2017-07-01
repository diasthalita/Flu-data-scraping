#!/usr/bin/env python
##============================================================================== 
# File:         parseny.py
# Date:         Sat Jul  1 14:43:28 EDT 2017
# Author(s):    Thalita Coleman  <thalitaneu@gmail.com>
# Abstract:	Scrapes the .txt files and returns a CSV file named californiaresults.csv 
#		with "Week", "Week Ending", "State", "Season", "Total", "Lab", "Visits", and 
#		"Hospitalizations" data for each week. When the data is not available in the
#		report, it returns N/A value. When the program was not able to parse the data, 
#		it returns a "could not retrieve" message. The "could not retrieve" values 
#		can then be collected manually.      
#------------------------------------------------------------------------------ 
# Requirements: Python 2.7 
#------------------------------------------------------------------------------ 
# Notes: 
#============================================================================== 

import sys
import re

pattern1 = re.compile('^(During the week ending\s)(.*)')
pattern2 = re.compile('(.*?)(\d+?\,?\d+?)(\slaboratory-confirmed influenza reports)(.*?)')
pattern3 = re.compile('(.*?)(hospitalized with laboratory-confirmed influenza was\s)(\d+)(.*\s.*)')

filename = sys.argv[1]
#filename = "2017_week02.txt"
file = open(filename)
lines = file.readlines()

lab = "could not retrieve"
week = "could not retrieve"
weekEnding = "could not retrieve"
hospital = "could not retrieve"


for i in range(0, len(lines)):
	if re.match(pattern1, lines[i]):
		weekEnding=re.findall(pattern1, lines[i])
		weekEnding=weekEnding[0][1]
		#print weekEnding
		for x in range(0,30):
			target = lines[i+x]
			if re.match(pattern2, target):
				lab = re.findall(pattern2, target)
				lab = lab[0][1]
				lab = lab.replace(" ","")
				lab = lab.replace(",","")
				#print lab


for i in range(0, len(lines)):
	if re.match(pattern3, lines[i]):
		hospital=re.findall(pattern3, lines[i])
		hospital=hospital[0][2]
		hospital=hospital.replace(",","")
		#print hospital
		break
total = str(int(lab) + int(hospital))

#Week	Week Ending	State	Season	Total	Lab	Visits	Hospitalizations																		
print week + ',' + '"' +  weekEnding + '",' + 'NY'+ "," +'2016-2017' + "," + total + "," + lab + "," + 'N/A' + ","  + hospital


