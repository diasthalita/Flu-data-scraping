#!/usr/bin/env python
##============================================================================== 
# File:         parsenewmexico.py
# Date:         Thu Dec  8 10:05:25 EST 2016
# Author(s):    Thalita Coleman  <thalitaneu@gmail.com>
# Abstract:     Scrapes the .txt files and returns a CSV file named newmexicoresults.csv 
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

pattern1 = re.compile('^Influenza Activity in New Mexico for Week Ending.*|^Influenza Activity in New Mexico for the Week Ending.*', re.IGNORECASE)
pattern2 = re.compile('(.*Week Ending\s+)(.*?)(\s+\(MMWR Week)(.*?)(\))')
pattern3 = re.compile('.*Outpatient\s+visits\s+for\s+influenza-like\s+illness.*', re.IGNORECASE)
pattern4 = re.compile('(.*?)(of which\s)(\d+)(.*?)')
pattern5 = re.compile('(.*?)(\d+)(\s+)(\(\d+\.\d+%\))(.*?)')
pattern6 = re.compile('.*Laboratory tests for influenza.*')
pattern7 = re.compile('(.*reported\s)(.*?)(\spositive.*)')
pattern8 = re.compile('(.*reported\s)(.*?)(\srespiratory.*)')

filename = sys.argv[1]

lab="could not retrieve"
week="could not retrieve"
weekEnding="could not retrieve"
visits= "could not retrieve"
file = open(filename)
lines = file.readlines()

for i in range(0,len(lines)):
   if re.match(pattern1,lines[i]):
		matches = re.findall(pattern2, lines[i])
		for match in matches:
			week = match[3]
			weekEnding = '"' + match[1] + '"'

for i in range(0,len(lines)):
	if re.match(pattern3, lines[i]):
		for j in range(1, 5):
			target = lines[i+j]
			if re.match(pattern4, target):
				matches = re.findall(pattern4, target)
				for match in matches:
					visits = match[2]

for i in range(0,len(lines)):
	if re.match(pattern6, lines[i]):
		for j in range(0, 6):
			target = lines[i+j]
			if re.match(pattern5, target):
				matches = re.findall(pattern5, target)
				lab = matches[0][1]
				break
			if re.match(pattern7, target):
				matches = re.findall(pattern7, target)
				lab = matches[0][1]
			if re.match(pattern8, target):
				matches = re.findall(pattern8, target)
				lab = matches[0][1]

total= "N/A"

print week + ',' + weekEnding + ',' + 'NM' + ',' + 'season' + ',' + total + ',' + lab + ',' + visits + ',' + 'N/A'					
