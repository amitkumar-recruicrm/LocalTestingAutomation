import pandas as pd
from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError

type_mapping = {
    'int': int,
    'bool': bool,
    'float': float
}

# column should contain only unique/distinct values
def checkif_unique(check,db_name, table_name, column_name, engine, db_type = 'sqlserver', schema = 'dbo'):
    if db_type == 'MySQL':
        query = f"select {column_name} from {db_name}.{table_name}"
    elif db_type == 'sqlserver':
        query = f"select {column_name} from {db_name}.{schema}.{table_name}"
    elif db_type == 'postgres':
        query = f"select {column_name} from {schema}.{table_name}"
    df = pd.read_sql(query, engine)
    return df[column_name].is_unique

# column should not contain any blank or NULL values
def checkif_notNull(check,db_name, table_name, column_name, engine, db_type = 'sqlserver', schema = 'dbo'):
    if db_type == 'MySQL':
        query = f"select {column_name} from {db_name}.{table_name}"
    elif db_type == 'sqlserver':
        query = f"select {column_name} from {db_name}.{schema}.{table_name}"
    elif db_type == 'postgres':
        query = f"select {column_name} from {schema}.{table_name}"
    df = pd.read_sql(query, engine)
    return not ( df[column_name].isnull().any() or (df[column_name] == '').any() )

# checks if character length of column exceeding the provided limit
def checkif_length(check,db_name, table_name, column_name, engine, db_type = 'sqlserver', schema = 'dbo'):
    if db_type == 'MySQL':
        query = f"select {column_name} from {db_name}.{table_name}"
    elif db_type == 'sqlserver':
        query = f"select {column_name} from {db_name}.{schema}.{table_name}"
    elif db_type == 'postgres':
        query = f"select {column_name} from {schema}.{table_name}"
    df = pd.read_sql(query, engine)
    return not ( df[column_name].astype(str).str.len().max() > int(check.split(':')[1]))

    # check if all the non-null values in the field follows provided pattern
def checkif_followsPattern(check,db_name, table_name, column_name, engine, db_type = 'sqlserver', schema ='dbo'):
    if db_type == 'MySQL':
        query = f"select {column_name} from {db_name}.{table_name} where {column_name} not regexp '{check.split(':')[1]}' and {column_name} != ''"
    elif db_type == 'sqlserver':
        query = f"select {column_name} from {db_name}.{schema}.{table_name} where {column_name} not like '{check.split(':')[2]}' and {column_name} != ''"
    elif db_type == 'postgres':
        query = text(f"select {column_name} from {schema}.{table_name} where {column_name} !~ :pattern and {column_name} != ''")
        print(query)
    df = pd.read_sql(query, engine, params={'pattern': check.split(':')[1]})
    return df[column_name].empty

# checks if all the values are of a particular datatype or not
def checkif_datatype(check,db_name, table_name, column_name, engine, db_type = 'sqlserver', schema ='dbo'):
    if db_type == 'MySQL':
        query = f"select {column_name} from {db_name}.{table_name} where {column_name} != ''"
    elif db_type == 'sqlserver':
        query = f"select {column_name} from {db_name}.{schema}.{table_name} where {column_name} is not null"
    elif db_type == 'postgres':
        query = f"select {column_name} from {schema}.{table_name} where {column_name} is not null"
    df = pd.read_sql(query, engine)
    check_type = type_mapping.get(check.split(':')[1])
    if check.split(':')[1] == 'float': #or check.split(':')[1] == 'int':
        # return df[column_name].apply(lambda x: isinstance(x, float)).all() # and df[column_name].apply(lambda x: str(x).split('.')[1] if '.' in str(x) else '').str.len() <= 2  
        return df[column_name].apply(lambda x: isinstance(x, (int, float)) and round(float(x), 2) == float(x)).all()
    return df[column_name].apply(lambda x: isinstance(x, check_type)).all()

# returns true if column only contains provided values. (single value)
def checkif_dropdown(check,db_name, table_name, column_name, engine, db_type = 'sqlserver', schema ='dbo'):
    condition = check.split(':')[1].replace("'","''").replace(",","','")
    if db_type == 'MySQL':
        query = f"select {column_name} from {db_name}.{table_name} where {column_name} != '' and {column_name} not in  ('{condition}')"
    elif db_type == 'sqlserver':
        query = f"select {column_name} from {db_name}.{schema}.{table_name} where {column_name} != '' and {column_name} not in  ('{condition}')"
    elif db_type == 'postgres':
        query = f"select {column_name} from {schema}.{table_name} where {column_name} is not null and {column_name} not in ('{condition}')"
        print(query)
    df = pd.read_sql(query, engine)
    return df[column_name].empty

# returns true if column follows provided pattern.
def checkif_followsCondition(check,db_name, table_name, column_name, engine, db_type = 'sqlserver', schema ='dbo'):
    condition = check.split(':')[1]
    if db_type == 'MySQL':
        query = f"select {column_name} from {db_name}.{table_name} where not ({condition})"
    elif db_type == 'sqlserver':
        query = f"select {column_name} from {db_name}.{schema}.{table_name} where not ({condition})"
    elif db_type == 'postgres':
        query = f"select {column_name} from {schema}.{table_name} where not ({condition})"
    df = pd.read_sql(query, engine)
    return df[column_name].empty

# returns true if column consists of only provided values (single or multiple values)
def checkif_multiselect(check,db_name, table_name, column_name, engine, db_type = 'sqlserver', schema ='dbo'):
    
    condition = check.split(':')[1].replace("'","''").replace(",","','")
    if db_type == 'MySQL':
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

    elif db_type == 'sqlserver':
        query = f"""
            with cte as (
                SELECT import_slug, value 
                FROM {db_name}.{schema}.{table_name}
                CROSS APPLY STRING_SPLIT({column_name}, ',')
            )
            SELECT DISTINCT value as {column_name}
            FROM cte
            WHERE value NOT IN ('{condition}')
        """
    
    elif db_type == 'postgres':
        query = f"""
            with cte as (
                SELECT import_slug, unnest(string_to_array({column_name}, ',')) AS value
                FROM {schema}.{table_name}
            )
            SELECT DISTINCT value as {column_name}
            FROM cte
            WHERE value NOT IN ('{condition}')
        """

    df = None
    try:
        df = pd.read_sql(query, engine)
    except ProgrammingError as e:
        print(e.orig)
    except Exception as e:
        print('Error:', e )

    # return df[column_name].empty
    if df is not None and column_name in df.columns:
        return df[column_name].empty
    else:
        return False
