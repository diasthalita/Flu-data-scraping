Make sure you are using Python 2 and that PDFMiner (https://pypi.python.org/pypi/pdfminer/) is installed and on path. 

To get started, run the californiarun.sh script. Once it is finished, open the californiaresults.csv file.

Because the reports are not consistent, not all data can be retrieved automatically. Please find below information about the data that needs to be extracted manually:

1. The field "Ending Date" need to be cleaned manually. Entries like January 22-28, 2012 should read January 28, 2012, and so forth. 
2. The field "Season" needs to be completed manually. Seasons start around week 40 and end around week 20 of the following year.
3. Reports are not issued for every week of the season. Add missing weeks and complete blank fields with N/A.
4. All the fields that read "could not retrieve" needs to be completed manually.

