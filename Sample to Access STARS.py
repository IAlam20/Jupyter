import pyodbc
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=DFTASTARS\DFTASTARS;'
                      'DATABASE=CLIENTDB;'
                      'UID=resuser;'
                      'PWD=res@123;')

import pandas as pd

df = pd.read_sql_query ('''

select *
from program

'''
, conn)

print(df)