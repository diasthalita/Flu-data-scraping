#!/usr/bin/env python
##============================================================================== 
# File:         parsedc.py
# Date:         Thu Dec  8 10:05:25 EST 2016
# Author(s):    Thalita Coleman  <thalitaneu@gmail.com>
# Abstract:     Scrapes the .txt files and returns a CSV file named dcresults.csv 
#		with "Week", "Week Ending", "State", "Season", "Total", "Lab", "Visits", and 
#		"Hospitalizations" data for each week. When the data is not available in the 
#		report, it returns N/A value. When the program was not able to parse the data, 
#		it returns a "could not retrieve" message. The "could not retrieve" values can 
#		then be collected manually.      
#------------------------------------------------------------------------------ 
# Requirements: Python 2.7 
#------------------------------------------------------------------------------ 
# Notes: 
#============================================================================== 

import sys
import re
import io

#filename = 'March29_2014.txt'
#filename = 'October31_2015.txt'
filename = sys.argv[1]


file = io.open(filename, encoding='utf8')
lines = file.readlines()

lab = "could not retrieve"
week = "could not retrieve"
weekEnding = "could not retrieve"
visits = "could not retrieve"

pattern1 = re.compile('(\d+-\d+)(\s+Influenza Season)')
pattern2 = re.compile('(Week.*?\(*?\))')
pattern3 = re.compile('(Week.*\()(.*?)(\s[A-Za-z]+ \d+,.*$)')
pattern4 = re.compile('(.*?)(cases of Influenza were reported.*|case of Influenza was reported.*)')
pattern5 = re.compile('(.*sentinel providers reported.*?)(\d+\s)(.*met the criteria for ILI)')
pattern6 = re.compile('.*did not report any visits meeting the criteria for ILI')

for i in range(0, len(lines)):
	if re.match(pattern1, lines[i]):
		matches = re.findall(pattern1, lines[i])
		season = matches[0][0]
		#print season
		for x in range(0,6):
			target = lines[i+x]
			if re.match(pattern3, target):
				#print lines[i]
				match = re.findall(pattern3, target)
				#print matches
				week = match[0][0]
				week = week.encode('ascii', 'ignore').decode('ascii') 
				week = week.replace("(","")
				week = week.replace(":","")
				weekEnding = match[0][2]
				weekEnding = weekEnding[1:]
				weekEnding = '"' + weekEnding.replace(")","") + '"'
				#print week, 'and', weekEnding
	if re.match(pattern4, lines[i]):
		#print lines[i]
		matches = re.findall(pattern4, lines[i])
		lab = matches[0][0]
		lab = lab.replace(" ","")
		lab = lab.encode('ascii', 'ignore').decode('ascii') 
		#lab = int(lab) 
		#print lab
	if re.match(pattern5, lines[i]):
		#print lines[i]
		matches = re.findall(pattern5, lines[i])
		visits = matches[0][1]
		visits = visits.replace(" ","")
		visits = visits.encode('ascii', 'ignore').decode('ascii')
		#visits = int(visits)
		#print visits
	if re.match(pattern6, lines[i]):
		#print lines[i]
		visits = '0'

total = "could not retrieve"

print week + ',' + weekEnding + ',' + 'DC' + ',' + season + ',' + total + ',' + lab + ',' + visits + ',' + 'N/A'					


