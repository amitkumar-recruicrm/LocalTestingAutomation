import pyodbc
import pandas as pd
from sqlalchemy import create_engine, text
# import urllib.parse
from conditions import *
from config import mysql_config, sqlserver_config
from functions import * 
from urllib.parse import quote_plus
# import sqlite3

platform = 'sqlserver'
# platform = 'MySQL'
schema = 'dbo'

#connecting to databases
if platform == 'MySQL':
    engine = create_engine(f"mysql+mysqlconnector://{mysql_config['user']}:{mysql_config['password']}@{mysql_config['host']}/{mysql_config['database']}")
    # f"mysql+mysqlconnector://{db_config['user']}:{encoded_password}@localhost/recruitcrm_normlized"
elif platform == 'sqlserver':
    # for mac:
    # driver = "/usr/local/lib/libmsodbcsql.17.dylib"
    # engine = create_engine(f"mssql+pyodbc://{sqlserver_config['user']}:{quote_plus(sqlserver_config['password'])}@localhost/{sqlserver_config['database']}?driver={quote_plus(driver)}")
    # for windows
    engine = create_engine(f"mssql+pyodbc://{sqlserver_config['user']}:{quote_plus(sqlserver_config['password'])}@localhost/{sqlserver_config['database']}?driver={{ODBC Driver 17 for SQL Server}}")


db_name = mysql_config['database'] if platform == 'MySQL' else sqlserver_config['database']


def get_all_tables_and_columns(engine):
    query = ''
    if platform == 'MySQL':
        query = f"""
            SELECT TABLE_NAME, COLUMN_NAME
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = '{db_name}'
            """
    elif platform == 'sqlserver':
        query = f"""
            SELECT TABLE_NAME, COLUMN_NAME
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_CATALOG = '{db_name}'
            """
    # print(pd.read_sql(query, conn))
    return pd.read_sql(query, engine)

# tblcol = pd.DataFrame(get_all_tables_and_columns(engine))
tblcol = get_all_tables_and_columns(engine)

# checklog_df - to store final result of all checks
resPairsCandidate = []
resPairsCompany = []
resPairsContact = []
resPairsJob = []
resPairsDeal = []
resPairsNote = []
resPairsAssignment = []

def checkIfExists(tblname, colname, engine):
    if platform == 'MySQL':
        query = f"select column_name from information_schema.columns where column_name = '{colname}' and table_name = '{tblname}' and table_schema = '{db_name}';"
    elif platform == 'sqlserver':
        query = f"select column_name from information_schema.columns where column_name = '{colname}' and table_name = '{tblname}' and table_catalog = '{db_name}' and table_schema = '{schema}';"
    df = pd.read_sql(query, engine)
    return not ( df['column_name'].empty )

def logToExcel(tblname, col, check, res):
    if tblname == 'candidate' or tblname == 'candidate_custom_data':
        resPairsCandidate.append((col, check, res))
    elif tblname == 'company' or tblname == 'company_custom_data':
        resPairsCompany.append((col, check, res))
    elif tblname == 'contact' or tblname == 'contact_custom_data':
        resPairsContact.append((col, check, res))
    elif tblname == 'job' or tblname == 'job_custom_data':
        resPairsJob.append((col, check, res))
    elif tblname == 'job_assignment':
        resPairsAssignment.append((col, check, res))
    elif tblname == 'deal' or tblname == 'deal_custom_data':
        resPairsDeal.append((col, check, res))
    elif 'note' in tblname :
        resPairsNote.append((col, check, tblname,res))
    

checklog_df = pd.DataFrame()

# This loop checks all non-custom fields ??
for table_name, df in tables.items():
    print('------------'+table_name+'-------------')
    for col, checks in df.items():
        exists = ((tblcol['TABLE_NAME']==table_name) & (tblcol['COLUMN_NAME']==col)).any()
        if(exists):
            for check in checks:
                if((check != '') & (check != 'mandatory')):
                    res = globals()["checkif_" + check.split(':')[0]](check,db_name,table_name, col, engine, platform,'dbo')
                    print("%s %s %s"%(col, check, res))
                    logToExcel(table_name, col, check, res)
                    # resPairs.append((col, check, res))
        elif('mandatory' in checks.to_list()):
            res = '''ERROR: doesn't exist'''
            # resPairsCandidate.append(table_name, col, check, res)
            logToExcel(table_name, col, 'mandatory', res)
            print(col + ' : ' + res)


