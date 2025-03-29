import pyodbc
import pandas as pd
from sqlalchemy import create_engine, text
# import urllib.parse
from conditions import *
from config import mysql_config
from functions import * 
# import sqlite3

#connecting to databases
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

# checklog_df - to store final result of all checks
resPairsCandidate = []
resPairsCompany = []
resPairsContact = []
resPairsJob = []
resPairsDeal = []

def logToExcel(tblname, col, check, res):
    if tblname == 'candidate' or tblname == 'candidate_custom_data':
        resPairsCandidate.append((col, check, res))
    if tblname == 'company' or tblname == 'company_custom_data':
        resPairsCompany.append((col, check, res))
    if tblname == 'contact' or tblname == 'contact_custom_data':
        resPairsContact.append((col, check, res))
    if tblname == 'job' or tblname == 'job_custom_data':
        resPairsJob.append((col, check, res))
    if tblname == 'deal' or tblname == 'deal_custom_data':
        resPairsDeal.append((col, check, res))
    

checklog_df = pd.DataFrame()

# This loop checks all non-custom fields ??
for table_name, df in tables.items():
    print('------------'+table_name+'-------------')
    for col, checks in df.items():
        exists = ((tblcol['TABLE_NAME']==table_name) & (tblcol['COLUMN_NAME']==col)).any()
        if(exists):
            for check in checks:
                if((check != '') & (check != 'mandatory')):
                    res = globals()["checkif_" + check.split(':')[0]](check,mysql_config['database'],table_name, col, engine, 'mysql','dbo')
                    print("%s %s %s"%(col, check, res))
                    logToExcel(table_name, col, check, res)
                    # resPairs.append((col, check, res))
        elif('mandatory' in checks.to_list()):
            res = '''ERROR: doesn't exist'''
            # resPairsCandidate.append(table_name, col, check, res)
            logToExcel(table_name, col, check, res)
            print(col + ' : ' + res)


# # for custom fields checking through tblextrafields query
if tblextrafields != '':
    # Connect to a SQLite database (or create it if it doesn't exist)
    # connection = sqlite3.connect('recruitcrm_normlized.db')
    # cursor = connection.cursor()  # Create a cursor object

    # Define the SQL query to create the table
    print("db_name: checkpoint 0")
    query = text(f"""
    CREATE TABLE IF NOT EXISTS {db_name}.tblextrafields (
        columnid INTEGER,
        accountid INTEGER,
        entitytypeid INTEGER,
        extrafieldname TEXT,
        extrafieldtype TEXT,
        defaultvalue TEXT
    )
    """)

    # Execute the query
    # cursor.execute(query)
    # connection.commit()
    print("db_name: checkpoint 1")


    with engine.connect() as connection:
        connection.execute(query)

  # Execute each statement separately
    for statement in tblextrafields.strip().split(';'):
        if statement.strip():  # Check if the statement is not empty
            with engine.connect() as connection:
                connection.execute(text(statement))
                connection.commit()  # Commit changes manually
        #     cursor.execute(statement)
        #  connection.commit()

    custom_tables = {
        2: 'contact_custom_data',
        3: 'company_custom_data',
        4: 'job_custom_data',
        5: 'candidate_custom_data'
    }
    print("db_name: checkpoint 2")
        # Query to select all records from tblextrafields
    select_query = text(f"SELECT * FROM " + db_name + ".tblextrafields")
    # cursor.execute(select_query)
    # records = cursor.fetchall()
    with engine.connect() as connection:
        result = connection.execute(select_query)
        records = result.fetchall()
    
    for record in records:
        for check in extrafieldchecks[record[4]]:
            if(check!=''):
                col = 'custcolumn' + str(record[0])
                check = check if check != 'dropdown' and check != 'multiselect' else check+':'+str(record[5])
                res = globals()["checkif_" + check.split(':')[0]](check,mysql_config['database'],custom_tables[record[2]], 'custcolumn' + str(record[0]), engine, 'mysql','dbo')
                print("%s %s %s"%(col, check, res))
                # resPairs.append((col, check, res))
                logToExcel(custom_tables[record[2]], col, check, res)


    drop_table_query = text("DROP TABLE IF EXISTS tblextrafields;")
    # cursor.execute(drop_table_query)
    with engine.connect() as connection:
        result = connection.execute(drop_table_query)
    connection.commit()

    # cursor.close()
    connection.close()

# print(resPairs)
# pd.DataFrame(resPairsCandidate, columns=['Column', 'Check', 'Result']).to_csv('checklog2.csv', index=False)
# checklog_df.to_csv('checklog.csv', index=False)

excel_path = "output.xlsx"
with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
    pd.DataFrame(resPairsCandidate, columns=['Column', 'Check', 'Result']).to_excel(writer, sheet_name='Candidate', index=False)  # Sheet 1
    pd.DataFrame(resPairsCompany, columns=['Column', 'Check', 'Result']).to_excel(writer, sheet_name='Company', index=False)   # Sheet 2
    pd.DataFrame(resPairsContact, columns=['Column', 'Check', 'Result']).to_excel(writer, sheet_name='Contact', index=False)   # Sheet 2
    pd.DataFrame(resPairsJob, columns=['Column', 'Check', 'Result']).to_excel(writer, sheet_name='Job', index=False)   # Sheet 2
    pd.DataFrame(resPairsDeal, columns=['Column', 'Check', 'Result']).to_excel(writer, sheet_name='deal', index=False)   # Sheet 2
    # resPairsCompany.to_excel(writer, sheet_name='Contact', index=False)   # Sheet 2
    # resPairsJob.to_excel(writer, sheet_name='Job', index=False)   # Sheet 2





