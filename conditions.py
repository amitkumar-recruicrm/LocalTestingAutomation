import pandas as pd

candidate_data = pd.DataFrame({
    "firstname" : ['notNull','mandatory'],
    "slug" :      ['unique', 'notNull'],
    "emailid"   : ['followsPattern:.*@.*[.].*',''],
    "contactnumber" : ['followsPattern:[0-9]+',''],
    "willingtorelocate": ['datatype:int','mandatory'],
    "genderid": ['dropdown:0,1,2',''],
    "currentsalary": ['datatype:float',''],
    "salaryexpectation": ['datatype:float',''],
    "noticeperiod": ['datatype:int','']
})

candidate_custom_field_data = pd.DataFrame({
    "import_slug" : ['notNull','']
})

company_data = pd.DataFrame({
    "createdon" : ['notNull',''],
    "slug" : ['unique', 'notNull']
})

# tables = {
#     "tblcandidate": candidate_data, 
#     "candidate_custom_fields_t": candidate_custom_field_data,
#     "tblcompany": company_data
# }

extrafieldchecks = pd.DataFrame({
    "dropdown" : ['dropdown:A,B,C',''],
    "multiselect" : ['dropdown', ''],
    "text" : ['', ''],
    "email" : ['followsPattern:.*@.*[.].*', ''],
    "phonenumber" : ['', ''],
    "number" : ['', '']
})

tables = {
    "candidate_data": candidate_data, 
    "candidate_custom_field_data": candidate_custom_field_data,
    "company_data": company_data
}

tblextrafields = """

    -- candidate

    insert into tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
    (37,42747,5,'Middle Name','text',null),
    (38,42747,5,'Secondary Job Category','dropdown','21 Gradate,22 Graduate,Admin,Business Improvement,Buyer,Category Leader,Category Manager,Continuous Improvement Specialist,Data Analyst,Demand Planner,Digital Marketing Executive,E-Commerce Executive,Expeditor,Export Manager,Freelance Procurement Consultant,Freight Forwarder,Graduate/Trainee Buyer,Head of Distribution,Head of Procurement,Head of Purchasing,Head of Supply Chain,HR,Import Manager,Inventory Manager,Inventory Planner,Logistics,Logistics Administrator,Maintenance Officer,Master Scheduler,Materials Manager,Materials Planner,Materials Team Leader,Merchandiser,Non Qualified,Operations Manager,Other,Part Qualified,Planning Manager,Procurement,Procurement Administrator,Procurement Director,Procurement Manager,Procurement Officer,Procurement Team Leader,Production Planner,Project Management,Purchasing Administrator,Purchasing Manager,Purchasing Team Leader,Qualified,S&OP Planning Manager,Sales,Senior Buyer,Senior Procurement Officer,Sourcing Manager,Supplier Manager,Supply Chain,Supply Chain Administrator,Supply Chain Analyst,Supply Chain Director,Supply Chain Manager,Third Party Vendor Manager,Trading Assistant,Trading Manager,Transport Manager,Transport Planner,Warehouse Manager,Warehouse Supervisor'),
    (39,42747,5,'Disability','dropdown','Yes,No'),
    (40,42747,5,'Disability Description','text',null),
    (41,42747,5,'Ethnicity','dropdown','White UK,White Other,Mixed,Black- African,Asian – Indian,Asian – Chinese,Asian - Pakastani,Asian - Other,Other'),
    (42,42747,5,'Belief','dropdown','Roman Catholic,Protestant,hindu,orthodox,Islam,Muslim,Christian'),
    (43,42747,5,'Resident Location','dropdown','Northern Ireland,Europe (but not the UK),England,Overseas (but not Europe),Scotland')
    ;
    
    -- Company

    insert into tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
    (6,42747,3,'Ownership Type','dropdown','AIM,Corporative,Not For Profit,Not Operating,PLC,Private,Public'),
    (7,42747,3,'Main Contact Email','email',null),
    (8,42747,3,'Main Phone','phonenumber',null),
    (9,42747,3,'Credit Status','dropdown','Credit Approved,Bad Credit'),
    (10,42747,3,'Payment Terms','dropdown','NET30,NET7,30 Days,NET14,EOM+15'),
    (11,42747,3,'Invoice Cycle','dropdown','Weekly,Monthly,Other'),
    (12,42747,3,'Registration','text',null),
    (13,42747,3,'Source','dropdown','Called in,Lead management,PSL,Hot boss,Candidate referral,BD,Second Tier - MS recruitment'),
    (14,42747,3,'Permanent Markup Percent','number',null),
    (15,42747,3,'Contract Markup Percent','number',null)
    ;
 """
