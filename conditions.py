import pandas as pd

# Replace with your actual file path for xlsx file of Initial data download from retool.
file_path = "/Users/amit/Documents/Work/Data Migrations/in progress/Ambacia (LOXO)/Initial_data 23625 (Ambacia) 2.xlsx" 

# Load all sheets as a dictionary of DataFrames
dfs = pd.read_excel(file_path, sheet_name=None)

# Check available sheet names
# print(dfs.keys())
# ['Account_plan', 'user_details', 'hotlist_mapping', 'note_type_mapping', 'deal_stage_mapping', 'job_status_mapping', 'extra_field_mapping', 'calllog_type_mapping', 'meeting_type_mapping', 'contact_stage_mapping', 'custom_industry_mapping', 'candidate_status_mapping']

candidate_data = pd.DataFrame({
    "migration_reserved1" : ['notNull','mandatory','unique'],
    "firstname" : ['notNull','mandatory','length:60'],
    "lastname" : ['','','length:60'],
    "locality" : ['','','length:100'],
    "city" : ['','','length:50'],
    "state" : ['','','length:50'],
    "country" : ['','','length:50'],
    "slug" :      ['unique', 'notNull','mandatory'],
    "emailid"   : ['followsPattern:.*@.*[.].*:%_@%_.%','',''],
    "contactnumber" : ['followsPattern:[0-9]+:%[0-9]%','',''],
    "willingtorelocate": ['datatype:int','',''],
    "genderid": ['dropdown:0,1,2','',''],
    "salarytype": ['dropdown:1,2,3,4,5','',''],
    "currentsalary": ['datatype:float','',''],
    "salaryexpectation": ['datatype:float','',''],
    "noticeperiod": ['datatype:int','',''],
    "lastorganisation": ['length:300','',''],
    "position": ['length:100','',''],
    "address": ['length:500','',''],
    "createdon": ['notNull','mandatory','followsCondition:createdon<=updatedon'],
    "updatedon": ['notNull','mandatory',''],
    "createdby": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "updatedby": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "ownerid": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "accountid": ['notNull','mandatory','dropdown:'+",".join(dfs["Account_plan"]["accountid"].astype(str).tolist())],
})

candidate_custom_field_data = pd.DataFrame({
    "import_slug" : ['notNull','mandatory'],
    "candidate_id" : ['notNull','mandatory'], 
})

company_data = pd.DataFrame({
    "createdon" : ['notNull','',''],
    "slug" : ['unique', 'notNull','mandatory'],
    "industryid" : ['datatype:int', '',''],
    "companyname" : ['mandatory', 'notNull','length:300'],
    "address": ['length:500','',''],
    "createdon": ['notNull','mandatory','followsCondition:createdon<=updatedon'],
    "updatedon": ['notNull','mandatory',''],
    "createdby": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "updatedby": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "ownerid": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "accountid": ['notNull','mandatory','dropdown:'+",".join(dfs["Account_plan"]["accountid"].astype(str).tolist())],
    "city" : ['','','length:50'],
    "aboutcompany" : ['','','length:5000'],
})

company_custom_field_data = pd.DataFrame({
    "import_slug" : ['notNull','mandatory'],
    "company_id" : ['notNull','mandatory'], 
})

contact_data = pd.DataFrame({
    "migration_reserved1" : ['notNull','mandatory','unique'],
    "firstname" : ['notNull','mandatory','length:60'],
    "lastname" : ['','','length:60'],
    "city" : ['','','length:50'],
    "slug" :      ['unique', 'notNull','mandatory'],
    "email"   : ['followsPattern:.*@.*[.].*:%_@%_.%','',''],
    "contactnumber" : ['followsPattern:[0-9]+:%[0-9]%','',''],
    "designation": ['length:100','',''],
    "address": ['length:500','',''],
    "createdon": ['notNull','mandatory','followsCondition:createdon<=updatedon'],
    "updatedon": ['notNull','mandatory',''],
    "createdby": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "updatedby": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "ownerid": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "accountid": ['notNull','mandatory','dropdown:'+",".join(dfs["Account_plan"]["accountid"].astype(str).tolist())],
})

contact_custom_field_data = pd.DataFrame({
    "import_slug" : ['notNull','mandatory'],
    "contact_id" : ['notNull','mandatory'], 
})

