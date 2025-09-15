import pandas as pd
from config import file_path, tblextrafields

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
    "emailid"   : ['followsPattern:.*@.*[.].*:%_@%_.%_','',''],
    "contactnumber" : ['followsPattern:[0-9]+:%[0-9]%','',''],
    "willingtorelocate": ['datatype:int','',''],
    "genderid": ['dropdown:0,1,2,3,4','',''],
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

extrafieldchecks = pd.DataFrame({
    "dropdown" : ['dropdown',''],
    "multiselect" : ['multiselect', ''],
    "text" : ['length:2000', ''],
    "email" : ['followsPattern:.*@.*[.].*:%_@%_.%', ''],
    "phonenumber" : ['followsPattern:[0-9]+:%[0-9]%', ''],
    "number" : ['datatype:float', ''],
    "date" : ['datatype:int', ''],
    "longtext" : ['length:5000', ''],
    "checkbox" : ['dropdown:0,1', 'notNull'],
    "file" : ['', ''],
    "social_profile" : ['','']
    # "social_profile" : ['followsPattern:^(?:https?:\/\/|www\.)[^.]+\..{2,}$:^(?:https?:\/\/|www\.)[^.]+\..{2,}$', ''],
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
    "note_candidate": note_data,
    "note_company": note_data,
    "note_contact": note_data,
    "note_job": note_data,
    "note_deal": note_data,
}

