# MySQL database connection configuration
mysql_config = {
    'user': 'root',
    'password': '12345678',
    'host': 'localhost',
    'database': 'AmbaciaLX_CL'
}

# SQL Server database connection configuration
sqlserver_config = {
    'server': 'localhost',
    'database': 'KMRRecJA_CL',
    'user': 'sa',
    'password': 'Amit@1234'
}

# platform = 'sqlserver'
platform = 'MySQL'
schema = 'dbo'

# Replace with your actual file path for xlsx file of Initial data download from retool.
file_path = "/Users/amit/Documents/Work/Data Migrations/completed/Ambacia (LOXO)/Initial_data 23625 (Ambacia) 2.xlsx" 


# Add all entries in a single insert statement - This is used for custom fields type and values #
tblextrafields = """
-- ambacia - loxo

insert into tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
(1,23625,5,'Email Type','dropdown','Work,Personal'),
(2,23625,5,'Work Emails','text',null),
(3,23625,5,'Personal Emails','text',null),
(4,23625,5,'Phone Type','dropdown','Work,Personal'),
(5,23625,5,'Work Phones','phonenumber',null),
(6,23625,5,'Personal Phones','phonenumber',null),
(7,23625,5,'Rating','dropdown','✅ Recommended ✅,❌ Not;Recommended ❌,❓ Recommended With Restrain ❓,🔥 Highly Recommended 🔥,🚩 Black List 🚩'),
(8,23625,5,'Lists','multiselect','.NET B2B,Agents 1,Android b2b,B2B Aliens,B2B Product,Corporate,DevOps B2B,Ecommerce,Frontend B2B,Germany Targets,iOS B2B,Netherlands Targets,Newsletter,PHP B2B,QA B2B'),
(9,23625,5,'Record Type','multiselect','Candidate,Contact'),
(10,23625,5,'Comp','number',null),
(1,23625,3,'Global Status','dropdown','Current Client,Dead Opportunity,Do Not Prospect,In Progress'),
(2,23625,3,'Contact Person','text',null),
(3,23625,3,'Contact Person 2','text',null),
(4,23625,3,'Linkedin Profile 2','text',null),
(5,23625,3,'Email','text',null),
(6,23625,3,'Email 2','text',null),
(7,23625,3,'Position','text',null),
(8,23625,3,'Position 2','text',null),
(9,23625,3,'Status','dropdown','Active,Black List,Contacted,Meeting,Not In Business,Not Interested,Not Preferred,On Hold,Potential,Qualified Lead,Sent Offer'),
(10,23625,3,'Phones','phonenumber',null),
(11,23625,3,'Lists','multiselect','Dev Teams for Luminary,Luminary UK,Luminary US,Luminary/Other'),
(12,23625,3,'Scope of activities','text',null),
(13,23625,3,'Office location in croatia','text',null),
(14,23625,3,'All Addresses','longtext',null),
(1,23625,2,'Email Type','dropdown','Work,Personal'),
(2,23625,2,'Secondary Emails','text',null),
(3,23625,2,'Lists','multiselect','Agents 1,Apollo Croatia,CCI France,Corporate,Germany Targets,Incubators,Netherlands Targets,Start ups'),
(4,23625,2,'Rating','dropdown','✅ Recommended ✅,🔥 Highly Recommended 🔥'),
(5,23625,2,'Phone Type','dropdown','Work,Personal'),
(6,23625,2,'Work Phones','phonenumber',null),
(7,23625,2,'Personal Phones','phonenumber',null),
(8,23625,2,'Record Type','multiselect','Candidate,Contact'),
(1,23625,4,'Seniority Levels','multiselect','Entry,Mid Level,Senior,Director'),
(2,23625,4,'Opened date','date',null),
(3,23625,4,'Selection Process','text',null),
(1,23625,11,'Workflow','dropdown','IT Recruitment 2025,LuminaryIT 2024,Recruitment 2023,Recruitment 2024'),
(2,23625,11,'Currency','dropdown','EUR'),
(3,23625,11,'Job type','dropdown','Full Time'),
(4,23625,11,'Salary Currency','dropdown','EUR')


 """