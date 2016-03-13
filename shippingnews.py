# Import libraries
import urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen("http://www.poal.co.nz/shipping_cargo/vesselsinport.asp") # Fetch the page with urllib2
html = response.read() # Read the page

soup  = BeautifulSoup(html)  # Load HTML into BeautifulSoup
table = soup.find('table')   # Ask BeautifulSoup to find the first table it sees in the HTML
rows  = table.find_all('tr') # Finds all the rows in the table

out_table = [] # Make an empty output table

for row in rows:             # Go through each row and...
  out_row = []               # Make an empty output row
  cells = row.find_all('td') # Get all the cells from this row
  for cell in cells:         # Go through each cell and...
    out_row += [cell.text]   # Add the text of each cell to the output row
  out_table += [out_row]     # Add the output row to the output table


for r in out_table:
  print ",".join(r)

#print out_table # Print the output table


