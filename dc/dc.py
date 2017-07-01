#!/usr/bin/env python

##============================================================================== 
# File:         dc.py 
# Date:         Thu Dec  8 10:05:25 EST 2016
# Author(s):    Thalita Coleman  <thalitaneu@gmail.com>
# Abstract:     Parses the files dc.html and dc1.html -- which contains the HTML source for
#  		     	the pages http://doh.dc.gov/node/981182 and http://doh.dc.gov/node/114982, 
#				and returns the URL of all weekly flu reports. Downloads the flu reports in .pdf format.
#------------------------------------------------------------------------------ 
# Requirements: Python 2.7 
#------------------------------------------------------------------------------ 
# Notes: 
#==============================================================================

import re
import sys
import os
from subprocess import *
import fileinput

nameUrls = []

#2014-2015
prefix = 'http://doh.dc.gov/sites/default/files/dc/sites/doh/page_content/attachments/Influenza%20Weekly%20Summary%20MMWR_' 
postfix = '_0.pdf'
postfix1 = '.pdf'
postfix2 = '_2015.pdf'
for i in range(40, 45):
	week = '2014week' + str(i) + '.pdf'
	url = prefix + str(i) + postfix1
	nameUrls.append((week, url))
	
#2013-2014
prefix1 = 'http://doh.dc.gov/sites/default/files/dc/sites/doh/publication/attachments/Influenza%20Weekly%20Summary%20MMWR_'
for i in range(40, 53):
	week = '2013week' + str(i) + '.pdf'
	url = prefix1 + str(i) + postfix1
	nameUrls.append((week, url))

prefix2 = 'http://doh.dc.gov/sites/default/files/dc/sites/doh/publication/attachments/2014%20Influenza%20Weekly%20Summary%20MMWR_'
for i in range(1, 5):
	week = '2014week' + str(i) + '.pdf'
	url = prefix2 + str(i) + postfix1
	nameUrls.append((week, url))

#2012-2013
prefix3 = 'http://doh.dc.gov/sites/default/files/dc/sites/doh/publication/attachments/Influenza%20Weekly%20Summary%20MMWR_' 
for i in range(1, 21):
	week = '2013week' + str(i) + '.pdf'
	url = prefix3 + str(i) + postfix1
	nameUrls.append((week, url))



pattern1 = re.compile('.*href.*\.pdf')
pattern2 = re.compile('(<a href=")(.*?)(".*</a>)(.*\s-\s)(.*)(\).*li>)')


for line in fileinput.input(files=('dc.html','dc1.html')):
	if re.match(pattern1, line):
		matches = re.findall(pattern2, line)
		for match in matches:
			url =  match[1]
			week = match[4] + '.pdf'
			week = week.replace(",","_")
			week = week.replace(" ","")
			nameUrls.append((week, url))


for pair in nameUrls:
	cmd = ['wget', '-O', pair[0], '--no-check-certificate', pair[1]]
	p = Popen(cmd)
	p.wait()

