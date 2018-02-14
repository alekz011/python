#! /usr/bin/python3

# excel.py  


import openpyxl, pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

# Fill in countryData with each contryś population and tracts

print('Reading rows...')
for row in range(2, sheet.max_row + 1):
   # Each row in the spreadsheet has data for one census tract.
   state = sheet['B' + str(row)].value
   county = sheet['C' + str(row)].value
   pop = sheet['D' + str(row)].value

# Make sure the key for this state exists
   countyData.setdefault(state, {})
   
   # Make sure the key for this country in this state exists.
   countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

   # Eacht row represents one census tract, so increment by one.
   countyData[state][county]['tracts'] += 1

   # Increase the country pop by pop in this census tracts.
   countyData[state][county]['pop'] += int(pop)


# Open a new text file and write the content of countryData to it.

print('Writing results...')
resultFile = open('census2018.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')