job_data = pd.DataFrame({
    "migration_reserved1" : ['notNull','mandatory','unique'],
    "name" : ['notNull','mandatory','length:300'],
    "locality" : ['','','length:50'],
    "city" : ['','','length:50'],
    "state" : ['','','length:50'],
    "country" : ['','','length:50'],
    "postalcode" : ['','','length:20'],
    "slug" :      ['unique', 'notNull','mandatory'],
    "designation": ['length:100','',''],
    "address": ['length:500','',''],
    "salarytype": ['dropdown:annual,monthly,weekly,daily,hourly','',''],
    "job_type": ['dropdown:parttime,fulltime,contract,contracttopermanent','',''],
    "job_category": ['length:100','',''],
    "minexperienceinyears": ['datatype:int','',''],
    "maxexperienceinyears": ['datatype:int','',''],
    "annualsalarymin": ['datatype:float','',''],
    "annualsalarymax": ['datatype:float','',''],
    "jobstatus": ['notNull','mandatory','dropdown:'+",".join(dfs["job_status_mapping"]["id"].astype(str).tolist())],
    "createdon": ['notNull','mandatory','followsCondition:createdon<=updatedon'],
    "updatedon": ['notNull','mandatory',''],
    "createdby": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "updatedby": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "ownerid": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "accountid": ['notNull','mandatory','dropdown:'+",".join(dfs["Account_plan"]["accountid"].astype(str).tolist())],
})

job_custom_field_data = pd.DataFrame({
    "import_slug" : ['notNull','mandatory'],
    "job_id" : ['notNull','mandatory'], 
})

job_assignment_data = pd.DataFrame({
    "share" : ['notNull','mandatory',''],
    "candidatename" : ['notNull','mandatory',''],
    "candidateslug" : ['notNull','mandatory',''],
    "jobname" : ['notNull','mandatory',''],
    "jobslug" : ['notNull','mandatory',''],
    "companyname" : ['','mandatory',''],
    "companyslug" : ['','mandatory',''],
    "contactname" : ['','mandatory',''],
    "contactslug" : ['','mandatory',''],
    "remark" : ['','length:10000',''],
    "createdon": ['notNull','mandatory','followsCondition:createdon<=updatedon'],
    "updatedon": ['notNull','mandatory',''],
    "stagedate": ['notNull','mandatory',''],
    "candidatestatusid": ['notNull','mandatory','dropdown:'+",".join(dfs["candidate_status_mapping"]["id"].astype(str).tolist())],
    "createdby": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "updatedby": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "ownerid": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "accountid": ['notNull','mandatory','dropdown:'+",".join(dfs["Account_plan"]["accountid"].astype(str).tolist())],
})

deal_data = pd.DataFrame({
    "migration_reserved1" : ['notNull','mandatory','unique'],
    "name" : ['notNull','mandatory','length:300'],
    "dealvalue" : ['notNull','mandatory','datatype:float'],
    "slug" :  ['unique', 'notNull',''],
    "dealtype": ['dropdown:1,2','',''],
    "closedate": ['notNull','mandatory','followsCondition:createdon<=updatedon'],
    "createdon": ['notNull','mandatory',''],
    "updatedon": ['notNull','mandatory',''],
    "dealstage": ['notNull','mandatory','dropdown:'+",".join(dfs["deal_stage_mapping"]["id"].astype(str).tolist())],
    "createdby": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "updatedby": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "ownerid": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "accountid": ['notNull','mandatory','dropdown:'+",".join(dfs["Account_plan"]["accountid"].astype(str).tolist())],
})

deal_custom_field_data = pd.DataFrame({
    "import_slug" : ['notNull','mandatory'],
    "deal_id" : ['notNull','mandatory'], 
})

note_data = pd.DataFrame({
    "relatedto" : ['notNull','mandatory',''],
    "relatedtotypeid" : ['notNull','mandatory','dropdown:2,3,4,5,11'],
    "relatedtoname" : ['notNull','mandatory',''],
    "type" :  ['mandatory', 'notNull',''],
    "description": ['length:10000','',''],
    "creatorname": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["Name"].astype(str).tolist())],
    "createdon": ['notNull','mandatory','followsCondition:createdon<=updatedon'],
    "updatedon": ['notNull','mandatory',''],
    "notetype": ['notNull','mandatory','dropdown:'+",".join(dfs["note_type_mapping"]["id"].astype(str).tolist())],
    "createdby": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "updatedby": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "ownerid": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "accountid": ['notNull','mandatory','dropdown:'+",".join(dfs["Account_plan"]["accountid"].astype(str).tolist())],
})

