#! /usr/bin/python3

import csv, os

os.makedirs('headerRemoved' , exist_ok=True)

# Loop through every file in the current dir
for csvFilename in os.listdir('.'):
   if not csvFilename.endswith('.csv'):
       continue

   print('Removig header from ' + csvFilename + '...')

# Read the CSV file in (skipping first row)
   csvRow = []
   csvFileObj = open(csvFilename)
   readerObj = csv.reader(csvFileObj)
   for row in readerObj:
       if readerObj.line_num ==1:
           continue
       csvRow.append(row)
   csvFileObj.close()


# Write out the CSV file
   csvFileObj = open(os.path.join('headerRemoved',  csvFilename), 'w', newline='')
   csvWriter = csv.writer(csvFileObj)
   for row in csvRow:
       #csvWriter.writerrow(row)
       csvWriter.writerow(row)
   csvFileObj.close()

