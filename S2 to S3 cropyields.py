import pyodbc, time
from datetime import datetime

conx = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-2LIFDKO;'
                        'Database=cropdata;'
                        'Trusted_connection=yes;',
                        autocommit=True)

print('Connection is stablishedn\n\n')

cursor = conx.cursor()

selectStatement = '''
                    SELECT countryCode, countryDescription, decade,
                        CONVERT(DECIMAL(8,4), SUM(barley_actual_yield)) as sum_barley_actual_yield, 
                        CONVERT(DECIMAL(8,4), SUM(rye_actual_yield)) as sum_rye_actual_yield, 
                        CONVERT(DECIMAL(8,4), SUM(wheat_actual_yield)) as sum_wheat_actual_yield, 
                        CONVERT(DECIMAL(8,4), SUM(ferrtilizer_consumption)) as sum_fertilizer_consumption, 
                        CONVERT(DECIMAL(8,4), SUM(pesticides_indicator)) as sum_pesticides_indicator
                    FROM target_table
                    GROUP BY countryCode, countryDescription, decade
                    '''

selectTable = cursor.execute(selectStatement).fetchall()
print('Table selected\n\n')

'''
# Source Table Structure Cursor Documentation
#   0   [code] from fertilizers
#   1	[entity] from [S1 fertilizer]
#   2   [year] from fertilizers
#   3	[barley_actual_yield] from [S1 fertilizer]
#	4   [rye_actual_yield] from [S1 fertilizer]
#   5   [wheat_actual_yield] from [S1 fertilizer]
#   6   [fertilizer_consumption] from fertilizer
#   7   [pesticides_indicator] from pesticides
'''

username = 'Amir Irani'

insertStatement = '''
                    INSERT INTO [cropdata].[dbo].[CerealCropYieldData]
                        (
                        CountryCode,
                        CountryDescription,
                        Decade,
                        IncompleteWarning,
                        BarleyActualYield,
                        RyeActualYield,
                        WheatActualYield,
                        FertilizerKgHa,
                        PesticideKgHa,
                        InsertedBy,
                        InsertedDate)
                    VALUES(?,?,?,?,?,?,?,?,?,?,?)
                    '''

print('Writing to the target table initializing...\n\n')
time.sleep(3)

for row in selectTable:
    currenttimestamp = datetime.now()
    incompleteWarning = 'N'
    for item in row:
        if item == None or item == '':
            incompleteWarning = 'Y'
    
    cursor.execute(insertStatement, row[0], row[1], row[2], incompleteWarning, row[3], row[4], row[5], row[6], row[7], username, currenttimestamp)

    pass
print('\n FInallyyyyy after 7 days DOne!!!!!!!!!')