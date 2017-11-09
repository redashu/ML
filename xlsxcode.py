#!/usr/bin/python3

import  pandas as pd
#  loading xlsx file
file=pd.ExcelFile('cert.xlsx')

#  sheet names printing
print(file.sheet_names)
#  parsing on behalf of sheet  and storing output 
output1=file.parse('Sheet1')

#  print complete sheet

print(output1)

#  print only specific column

print(output1['COLLAGE'])
