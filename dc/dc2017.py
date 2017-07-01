#!/usr/bin/env python
##============================================================================== 
# File:         dc2017.py 
# Date:         Thu Dec  8 10:05:25 EST 2016
# Author(s):    Thalita Coleman  <thalitaneu@gmail.com>
# Abstract:     Parses the page https://doh.dc.gov/node/114982
#		and returns the URL of all weekly flu reports. Downloads the flu reports in .pdf format.
#------------------------------------------------------------------------------ 
# Requirements: Python 2.7 
#------------------------------------------------------------------------------ 
# Notes: 
#============================================================================== 

import re
from datetime import datetime
import sys
import os
from subprocess import *
import urllib2


url = 'https://doh.dc.gov/node/114982'
header = "Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
r = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
response = urllib2.urlopen(r)
lines = response.readlines()

# find the lines we're interested in
pattern1 = re.compile('.*href.*\.pdf')
pattern2 = re.compile('(<a href=")(.*?)(".*>)')

#https://doh.dc.gov/sites/default/files/dc/sites/doh/page_content/attachments/Influenza%20Weekly%20Summary%20MMWR_19_0.pdf" type="application/pdf; length=702208" title="Influenza Weekly Summary MMWR_19.pdf">Influenza Summary Week 19  (May 7, 2017 - May 13, 2017)</a></span></div></div></div><div class="field field-name-field-related field-type-node-reference field-label-above"><div class="field-label">Related Content:&nbsp;</div><div class="field-items"><div class="field-item even"><a

pattern3 = re.compile('(.*?)(Week\s\d+)(.*?)')




nameUrls = []
for line in lines:
        if re.match(pattern1, line):
		#print line
                matches = re.findall(pattern2, line)
		matches = matches[0]
		matches = ' '.join(matches)
		matches = matches.split('href="')
		#print matches
                for match in matches:
			match = match.split('" type="')
                        url =  match[0]
			#print url
			#print type(match), '\n'
			if re.findall(pattern3, str(match)):
				week = re.findall(pattern3, str(match))
                        	week = week[0][1] + '.pdf'
                        	week = week.replace(",","_")
                        	week = week.replace(" ","")
                        	nameUrls.append((week, url))


for pair in nameUrls:
	print pair
        cmd = ['wget', '-O', pair[0], '--no-check-certificate', pair[1]]
        p = Popen(cmd)
        p.wait()

