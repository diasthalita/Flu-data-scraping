#!/usr/bin/env python
##============================================================================== 
# File:         newmexico.py 
# Date:         Tue Nov 21 15:38:20 EST 2017
# Author(s):    Thalita Coleman  <thalitaneu@gmail.com>
# Abstract:     Parses the .html files which contains the HTML source for
#       	the page https://nmhealth.org/about/erd/ideb/isp/data/, and returns the URL 
#		of all weekly flu reports.
#------------------------------------------------------------------------------ 
# Requirements: Python 2.7 
#------------------------------------------------------------------------------ 
# Notes: Don't forget to update html file names 
#==============================================================================


import re
import sys
import os
from subprocess import *
import fileinput #use fileinput instead of open() for multiple files

pattern1 = re.compile('.*href.*\.pdf')
pattern2 = re.compile('(.*href=")(.*?)("\stitle.*?)(WeekEnding-)(.*?)(.pdf.*?)')


prefix = 'https://nmhealth.org'

nameUrls = []

# Insert the names of the .html files below 
for line in fileinput.input(files=('yourHTML1.html', 'yourHTML.html')):
#for line in fileinput.input(files=('NMpage1.html','NMpage2.html','NMpage3.html','NMpage4.html','NMpage5.html', 'NMpage6.html','NMpage7.html')):
	if re.match(pattern1, line):

		matches = re.findall(pattern2, line)
		for match in matches:
			url = prefix + match[1]
			weekEnding = match[4] + '.pdf'
			weekEnding = weekEnding.replace(" ","")
			nameUrls.append((weekEnding, url))

for pair in nameUrls:
	print pair
	cmd = ['wget', '-O', pair[0], '--no-check-certificate', pair[1]]
	p = Popen(cmd)
	p.wait()


