import re
import pyodbc

conx = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-2LIFDKO;'
                        'Database=cropdata;'
                        'Trusted_connection=yes;',
                        autocommit=True)

print('Connection is stablished')


def actual_yield(crop, row):
    if crop == 'barley':
        result = row[2] - row[5]
    elif crop =='rye':
        result = row[3] - row[6]
    else:
        result = row[4] - row[7]
    if result == 0:
        result = None
    return result


cursor = conx.cursor()

selectStatement = '''
                select  * from cropyield
                    where entity in ('United States', 'Canada', 'Mexico')
                    '''

cursor.execute(selectStatement)

cropRow = cursor.fetchall()
croplist = ['barley', 'rye', 'wheat']

for row in cropRow:
    actual_yield(croplist, row)

    insertStatement = '''
                    INSERT INTO [cropdata].[dbo].[S1 fertilizers]
                        VALUES (?,?,?,?,?)'''

    cursor2.execute(insertStatement, row[0], row[1], barley_actual_yield, rye_actual_yield, wheat_actual_yield)



