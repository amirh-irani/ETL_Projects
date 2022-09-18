import csv
from datetime import datetime
from itertools import count
import pyodbc

conx = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-2LIFDKO;'
                        'Database=cropdata;'
                        'Trusted_connection=yes;',
                        autocommit=True)

print('Connection is stablished')

cursor = conx.cursor()

with open('pesticide-use-per-hectare-of-cropland.csv', newline='') as pesticides: 
    csvreader = csv.reader(pesticides)
    
    counter = 0
    for line in csvreader:
        if (line[1] == 'Code'):
                continue
        
        line[2] = datetime.strptime(str(line[2]), '%Y')
        cursor.execute('INSERT INTO pesticides VALUES (?,?,?,?)', line[0], line[1], line[2], line[3])
        counter += 1
    
    print(counter, ' number inserted into table')

