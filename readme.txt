# Steps to run the script: 
## INSTALL ALL DEPENDENCIES: pip install -r requirements.txt

## ADD CONFIGURATION AND CREDENTIALS
    1. Add database configurations. 
    2. Add file path for Initail data excel sheet download from retool.
    3. Add insert statements of tbletrafields prepared for testing. 
    4. Set platform value according to database. MySQL or sqlserver.
    5. Command to run the script: python3 main.py [for mac]

    OPTIONAL
    6. Edit tablenames if it doesn't match. Naming method we use on retool is used here too. [conditions.py ]

## RUN THE SCRIPT: python main.py