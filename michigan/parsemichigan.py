#!/usr/bin/env python

##============================================================================== 
# File:         parsemichigan.py
# Date:         Tue Nov 21 16:32:51 EST 2017
# Author(s):    Thalita Coleman  <thalitaneu@gmail.com>
# Abstract:     Scrapes the .txt files and returns a CSV file named michiganresults.csv 
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

filename = sys.argv[1]
file = open(filename)
lines = file.readlines()

pattern1 = re.compile('(Influenza Surveillance Repor)(.*for the Week Ending\s|for the Week Ending Date\s)(.*)')
pattern2 = re.compile('Sentinel Provider Surveillance')
pattern3 = re.compile('(.*total\s+of\s+)(.*?)(patient visits due to ILI)(.*?)')
pattern4 = re.compile('.*?Hospital Surveillance.*')
pattern5 = re.compile('(.*?counties\.\s)(.*?)(hospitalization reported|hospitalizations reported)(.*?)')
pattern6 = re.compile('.*?Laboratory Surveillance.*')
pattern7 = re.compile('(.*Bureau of Laboratories reported\s)(\\d+|\w+)(.*?)')
pattern8 = re.compile('.*?to Date.*')

weekEnding=''
for i in range(0, len(lines)):
	if re.match(pattern1, lines[i]):
		matches = re.findall(pattern1, lines[i])
		weekEnding = '"' + matches[0][2] + '"'
		
visits = ''
for i in range(0, len(lines)):
	visitsILI = []
	if re.match(pattern2, lines[i]):
		visitsILI.append(lines[i+1])
		visitsILI.append(lines[i+2])
		visitsILI.append(lines[i+3])
		visitsILI.append(lines[i+4])
		visitsILI.append(lines[i+5])
		visitsILI.append(lines[i+6])
		visitsILI.append(lines[i+7])
		visitsILI = ' '.join(visitsILI)
		visitsILI = visitsILI.replace('\n', '')
		if re.match(pattern3, visitsILI):
			matches = re.findall(pattern3, visitsILI)
			visits = matches[0][1]

hospitalization = ''
hosp1 = ''
hosp2 = ''
for i in range(0, len(lines)):
	hosp = []
	if re.match(pattern4, lines[i]):
		hosp.append(lines[i+1])
		hosp.append(lines[i+2])
		hosp.append(lines[i+3])
		hosp.append(lines[i+4])
		hosp.append(lines[i+5])
		hosp.append(lines[i+6])
		hosp.append(lines[i+7])
		hosp = ' '.join(hosp)
		hosp = hosp.replace('\n', '')
		if re.match(pattern5, hosp):
			matches = re.findall(pattern5, hosp)
			hosp1 = '"' + matches[0][1] + '"'
	hosps = []
	if re.match(pattern8, lines[i]):
		hosps.append(lines[i-1])
		hosps.append(lines[i-2])
		hosps.append(lines[i-3])
		hosps.append(lines[i-4])
		hosps.append(lines[i-5])
		hosps = ' '.join(hosps)
		hosp2 = hosps.replace('\n', '') 
		hosp2 = '"' + hosp2.replace(' ', '') + '"'
hospitalization = hosp1 + hosp2		

laboratory = ''
for i in range(0, len(lines)):
	lab = []
	if re.match(pattern6, lines[i]):
		lab.append(lines[i+1])
		lab.append(lines[i+2])
		lab.append(lines[i+3])
		lab.append(lines[i+4])
		lab.append(lines[i+5])
		lab = ' '.join(lab)
		lab = lab.replace('\n', '')
		if re.match(pattern7, lab):
			matches = re.findall(pattern7, lab)
			laboratory = '"' + matches[0][1] + '"'


print 'week' + ',' + weekEnding + ',' + 'MI' + ',' + 'season' + ',' + 'total' + ',' + laboratory + ',' + visits + ',' + hospitalization











