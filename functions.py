import pandas as pd

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
 
def checkif_notNull(check,db_name, table_name, column_name, engine, db_type = 'sqlserver', schema = 'dbo'):
    if db_type == 'mysql':
        query = f"select {column_name} from {db_name}.{table_name}"
    elif db_type == 'sqlserver':
        query = f"select {column_name} from recruitcrm_normlized.dbo.{table_name}"
    df = pd.read_sql(query, engine)
    return not ( df[column_name].isnull().any() or (df[column_name] == '').any() )

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