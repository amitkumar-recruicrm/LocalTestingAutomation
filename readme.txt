Steps to run the script: 
    1. Add database configurations. [config.py]
    2. Add file path for Initail data excel sheet download from retool. [ conditions.py ]
    3. Add insert statements of tbletrafields prepared for testing. [ conditions.py ]
    4. Edit tablenames if it doesn't match. Naming method we use on retool is used here too. [conditions.py ]
    5. Set platform value according to database. MySQL or sqlserver. [ main.py ] 
    6. Command to run the script: python3 main.py [for mac]