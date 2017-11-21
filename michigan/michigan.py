#!/usr/bin/env python

##============================================================================== 
# File:         michigan.py 
# Date:         Tue Nov 21 16:28:36 EST 2017
# Author(s):    Thalita Coleman  <thalitaneu@gmail.com>
# Abstract:     Parses the file michigan.html  -- which contains the HTML source 
#		for the page http://www.michigan.gov/mdhhs/0,5885,7-339-71550_2955_22779_40563-143382--,00.html,
#		and returns the URL of all weekly flu reports. Downloads the flu reports in .pdf format.
#------------------------------------------------------------------------------ 
# Requirements: Python 2.7 
#------------------------------------------------------------------------------ 
# Notes: Don't forget to update html file names
#==============================================================================

import re
import sys
import os
from subprocess import *

# Insert the names of the .html files below 
file = open('yourHtml.html', 'r')
#file = open('2017_michigan.html', 'r')
lines =  file.readlines()
file.close()

pattern1 = re.compile('.*href.*\.pdf')
pattern2 = re.compile('(.*style=".*?)(href=")(.*\.pdf)(.*_blank">)(.*?)(</a>)')

prefix = 'http://www.michigan.gov'

nameUrls = []

for i in range(0, len(lines)):
	if re.match(pattern1, lines[i]):
		matches = re.findall(pattern2, lines[i])
		#print matches
		for match in matches:
			url = prefix + match[2]
			week = match[4] + '.pdf'
			week = week.replace(" ","")
			week = week.replace(",","")
			#print week, url
			nameUrls.append((week, url))

for pair in nameUrls:
	cmd = ['wget', '-O', pair[0], '--no-check-certificate', pair[1]]
	p = Popen(cmd)
	p.wait()

