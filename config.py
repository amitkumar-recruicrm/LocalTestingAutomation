# MySQL database connection configuration
mysql_config = {
    'user': 'root',
    'password': '12345678',
    'host': 'localhost',
    'database': 'HouseholdStaffing_CL'
}

# SQL Server database connection configuration
sqlserver_config = {
    'server': 'localhost',
    'database': 'KMRRecJA_CL',
    'user': 'sa',
    'password': 'Amit@1234'
}

platform = 'sqlserver'
# platform = 'MySQL'

schema = 'cleaned'

# Replace with your actual file path for xlsx file of Initial data download from retool.
file_path = "/Users/amit/Documents/Work/Data Migrations/completed/KMR Rec (JobAdder)/Initial_data 70963 (KMR Recruitment ) 4.xlsx" 
# file_path = "/Users/amit/Documents/Work/Data Migrations/completed/Ambacia (LOXO)/Initial_data 23625 (Ambacia) 2.xlsx"
# file_path = "/Users/amit/Documents/Work/Data Migrations/completed/household staffing (CATS)/Initial_data 62825 (householdstaffing) 5.xlsx"

# Add all entries in a single insert statement - This is used for custom fields type and values #
tblextrafields = """


"""