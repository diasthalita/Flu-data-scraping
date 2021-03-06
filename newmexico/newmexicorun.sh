
##============================================================================== 
# File:         newmexicorun.sh 
# Date:         Tue Nov 21 14:52:17 EST 2017
# Author(s):    Thalita Coleman  <thalitaneu@gmail.com>
# Abstract: Executes programs newmexico.py and parsenewmexico.py. 
#       Parses the html files containing the HTML source for
#       the page https://nmhealth.org/about/erd/ideb/isp/data/,
#       and returns the URL of all weekly flu reports. Downloads the flu reports 
#       in .pdf format and transforms into .txt. Deletes files prior to 2012. 
#       Scrapes the .txt files and returns a CSV file named newmexicoresults.csv 
#       with "Week", "Week Ending", "State", "Season", "Total", "Lab", "Visits", and 
#       "Hospitalizations" data for each week. When the data is not available in the report, 
#       it returns N/A value. When the program was not able to parse the data, it returns a 
#       "could not retrieve" message. The "could not retrieve" values can then be collected manually.        
#------------------------------------------------------------------------------ 
# Requirements: Python 2.7, PDFminer on path  
#------------------------------------------------------------------------------ 
# Notes: Don't forget to add PDFminer location to PATH 
#============================================================================== 

# defines path
#PATH=/home/tcoleman/venv/pdfminer/bin:$PATH
PATH=/your/path/to/pdfminer:$PATH

# defines output file 
CSV="newmexicoresults.csv"

# removes previous newmexicoresults.csv files, if any
rm -i $CSV

# writes header
echo '"Week", "Week Ending", "State", "Season", "Total", "Lab", "Visits", "Hospitalizations"' >> $CSV

# downloads .csv files
./newmexico.py

# removes files prior to 2011
find . -type f -name "2011*" -exec rm -f {} \;

# transforms files into .txt, parse files and creates delawareresults.csv file with the data
for file in *.pdf
do
		echo "parsing file $file..."
		textfile=`echo "$file" | sed 's/.pdf/.txt/'`
		pdf2txt.py -t text -o "$textfile" "$file"
		./parsenewmexico.py "$textfile" >> $CSV
done
			
			
