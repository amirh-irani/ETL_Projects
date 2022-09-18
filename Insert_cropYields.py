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

with open('cropyield.csv', newline='') as cropyields: 
    csvreader = csv.reader(cropyields)
    
    counter = 0
    for line in csvreader:
        if (line[1] == 'Year'):
                continue
        line[1] = datetime.strptime(line[1], '%Y')
        cursor.execute('INSERT INTO cropyield VALUES (?,?,?,?,?,?,?,?)', line[0], 
        line[1], line[2], line[12], line[18], 
        line[20], line[21], line[19])
        counter += 1
    
    print(counter, ' number inserted into table')

