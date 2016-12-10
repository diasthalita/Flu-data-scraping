#!/usr/bin/env python
##============================================================================== 
# File:         parsedelaware.py
# Date:         Thu Dec  8 10:05:25 EST 2016
# Author(s):    Thalita Coleman  <thalitaneu@gmail.com>
# Abstract:     Scrapes the .txt files and returns a CSV file named delawareresults.csv 
#		with "Week", "Week Ending", "State", "Season", "Total", "Lab", "Visits", 
#		and "Hospitalizations" data for each week. When the data is not available 
#		in the report, it returns N/A value. When the program was not able to parse 
#		the data, it returns a "could not retrieve" message. The "could not retrieve"
#		values can then be collected manually.      
#------------------------------------------------------------------------------ 
# Requirements: Python 2.7 
#------------------------------------------------------------------------------ 
# Notes: 
#============================================================================== 


import sys
import re

pattern1 = re.compile('.*Delaware Weekly Influenza Report.*')
pattern9 = re.compile('.*Delaware Weekly Influenza Surveillance Report.*')
pattern2 = re.compile('(.*Week\s+)(\d+)(\s+\(.*?\s\d+)(\s.*?\s)(.*\))')
pattern6 = re.compile('(.*Week\s)(\d+)(\s\()(.*?)(\s\d+)(\s.*?\s)(.*)(\))')				
pattern7 = re.compile('(.*Week\s)(\d+)(\s\()(.*?)(\s\d+)(.*\s)(.*)(\))')				
pattern3 = re.compile('.*laboratory-confirmed\s+cases\s+of\s+influenza\s+reported\s+among.*')
pattern4 = re.compile('(.*were)(.*?)(laboratory-confirmed\s+cases\s+of\s+influenza\s+reported\s+among.*)')
pattern5 = re.compile('(.*There were)(\s\d*\,?\d+?\s)(confirmed cases of influenza.*)')
pattern8 = re.compile('(.*There were\s+)(.*?)(\s+confirmed cases of influenza.*)')
pattern10 = re.compile('(.*Delaware Weekly InfluenzaSurveillance ReportWeek\s|Delaware Weekly Influenza Surveillance ReportWeek\s)(.*?)(\s\(.*\))(Delaware Division.*)')

filename = sys.argv[1]
file = open(filename)
lines = file.readlines()

week = "could not retrieve"
weekEnding = "could not retrieve"
labCases = "could not retrieve"
 
for i in range(0, len(lines)):
	if re.match(pattern1, lines[i]):
		for j in range(1,15):
			target = lines[i+j]
			if re.match(pattern2, target):
				matches = re.findall(pattern2, target)
				week = matches[0][1]
				week = week.replace("\n","")
				weekEnding = '"' + matches[0][4] + '"'
				weekEnding = weekEnding.replace(")","")
			if re.match(pattern7, target):
				matches = re.findall(pattern7, target)
				week = matches[0][1]
				weekEnding = '"' + matches[0][3] + matches[0][5] + matches[0][6] + '"'
				weekEnding = weekEnding.replace(")","")
				weekEnding = weekEnding.replace("-"," ")

for i in range(0, len(lines)):
	if re.match(pattern10, lines[i]):
			matches = re.findall(pattern10, lines[i])
			week = matches[0][1]
			week = week.replace("\n","")
			weekEnding = '"' + matches[0][2] + '"'
			weekEnding = weekEnding.replace("(","")
			weekEnding = weekEnding.replace(")","")
																			        
for i in range(0, len(lines)):
	if re.match(pattern9, lines[i]):
		for j in range(1,15):
			target = lines[i+j]
			if re.match(pattern2, target):
				matches = re.findall(pattern2, target)
				week = matches[0][1]
				week = week.replace("\n","")
				weekEnding = '"' + matches[0][4] + '"'
				weekEnding = weekEnding.replace(")","")
			if re.match(pattern7, target):
				matches = re.findall(pattern7, target)
				week = matches[0][1]
				weekEnding = '"' + matches[0][3] + matches[0][5] + matches[0][6] + '"'
				weekEnding = weekEnding.replace(")","")
				weekEnding = weekEnding.replace("-"," ")
																			        
for i in range(0, len(lines)):
	if re.match(pattern3, lines[i]):
		target = re.findall(pattern4, lines[i])
		labCases = target[0][1]
		labCases = labCases.replace(",","")
		labCases = labCases.replace(" ","")
		labCases = labCases.replace("no","0")
	if re.match(pattern5, lines[i]):
		target = re.findall(pattern5, lines[i])
		labCases = target[0][1]
		labCases = labCases.replace(",","")
		labCases = labCases.replace(" ","")
		labCases = labCases.replace("no","0")
	if re.match(pattern8, lines[i]):
		target = re.findall(pattern8, lines[i])
		labCases = target[0][1]
		labCases = labCases.replace(",","")
		labCases = labCases.replace(" ","")
		labCases = labCases.replace("no","0")

print week + ',' + weekEnding + ',' + 'DE' + ',' + 'season' + ',' + 'total' + ',' + labCases + ',' + 'visits' + ',' + 'hospitalization'




