-- Find out the program ID of Selfhelp Austin Senior Center
-- Use the ID to restrict your data pulling
-- Find out "Registration Table"
-- Pull out top 100 clients records in Registration Table
-- Just pull out any records related to the status of the client in the Registration Table
-- pull out creator or modifier info from Registration Table
-- Find out "Contact" table
-- Pull out top 100 clients records in Contact Table
-- Just pull out contact_id, name, gender, dob and creator or modifier info from Contact table
-- combine records from registration and contact tables


import pyodbc
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=DFTASTARS\DFTASTARS;'
                      'DATABASE=CLIENTDB;'
                      'UID=resuser;'
                      'PWD=res@123;')

import pandas as pd

df = pd.read_sql_query ('''

select top 10 *
from PROGRAM
where program_name like '%austin%'

'''
, conn)

print(df)
