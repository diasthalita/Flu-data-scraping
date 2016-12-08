##============================================================================== 
# File:         californiarun.sh 
# Date:         Thu Dec  8 10:05:25 EST 2016
# Author(s):    Thalita Coleman  <thalitaneu@gmail.com>
# Abstract:		 Executes programs california.py and parsecalifornia.py. Parses the file cali1.htm  -- which contains the HTML source for the page https://www.cdph.ca.gov/data/statistics/Pages/CISPDataArchive.aspx -- and returns the URL of all weekly flu reports. Downloads the flu reports in .pdf format and transforms into .txt. Deletes files prior to 2012. Scrapes the .txt files and returns a CSV file named californiaresults.csv with "Week", "Week Ending", "State", "Season", "Total", "Lab", "Visits", and "Hospitalizations" data for each week. When the data is not available in the report, it returns N/A value. When the program was not able to parse the data, it returns a "could not retrieve" message. The "could not retrieve" values can then be collected manually.		 
#------------------------------------------------------------------------------ 
# Requirements: Python 2.7, 
#------------------------------------------------------------------------------ 
# Notes: 
#============================================================================== 

# defines output file
CSV="californiaresults.csv"

# removes previous californiaresults.csv files, if any
rm -i $CSV

# downloads .csv files
./california.py

# removes files prior to 2011
find . -name "2008*" -o -name "2009*" -o -name  "2010*" -o -name "2011*" | xargs rm -f

# transform files into .txt, parse files and creates californiaresults.csv file with the data.
for file in *.pdf
do
		echo "Parsing file $file..."
        textfile=`echo "$file" | sed 's/.pdf/.txt/'`
        pdf2txt.py -t text -o "$textfile" "$file"
        ./parsecalifornia.py "$textfile" >> californiaresults.csv
done

