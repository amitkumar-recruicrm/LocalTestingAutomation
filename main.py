import pyodbc
import pandas as pd
from sqlalchemy import create_engine
# import urllib.parse
from conditions import *
from config import mysql_config
from functions import * 
import sqlite3

# encoded_password = urllib.parse.quote_plus('12345678')

platform = 'MySQL'

if platform == 'MySQL':
    engine = create_engine(f"mysql+mysqlconnector://{mysql_config['user']}:{mysql_config['password']}@{mysql_config['host']}/{mysql_config['database']}")
    # f"mysql+mysqlconnector://{db_config['user']}:{encoded_password}@localhost/recruitcrm_normlized"
elif platform == 'sqlserver':
    engine = create_engine(f"mssql+pyodbc://testAccount_2:12345678@localhost/fortisresourcesbh_cl?driver=ODBC+Driver+17+for+SQL+Server")

db_name = mysql_config['database']
def get_all_tables_and_columns(engine):
    query = f"""
        SELECT TABLE_NAME, COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = '{db_name}'
        """
    # print(pd.read_sql(query, conn))
    return pd.read_sql(query, engine)

tblcol = pd.DataFrame(get_all_tables_and_columns(engine))

checklog_df = pd.DataFrame()

for table_name, df in tables.items():
    print('------------'+table_name+'-------------')
    for col, checks in df.items():
        exists = ((tblcol['TABLE_NAME']==table_name) & (tblcol['COLUMN_NAME']==col)).any()
        if(exists):
            for check in checks:
                if((check != '') & (check != 'mandatory')):
                    res = globals()["checkif_" + check.split(':')[0]](check,mysql_config['database'],table_name, col, engine, 'mysql','dbo')
                    # print("%s %s"%(col, res))
                    df = pd.concat([df, pd.DataFrame([{"Col Name": col, "Remark": res}])], ignore_index=True)
                    # print(df)
        elif('mandatory' in checks.to_list()):
            print(col + ''' : ERROR: doesn't exists''')

# for custom fields checking through tblextrafields query
if tblextrafields != '':
    # Connect to a SQLite database (or create it if it doesn't exist)
    connection = sqlite3.connect('recruitcrm_normlized.db')

    # Create a cursor object
    cursor = connection.cursor()

    # Define the SQL query to create the table
    query = """
    CREATE TABLE IF NOT EXISTS tblextrafields (
        columnid INTEGER,
        accountid INTEGER,
        entitytypeid INTEGER,
        extrafieldname TEXT,
        extrafieldtype TEXT,
        defaultvalue TEXT
    )
    """

    # Execute the query
    cursor.execute(query)
    connection.commit()

  # Execute each statement separately
    for statement in tblextrafields.strip().split(';'):
        if statement.strip():  # Check if the statement is not empty
            cursor.execute(statement)
    connection.commit()

    custom_tables = {
        2: 'contact_custom_field_data',
        3: 'company_custom_field_data',
        4: 'job_custom_field_data',
        5: 'candidate_custom_field_data'
    }
        # Query to select all records from tblextrafields
    select_query = "SELECT * FROM tblextrafields"
    cursor.execute(select_query)
    records = cursor.fetchall()
    
    for record in records:
        for check in extrafieldchecks[record[4]]:
            if(check!=''):
                print("%s %s"%('custcolumn' + str(record[0]), globals()["checkif_" + check.split(':')[0]](check,mysql_config['database'],custom_tables[record[2]], 'custcolumn' + str(record[0]), engine, 'mysql','dbo')))



    drop_table_query = "DROP TABLE IF EXISTS tblextrafields;"
    cursor.execute(drop_table_query)
    connection.commit()

    cursor.close()
    connection.close()