# # for custom fields checking through tblextrafields query
if tblextrafields != '':

    if platform == 'MySQL':
    # Define the SQL query to create the table
        drop_table_query = text("DROP TABLE IF EXISTS tblextrafields;")
        with engine.connect() as connection:
            result = connection.execute(drop_table_query)
            connection.commit()
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
    elif platform == 'sqlserver':
        drop_table_query = text(f"""
            IF OBJECT_ID('{schema}.tblextrafields', 'U') IS NOT NULL
                DROP TABLE {schema}.tblextrafields;
            """)
        with engine.connect() as connection:
            result = connection.execute(drop_table_query)
            connection.commit()
        query = text(f"""
                    IF NOT EXISTS (
                        SELECT * FROM INFORMATION_SCHEMA.TABLES 
                        WHERE TABLE_NAME = 'tblextrafields' 
                        AND TABLE_SCHEMA = '{schema}'
                        AND TABLE_CATALOG = '{db_name}'
                    )
                    BEGIN
                        CREATE TABLE {schema}.tblextrafields (
                            columnid INT,
                            accountid INT,
                            entitytypeid INT,
                            extrafieldname NVARCHAR(MAX),
                            extrafieldtype NVARCHAR(MAX),
                            defaultvalue NVARCHAR(MAX)
                        )
                    END
        """)

    with engine.connect() as connection:
        trans = connection.begin()
        try:
            print('--- check point query not exists--')
            connection.execute(query)
            trans.commit()
        except:
            trans.rollback()
            raise

  # Execute each statement separately
    for statement in tblextrafields.strip().split(';'):
        if statement.strip():  # Check if the statement is not empty
            with engine.connect() as connection:
                if platform == 'MySQL':
                    statement = statement.replace("INSERT INTO tblextrafields", f"INSERT INTO {db_name}.tblextrafields")
                elif platform == 'sqlserver':
                    statement = statement.replace("INSERT INTO tblextrafields", f"INSERT INTO {schema}.tblextrafields")
                connection.execute(text(statement + ';'))
                connection.commit()  # Commit changes manually
        #     cursor.execute(statement)
        #  connection.commit()

    custom_tables = {
        2: 'contact_custom_data',
        3: 'company_custom_data',
        4: 'job_custom_data',
        5: 'candidate_custom_data',
        11: 'deal_custom_data',
    }
    print("db_name: checkpoint 2")
        # Query to select all records from tblextrafields
    if platform == 'MySQL':
        select_query = text(f"SELECT * FROM {db_name}.tblextrafields")
    elif platform == 'sqlserver':
        select_query = text(f"SELECT * FROM {db_name}.{schema}.tblextrafields")
    # cursor.execute(select_query)
    # records = cursor.fetchall()
    with engine.connect() as connection:
        result = connection.execute(select_query)
        records = result.fetchall()
    
    for record in records:
        for check in extrafieldchecks[record[4]]:
            exists = ((tblcol['TABLE_NAME']==table_name) & (tblcol['COLUMN_NAME']==col)).any()
            if(check!=''):
                col = 'custcolumn' + str(record[0])
                check = check if check != 'dropdown' and check != 'multiselect' else check+':'+str(record[5])
                res = globals()["checkif_" + check.split(':')[0]](check,db_name,custom_tables[record[2]], 'custcolumn' + str(record[0]), engine, platform,'dbo')
                print("%s %s %s"%(col, check, res))
                # resPairs.append((col, check, res))
                logToExcel(custom_tables[record[2]], col, check, res)

    if platform == 'MySQL':
        drop_table_query = text("DROP TABLE IF EXISTS tblextrafields;")
    elif platform == 'sqlserver':
        drop_table_query = text(f"""
            IF OBJECT_ID('{schema}.tblextrafields', 'U') IS NOT NULL
                DROP TABLE {schema}.tblextrafields;
            """)
    # cursor.execute(drop_table_query)
    with engine.connect() as connection:
        result = connection.execute(drop_table_query)
        connection.commit()

    # cursor.close()
    connection.close()

excel_path = f"{db_name}_output.xlsx"
with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
    pd.DataFrame(resPairsCandidate, columns=['Column', 'Check', 'Result']).to_excel(writer, sheet_name='Candidate', index=False) 
    pd.DataFrame(resPairsCompany, columns=['Column', 'Check', 'Result']).to_excel(writer, sheet_name='Company', index=False) 
    pd.DataFrame(resPairsContact, columns=['Column', 'Check', 'Result']).to_excel(writer, sheet_name='Contact', index=False)  
    pd.DataFrame(resPairsJob, columns=['Column', 'Check', 'Result']).to_excel(writer, sheet_name='Job', index=False)  
    pd.DataFrame(resPairsAssignment, columns=['Column', 'Check', 'Result']).to_excel(writer, sheet_name='Assignment', index=False)  
    pd.DataFrame(resPairsDeal, columns=['Column', 'Check', 'Result']).to_excel(writer, sheet_name='deal', index=False)  
    pd.DataFrame(resPairsNote, columns=['Column', 'Check', 'Table_Name' ,'Result']).to_excel(writer, sheet_name='note', index=False)   
    # resPairsCompany.to_excel(writer, sheet_name='Contact', index=False)   # Sheet 2
    # resPairsJob.to_excel(writer, sheet_name='Job', index=False)   # Sheet 2





