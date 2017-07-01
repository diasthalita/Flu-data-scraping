#!/usr/bin/env python
##============================================================================== 
# File:         delaware.py 
# Date:         Thu Dec  8 10:05:25 EST 2016
# Author(s):    Thalita Coleman  <thalitaneu@gmail.com>
# Abstract:     Parses the file delaware.html  -- which contains the HTML source for the page 
#		http://dhss.delaware.gov/dhss/dph/epi/influenzawkly.html, and returns the URL 
#		of all weekly flu reports. Downloads the flu reports in .pdf format.
#------------------------------------------------------------------------------ 
# Requirements: Python 2.7 
#------------------------------------------------------------------------------ 
# Notes: 
#==============================================================================

import re
import sys
import os
from subprocess import *
<<<<<<< HEAD
import urllib2


url = 'http://dhss.delaware.gov/dhss/dph/epi/influenzawkly.html'
response = urllib2.urlopen(url)
lines = response.readlines()
=======

file = open('delaware.html', 'r')
lines =  file.readlines()
file.close()
>>>>>>> a1bb2fbb5ad6c54d49ea14c20c56afc9d9ae0c90

pattern1 = re.compile('.*href.*\.pdf')
pattern2 = re.compile('(.*?)(title=")(.*?)(Report".*?)(href=")(.*?)(".*?>)(.*?)(</a>)')

prefix = 'http://dhss.delaware.gov/dhss/dph/epi/'

nameUrls = []

for i in range(0, len(lines)):
	if re.match(pattern1, lines[i]):
		matches = re.findall(pattern2, lines[i])
		#print matches
		for match in matches:
			url = prefix + match[5]
			week = match[2] + '.pdf'
			week = week.replace(" ","")
			#print week, url
			nameUrls.append((week, url))


for pair in nameUrls:
	cmd = ['wget', '-O', pair[0], '--no-check-certificate', pair[1]]
	p = Popen(cmd)
	p.wait()