# tables = {
#     "tblcandidate": candidate_data, 
#     "candidate_custom_fields_t": candidate_custom_field_data,
#     "tblcompany": company_data
# }

extrafieldchecks = pd.DataFrame({
    "dropdown" : ['dropdown',''],
    "multiselect" : ['multiselect', ''],
    "text" : ['length:2000', ''],
    "email" : ['followsPattern:.*@.*[.].*:%_@%_.%', ''],
    "phonenumber" : ['followsPattern:[0-9]+:%[0-9]%', ''],
    "number" : ['datatype:float', ''],
    "date" : ['datatype:int', ''],
    "longtext" : ['length:5000', ''],
    "checkbox" : ['dropdown:0,1', ''],
})

tables = {
    "candidate": candidate_data, 
    "candidate_custom_data": candidate_custom_field_data,
    "company": company_data,
    "company_custom_data": company_custom_field_data,
    "contact": contact_data,
    "contact_custom_data": contact_custom_field_data,
    "job": job_data,
    "job_custom_data": job_custom_field_data,
    "job_assignment": job_assignment_data,
    "deal": deal_data,
    "deal_custom_data": deal_custom_field_data,
    "note": note_data,
    # "note_2": note_data,
    # "note_candidate": note_data,
    # "note_company": note_data,
    # "note_contact": note_data,
    # "note_job": note_data,
    # "note_deal": note_data,
}

#  ⚠️ Insert statements should only include columns that are present in the database.
tblextrafields = """

-- ambacia - loxo

INSERT INTO tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
(1,23625,5,'Email Type','dropdown','Work,Personal'),
(2,23625,5,'Work Emails','text',null),
(3,23625,5,'Personal Emails','text',null),
(4,23625,5,'Phone Type','dropdown','Work,Personal'),
(5,23625,5,'Work Phones','phonenumber',null),
(6,23625,5,'Personal Phones','phonenumber',null),
(7,23625,5,'Rating','dropdown','✅ Recommended ✅,❌ Not Recommended ❌,❓ Recommended With Restrain ❓,🔥 Highly Recommended 🔥,🚩 Black List 🚩'),
(8,23625,5,'Lists','multiselect','.NET B2B,Agents 1,Android b2b,B2B Aliens,B2B Product,Corporate,DevOps B2B,Ecommerce,Frontend B2B,Germany Targets,iOS B2B,Netherlands Targets,Newsletter,PHP B2B,QA B2B'),
(9,23625,5,'Record Type','multiselect','Candidate,Contact'),
(10,23625,5,'Comp','number',null)
;

-- COMPANY
INSERT INTO tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
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
(13,23625,3,'All Addresses','longtext',null)
;

-- CONTACT
INSERT INTO tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
(1,23625,2,'Email Type','dropdown','Work,Personal'),
(2,23625,2,'Secondary Emails','text',null),
(3,23625,2,'Lists','multiselect','Agents 1,Apollo Croatia,CCI France,Corporate,Germany Targets,Incubators,Netherlands Targets,Start ups'),
(4,23625,2,'Rating','dropdown','✅ Recommended ✅,🔥 Highly Recommended 🔥'),
(5,23625,2,'Phone Type','dropdown','Work,Personal'),
(6,23625,2,'Work Phones','phonenumber',null),
(7,23625,2,'Personal Phones','phonenumber',null),
(8,23625,2,'Record Type','multiselect','Candidate,Contact')
;

 -- JOB
INSERT INTO tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
(1,23625,4,'Seniority Levels','multiselect','Entry,Mid Level,Senior,Director'),
(2,23625,4,'Opened date','date',null),
(3,23625,4,'Selection Process','text',null)
;

 -- deals
INSERT INTO tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
(1,23625,11,'Workflow','dropdown','IT Recruitment 2025,LuminaryIT 2024,Recruitment 2023,Recruitment 2024'),
(2,23625,11,'Currency','dropdown','EUR'),
(3,23625,11,'Job type','dropdown','Full Time'),
(4,23625,11,'Salary Currency','dropdown','EUR')
;


 """
