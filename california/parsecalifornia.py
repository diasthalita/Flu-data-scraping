#!/usr/bin/python

##============================================================================== 
# File:         parsecalifornia.py
# Date:         Thu Dec  8 10:05:25 EST 2016
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

pattern1 = re.compile('^Influenza Report Highlights')
pattern2 = re.compile('(.*?)(\d*\,?\d+?)(\s\(.*\)\s)(were positive for influenza)(.*?)')
pattern3 = re.compile('^(.\s+)(\d*\,?\d+?)(.*specimens tested.*)')
pattern4 = re.compile('^California Influenza and Other Respiratory Disease Surveillance for.*')
pattern5 = re.compile('(.*?)(Week)(\s)(\d+)')
pattern6 = re.compile('(\()(.*?)(\sto\s)(.*\d+,\s\d+)(\))')
pattern7 = re.compile('(^California Influenza and Other Respiratory Disease Surveillance for.*)(\(.*)')
pattern8 = re.compile('(^\(.*\))')

filename = sys.argv[1]
file = open(filename)
lines = file.readlines()

lab = "could not retrieve"
for i in range(0, len(lines)):
	if re. match(pattern1, lines[i]):
		for x in range(0,30):
			target = lines[i+x]
			if re.match(pattern3, target):
				lab = re.findall(pattern3, target)
				lab = '"' + lab[0][1] + '"'
				lab = lab.replace(" ","")
			if re.match(pattern2, target):
				lab = re.findall(pattern2, target)
				lab = '"' + lab[0][1] + '"'
				lab = lab.replace(" ","")


week = "could not retrieve"
weekEnding = "could not retrieve"
for i in range(0, len(lines)):
	if re.match(pattern4, lines[i]):
		weekline = re.findall(pattern5, lines[i])
		week = weekline[0][3]
	if re. match(pattern4, lines[i]):
		for x in range(0,5):
			target = lines[i+x]
			if re.match(pattern8, target):
				weekEndingline = re.findall(pattern8, target)
				weekEnding =  weekEndingline[0]
				weekEnding =  weekEnding.replace("(","")
				weekEnding =  weekEnding.replace(")","")
				break
	if re.match(pattern6, lines[i]):
		weekEndingline = re.findall(pattern6, lines[i])
		weekEnding =  weekEndingline[0][3]
		break
	if re.match(pattern7, lines[i]):
		weekEndingline = re.findall(pattern7, lines[i])
		weekEnding =  weekEndingline[0][1]
		weekEnding =  weekEnding.replace("(","")
		break

print week + ',' + '"' +  weekEnding + '",' + 'CA'+ "," + lab + "," + lab + "," + 'N/A' + ","  + 'N/A'


