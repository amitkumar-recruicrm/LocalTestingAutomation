import pandas as pd
from sqlalchemy import text

type_mapping = {
    'int': int,
    'bool': bool,
    'float': float
}

def checkif_unique(check,db_name, table_name, column_name, engine, db_type = 'sqlserver', schema = 'dbo'):
    if db_type == 'mysql':
        query = f"select {column_name} from {db_name}.{table_name}"
    elif db_type == 'sqlserver':
        query = f"select {column_name} from recruitcrm_normlized.dbo.{table_name}"
    df = pd.read_sql(query, engine)
    return df[column_name].is_unique

# column should not contain any blank or NULL values
def checkif_notNull(check,db_name, table_name, column_name, engine, db_type = 'sqlserver', schema = 'dbo'):
    if db_type == 'mysql':
        query = f"select {column_name} from {db_name}.{table_name}"
    elif db_type == 'sqlserver':
        query = f"select {column_name} from recruitcrm_normlized.dbo.{table_name}"
    df = pd.read_sql(query, engine)
    return not ( df[column_name].isnull().any() or (df[column_name] == '').any() )

# checks if character length of column exceeding the limit
def checkif_length(check,db_name, table_name, column_name, engine, db_type = 'sqlserver', schema = 'dbo'):
    if db_type == 'mysql':
        query = f"select {column_name} from {db_name}.{table_name}"
    elif db_type == 'sqlserver':
        query = f"select {column_name} from recruitcrm_normlized.dbo.{table_name}"
    df = pd.read_sql(query, engine)
    return not ( df[column_name].str.len().max() > int(check.split(':')[1]))


def checkif_followsPattern(check,db_name, table_name, column_name, engine, db_type = 'sqlserver', schema ='dbo'):
    query = f"select {column_name} from {db_name}.{table_name} where {column_name} not regexp '{check.split(':')[1]}' and {column_name} != ''"
    df = pd.read_sql(query, engine)
    return df[column_name].empty

def checkif_datatype(check,db_name, table_name, column_name, engine, db_type = 'sqlserver', schema ='dbo'):
    query = f"select {column_name} from {db_name}.{table_name} where {column_name} != ''"
    df = pd.read_sql(query, engine)
    check_type = type_mapping.get(check.split(':')[1])
    if check.split(':')[1] == 'float':
        return df[column_name].apply(lambda x: isinstance(x, float)).all() #and df[column_name].apply(lambda x: str(x).split('.')[1] if '.' in str(x) else '').str.len() > 2  
    return df[column_name].apply(lambda x: isinstance(x, check_type)).all()

def checkif_dropdown(check,db_name, table_name, column_name, engine, db_type = 'sqlserver', schema ='dbo'):
    condition = check.split(':')[1].replace(",","','")
    query = f"select {column_name} from {db_name}.{table_name} where {column_name} != '' and {column_name} not in  ('{condition}')"
    df = pd.read_sql(query, engine)
    return df[column_name].empty

def checkif_multiselect(check,db_name, table_name, column_name, engine, db_type = 'sqlserver', schema ='dbo'):
    condition = check.split(':')[1].replace(",","','")
    print("-----------------")
    print(condition)
    print("-----------------")
    # query = f"select {column_name} from {db_name}.{table_name} where {column_name} != '' and {column_name} not in  ('{condition}')"
    query = f"""
        WITH RECURSIVE cte AS (
            -- Initial row extraction
            SELECT 
                import_slug,
                TRIM(SUBSTRING_INDEX({column_name}, ',', 1)) AS value,
                SUBSTRING({column_name}, LOCATE(',', {column_name}) + 1) AS remaining
            FROM {db_name}.{table_name}
            
            UNION ALL
            
            -- Recursive extraction of remaining values
            SELECT 
                import_slug,
                TRIM(SUBSTRING_INDEX(remaining, ',', 1)) AS value,
                CASE 
                    WHEN LOCATE(',', remaining) > 0 
                    THEN SUBSTRING(remaining, LOCATE(',', remaining) + 1) 
                    ELSE NULL 
                END AS remaining  -- Avoids infinite loop
            FROM cte
            WHERE remaining IS NOT NULL AND remaining != ''
        )
        SELECT DISTINCT value as {column_name}
        FROM cte
        WHERE value NOT IN ('{condition}')
        ;
        """

    
    with engine.connect() as connection:
        connection.execute(text("SET SESSION cte_max_recursion_depth = 50000;")) 

    df = pd.read_sql(query, engine)
    return df[column_name].empty


# def checkif_followsPattern(table_name, column_name, engine, db_type = 'sqlserver', schema ='dbo'):
#     if db_type == 'mysql':
#         if 'email' in column_name:
#             query = f"select {column_name} from recruitcrm_normlized.{table_name} where {column_name} not like '%_@%_.%_'"
#         elif 'contactnumber' in column_name:
#             query = f"select {column_name} from recruitcrm_normlized.{table_name} where {column_name} not regexp '[0-9]'"
#     elif db_type == 'sqlserver':
#         query = f"select {column_name} from recruitcrm_normlized.dbo.{table_name}"
#     df = pd.read_sql(query, engine)
#     return not ( df[column_name].isnull().any() or (df[column_name] == '').any() )