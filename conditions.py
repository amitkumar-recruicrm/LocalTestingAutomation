import pandas as pd

# Replace with your actual file path for xlsx file of Initial data download from retool.
file_path = "/Users/amit/Documents/Work/Data Migrations/completed/Brown and Wills. (Bullhorn)/Initial_data 60297 (Brown and Wills Recruitment Lt) 2.xlsx" 

# Load all sheets as a dictionary of DataFrames
dfs = pd.read_excel(file_path, sheet_name=None)

# Check available sheet names
# print(dfs.keys())
# ['Account_plan', 'user_details', 'hotlist_mapping', 'note_type_mapping', 'deal_stage_mapping', 'job_status_mapping', 'extra_field_mapping', 'calllog_type_mapping', 'meeting_type_mapping', 'contact_stage_mapping', 'custom_industry_mapping', 'candidate_status_mapping']

candidate_data = pd.DataFrame({
    "migration_reserved1" : ['notNull','mandatory','unique'],
    "firstname" : ['notNull','mandatory','length:60'],
    "lastname" : ['','','length:60'],
    "locality" : ['','','length:50'],
    "city" : ['','','length:50'],
    "state" : ['','','length:50'],
    "country" : ['','','length:50'],
    "slug" :      ['unique', 'notNull',''],
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
    "slug" : ['unique', 'notNull',''],
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
    "slug" :      ['unique', 'notNull',''],
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
    "slug" :      ['unique', 'notNull',''],
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
    "note_candidate": note_data,
    "note_company": note_data,
    "note_contact": note_data,
    "note_job": note_data,
    "note_deal": note_data,
}

#  ⚠️ Insert statements should only include columns that are present in the database.
tblextrafields = """

-- brown and wills

insert into tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
(2, 1343554,5,'Notice','dropdown','3 Months,4 Weeks,1 Week,IMMEDIATE,6 Months,1 Month,2 Weeks,2 Months,3 Weeks'),
(1, 1343554,5,'Industry','multiselect','Building,Civils,Residential,Social Housing,M & E,Modular,Consultancy,Sub-Contractor'),
(3, 1343554,5,'Tags','multiselect','Education,Health,Commerial,Industrial,Retail,Leisure,Heritage,MOD,MOJ,Major Projects,Highrise,Frameworks,Refurbs,Smallworks,Fit-Out,H & S,Maintenance,Joinery,Brickwork,Architecture,Nuclear,Infrastructure,BIM,Conquest,ASTSA,Building Regs,3DModelling,Tier 1,Medium Contractor,Astra,Bridges,Building,Car Showroom,Carehome,Civils,Cleansed,CSCS,Data centres,Datacentres,Electrical,Energy,Excavation,Groundworks,Health and Safety,Heavy Civils,High Rise,Hotel,HVAC,Listed Building,Luxury Housing,Major Project,Marine,Mechanical,MEP,Modular,Office,Pipelines,Power,Public Health,Rail,Refurb,Regional,Regional Contractor,Remove from database,Renewables,Residential,Sheds,Small Contractor,Small Works,SMSTS,Social Houseing,Social Housing,Social Housing (New Build),Social Housing (Refurb),Spec Housing,Trades,Universities,University,Xmas 2023 KIT'),
(5, 1343554,5,'Other Source','dropdown','LinkedIN,CV Library Search,Database Search,Referral,Previous Placement,Website Response,Client Contact,Already KnownData,ContactOut,CV Library,CV Library Ad,CV Library Watchdog,Glennigans,Headhunt,Indeed,Other,Total Jobs,Web Registration'),
(8, 1343554,5,'Other Info','longtext',null),
(9, 1343554,5,'Status','dropdown','To be confirmed,Active,Keep in touch,Immediate,Unknown,Asked not to be contacted'),
(10, 1343554,5,'Day Rate','number',null),
(11, 1343554,5,'Desired Job','longtext',null),
(12,1343554,5,'Phone','text',null), 
(13,1343554,5,'WorkPhone','text',null),
(14,1343554,5,'Name Prefix','text',null),
(15,1343554,5,'Date Last Comment','date',null),
(12,1343554,5,'Phone','text',null), 
(13,1343554,5,'WorkPhone','text',null),
(14,1343554,5,'Name Prefix','text',null),
(15,1343554,5,'Date Last Comment','date',null),
(16,1343554,5,'Other Contact Status','text',null)
;


 -- COMPANY
insert into tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
(3, 1343554,3,'Status','multiselect','PSA Agreement,Regular/Warm Client,New Client/Cold,Archive/Bad Business!'),
(4, 1343554,3,'Industries','multiselect','Building,Residential,Sub-Contractor,Civil Engineering,Consultancy,Architecture'),
(5, 1343554,3,'Fees','number',''),
(6,1343554,3,'Phone Number','phonenumber',null)
;

  -- CONTACT
insert into tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
(3,1343554,2,'Status','multiselect','New Lead/Cold,Follow Up Needed,Regular Contact,VIP Contact,Left Company,Active Employee,Hiring Manager'),
(7,1343554,2,'Mobile','phonenumber',null),
(8,1343554,2,'Name Prefix','text',null),
(9,1343554,2,'Date Last Comment','date',null),
(10,1343554,2,'Industries','multiselect','Administration,Building,Civil Engineering,Housing,M & E,Others,Private Practice')
;

-- JOB
insert into tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
(1, 1343554,4,'Employment Type','multiselect','Permanent,Freelance,Fixed Term'),
(2, 1343554,4,'Start Date','date',null),
(3, 1343554,4,'Duration','text',null),
(5,1343554,4,'Date Client Interview','date',null),
(6,1343554,4,'Date End','date',null),
(7,1343554,4,'Charge Rate','number',null),
(8,1343554,4,'Pay Rate','number',null),
(9,1343554,4,'Industries','multiselect','Administration,Architecture,Bid,Building,Civil Engineering,Commercial,Consultancy,Design,Engineering,Estimating,Housing,M & E,Operations,Others,Planning,Pre-Construction,Private Practice,Residential,Site Management,Sub-Contractor')
;

 """
