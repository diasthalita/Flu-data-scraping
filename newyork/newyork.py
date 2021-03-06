#!/usr/bin/env python
##============================================================================== 
# File:         newyork.py 
# Date:         Sat Jul  1 11:31:41 EDT 2017
# Author(s):    Thalita Coleman  <thalitaneu@gmail.com>
# Abstract:     Parses the page https://www.health.ny.gov/diseases/communicable/influenza/surveillance/2016-2017/archive/
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


url = 'https://www.health.ny.gov/diseases/communicable/influenza/surveillance/2016-2017/archive/'
response = urllib2.urlopen(url)
lines = response.readlines()


# find the lines we're interested in
pattern1= re.compile('.*href.*\.pdf')

# break the line into the parts we're interested in
#
#                                   link        link 
#                                   url         name
pattern2= re.compile('(.*?)(href=")(.*?)(".*?>)(.*?)(</a>)')
pattern3= re.compile('.*href')
pattern4= re.compile('.*</a>')

# break the match into parts
pattern5= re.compile('(Report for week ending\s)(.*)')
#pattern5= re.compile('(.*Weekly Report\s+-\s+|.*Weekly Report\-\s+)(.*?)(\s)(\(.*?\))')

prefix = 'https://www.health.ny.gov'

nameUrlPairs= []
problemDates= []


for i in range(0,len(lines)):
	if re.match(pattern1, lines[i]):
		matches= re.findall(pattern2,lines[i])
		for match in matches:

			# Figure out which element of the match contains href.
			# This is useful since the item after href will be the url
			for j in range(0,len(match)):
				if re.match(pattern3,match[j]):
					urlIndex= j+1  #we want the item after this match, so add 1
					currentUrl= match[urlIndex]
					currentUrl= prefix + currentUrl  # prepend the prefix
				
				
			# Figure out which element of the match contains </a>.
			# This is useful since the item before </a> will be the name of the url
			for j in range(0,len(match)):
				if re.match(pattern4,match[j]):
					nameIndex= j-1 #we want the item before this match, so subtract 1
					currentName= match[nameIndex]


			# Now display the URL and the name
			#print 'URL: ' + currentUrl + ',  Name: ' + currentName


			# Break the name into parts and retrieve the date.
			# Get the year and the "week of the year" from the date.
			# Use python's datetime module to accomplish this.
			#print currentName
			nameParts= re.findall(pattern5,currentName)
			#print nameParts
			for namePart in nameParts:
				currentDate= namePart[1]
				# January is misspelled in some reports and the program doesn't recognize the date. This should fix it.
				currentDate= currentDate.replace('Janaury', 'January')
				#print '"' + currentDate + '"'


				# Since the strptime method throws an exception when it
				# encounters an error, we have to use the "try/except"
				# construct.  If we don't use a try/except construct here,
				# then if an error is encountered python would stop
				# execution and show the error on the command line.
				try:
					dateObj= datetime.strptime(currentDate, '%B %d, %Y')
				except:
					print "skipping this date: ", currentDate
					problemDates.append(currentDate)

				# get the current year, and the current week of the year
				currentYear= dateObj.strftime('%Y')
				currentWeek= dateObj.strftime('%U')
				storedName= currentYear + '_week' + currentWeek + '.pdf'
				
				# Add the url and stored name to the nameUrlPairs list
				# as a tuple
				nameUrlPairs.append((currentUrl,storedName))
				

for pair in nameUrlPairs:
	print pair
	cmd = ['wget', '-O', pair[1], '--no-check-certificate', pair[0]]
	p = Popen(cmd)
	p.wait()



# These dates could not be parsed by datetime.strptime()
# They're likely the result of a formatting error, so you'll
# need to download/save them manually.
print '\n\nDates that could not be parsed: '
print '(You will need to download/save these files manually)'
for i in range(0,len(problemDates)):
	print '   ' + str(i+1) + '. ' + problemDates[i]
print '\n\n'



