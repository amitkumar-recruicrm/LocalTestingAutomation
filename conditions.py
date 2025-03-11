import pandas as pd

# Replace with your actual file path
file_path = "/Users/amit/Documents/Work/Data Migrations/in progress/Altura Partners (Loxo)/Initial_data 51057 (Altura Partners Ltd) 3.xlsx" 

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
    "emailid"   : ['followsPattern:.*@.*[.].*','',''],
    "contactnumber" : ['followsPattern:[0-9]+','',''],
    "willingtorelocate": ['datatype:int','',''],
    "genderid": ['dropdown:0,1,2','',''],
    "salarytype": ['dropdown:1,2,3,4,5','',''],
    "currentsalary": ['datatype:float','',''],
    "salaryexpectation": ['datatype:float','',''],
    "noticeperiod": ['datatype:int','',''],
    "lastorganisation": ['length:300','',''],
    "position": ['length:100','',''],
    "address": ['length:500','',''],
    "createdon": ['notNull','mandatory',''],
    "updatedon": ['notNull','mandatory',''],
    "createdby": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "updatedby": ['notNull','mandatory','dropdown:'+",".join(dfs["user_details"]["id"].astype(str).tolist())],
    "accountid": ['notNull','mandatory','dropdown:'+",".join(dfs["Account_plan"]["accountid"].astype(str).tolist())],
})

candidate_custom_field_data = pd.DataFrame({
    "import_slug" : ['notNull',''],
    "candidate_id" : ['notNull','mandatory'],
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
    "multiselect" : ['dropdown:Ab,Bc', ''],
    "text" : ['length:2000', ''],
    "email" : ['followsPattern:.*@.*[.].*', ''],
    "phonenumber" : ['', ''],
    "number" : ['', '']
})

tables = {
    "candidate": candidate_data, 
    "candidate_custom_data": candidate_custom_field_data,
    "company": company_data
}

tblextrafields = """

-- Altura Partners

-- CANDIDATE 
insert into tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
(1,51057,5,'Location','text',null), 
(2,51057,5,'Candidate Source','dropdown','Linkedin inmail,Liknkedin Job Advert,Data Import,Referral,Network,Event'),
(3,51057,5,'Secondary Emails','text',null),
(4,51057,5,'Phone Type','dropdown','Personal,Work,Other'),
(5,51057,5,'Secondary Phones','text',null),
(6,51057,5,'Social URLs','text',null);

 -- COMPANY
insert into tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
(1,51057,3,'Address Type','dropdown','Main'),
(2,51057,3,'Emails','email',null),
(3,51057,3,'Email Type','dropdown','Work'),
(4,51057,3,'Phones','phonenumber',null);


 -- CONTACT
insert into tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
(1,51057,2,'Secondary Emails','email',null),
(2,51057,2,'Email Type','dropdown','Work,Other'),
(3,51057,2,'Lists','multiselect','15sep20x1,18thSep2020,28thSep,9sep20,9sep20x3,9sep20x5,9sep20x6,Agency,AI,Ai Cyber Security BD,AI enrichment | CEO/Founder,AI enrichment | Customer Success,AI enrichment | HR & TA,AI enrichment | Marketing,AI enrichment | Presales,AI enrichment | Product,AI enrichment | Sales,AM - DevSecOps BD,AM America,AM Asia,AM Europe,AM UK,Anti-Ransomware BD,AP Automation enrichment | CEO/Owner,AP Automation enrichment | CS,AP Automation enrichment | HR/TA,AP Automation enrichment | Marketing,AP Automation enrichment | Presales,AP Automation enrichment | Product,AP Automation enrichment | Sales,AP, AR Automation Mailshot BD,API Security Mailshot,Application Defence Platform BD,ASIC - Denmark,ASPM BD,Automated Security Workflow BD,Automated Threat Modelling BD,Badams | Insight | Product,BD,BD calls Observability,BD List 11/22,BD USA,ben Identity,Ben P - Candidates - Cyber MSSP,Ben P - Candidates - Reseller,Ben P - Consultancy,Ben P - Cyber Consultancy,Ben P - Cyber Managers to spec into,ben p - Cyber Marketing,Ben P - Cyber Vendor Channel,Ben P - Data Security,Ben P - Digital Forensics,Ben P - Distributors,Ben P - MSSPs,Ben P - MSSPs 2,Ben P - Reseller Sales Directors,Ben P - Resellers,Ben P - Resellers Midlands,Ben P - Resellers North,Ben P - Resellers South,Ben P - Threat Intel,Ben P - Warm Leads,Ben P - XDR,Ben P 20 target accounts,Ben P 2023,Ben P Anti-Fraud,Ben P December BD List,Ben P IAM,Ben P IoT,Ben P Jan Call List,Ben P MDR,Ben P MPCs,Ben P Threat Intel,Ben P US List,Ben P Verification,Big City Digital Design and Verification,Billing, AR, Payments and Billing solution BD,Bot Management Software,Buy-now-pay-later BD,CAASM BD,california,Call sprint - US,Call Sprint - USA,Call sprint list Lindae EMEA,candidates - CDW,Candidates for 2023,Cash Flow Forecasting BD,Cash Flow Management,Chase Old Relex People,CJ 0 - Targets,CJ 1 - Leads,CJ 2- Callback,CJ 3 - Chasing Engaged,CJ 4 - Live,Claud Fraud List,Claud Identity Manager List,Cloud Security BD,Cool Vendors,Crisis Management BD,CRO USA,CSM BD Outreach,Currency Cloud,CX,Cyber CRO - US (Anthony),Cyber Risk Assessment software,Cyber Training BD,Cybersec Software General BD,Cybersecurity PS Salespeople,Damo | EAM | Customer Success,Damo | EAM | Founder,Damo | EAM | Marketing,Damo | EAM | Product,Damo | EAM | Sales,Damo | EAM | TA/HR,Damo | FSM | Founder,Damo | FSM | Marketing,Damo | FSM | Product,Damo | FSM | Sales,Damo | FSM | TA/HR,Damo | Supply Chain | Customer Success,Damo | Supply Chain | Founder,Damo | Supply Chain | Marketing,Damo | Supply Chain | Pre-Sales,Damo | Supply Chain | Product,Damo | Supply Chain | Sales,Damo | Supply Chain | TA/HR,Damo BD flip targets,Dan - Cyber Enrichment (India) - Customer Success,Dan - Cyber Enrichment (India) - Founder/CEO/Owner,Dan - Cyber Enrichment (India) - HR/People/TA,Dan - Cyber Enrichment (India) - Marketing,Dan - Cyber Enrichment (India) - Pre-Sales,Dan - Cyber Enrichment (India) - Product,Dan - Cyber Enrichment (India) - Sales,Dan BD leads july 23,Dan BD Sep 22,Dan Sequencing - CEO,Dan Sequencing - Customer Success,Dan Sequencing - HR/People,Dan Sequencing - Marketing,Dan Sequencing - Pre-Sales,Dan Sequencing - Product,Dan Sequencing - Sales,Dan Sequencing - TA,DAS Enrichment - CEO/Founder,DAS Enrichment - Marketing,DAS Enrichment - Presales,DAS Enrichment - Product,DAS Enrichment - Sales,DAS Enrichment - Tech,DAST BD,data analytics,Data security and compliance BD,DBR,DF AE outreach,DF client prospects,DF Contacts,DF NOV 23 outreach,DF VP Sales Engineering,Digital Identity Wallet,Digital Transformation,Doug | DevOps Series A | Customer Success,Doug | DevOps Series A | Founder,Doug | DevOps Series A | Marketing,Doug | DevOps Series A | Pre-Sales,Doug | DevOps Series A | Product,Doug | DevOps Series A | Sales,Doug | DevOps Series A | TA/HR,Doug | DevOps Series B | Customer Success,Doug | DevOps Series B | Founder,Doug | DevOps Series B | Marketing,Doug | DevOps Series B | Product,Doug | DevOps Series B | Sales,Doug | DevOps Series B | TA/HR,Doug Crunchbase - CEO,Doug Crunchbase - Sales,Drones- C-Level,Drones- VP & SD,Drupal Hiring Managers - London,Ecommerce Subscription Platform BD,EDR BD,Email security BD,EMEA CALL LIST Lindae,Emma BD,Encrypted Platform BD,ESG - BD,European start ups CYBER,Expense Management BD,Exposure Management BD,Financial Fraud Detection and AML BD,Financial Risk Solutions BD,Fleur - 1st BD Reach Out,Fleur - BD Ad chasing,Fleur - Target Client List,FNE 0 - Targets,FNE 1 - Leads,FNE 4 - Live,FP&A BD,Fran BD list AM,FSM America,FSM australia,FSM Europe,FSM UK,Go-To-Market Security BD,Hexagon | Challenge Cohort | Customer Success,Hexagon | Challenge Cohort | Founder/CEO,Hexagon | Challenge Cohort | Marketing,Hexagon | Challenge Cohort | Product,Hexagon | Challenge Cohort | Sales,Hexagon | Challenge Cohort | TA/HR,Hexagon Leaders,Human Risk Management BD,Hybris,IAM Mailshot,Identity Verification BD,international RFIC Managers,IOT Security,James - IoT/Saas BD Outreach List,Jim | Additive Manufacturing | Customer Success,Jim | Additive Manufacturing | Founder,Jim | Additive Manufacturing | Marketing,Jim | Additive Manufacturing | Product,Jim | Additive Manufacturing | Sales,Jim | Additive Manufacturing | TA/HR,Jim | Digital Twin SaaS | CEO - MD - President,Jim | Digital Twin SaaS | Customer Success,Jim | Digital Twin SaaS | Marketing,Jim | Digital Twin SaaS | Product,Jim | Digital Twin SaaS | Sales,Jim | Geospatial | Customer Success,Jim | Geospatial | Founder,Jim | Geospatial | Marketing,Jim | Geospatial | Pre-Sales,Jim | Geospatial | Product,Jim | Geospatial | Sales,Jim | Geospatial | TA/HR,Jim | Industrial Engineering | Customer Success,Jim | Industrial Engineering | Founder,Jim | Industrial Engineering | Marketing,Jim | Industrial Engineering | Product,Jim | Industrial Engineering | Sales,Jim | Industrial Engineering | TA/HR,Jim | Manufacturing SaaS | Founder,Jim | Manufacturing SaaS | Marketing,Jim | Manufacturing SaaS | Pre-Sales,Jim | Manufacturing SaaS | Product,Jim | Manufacturing SaaS | Sales,Jim | Manufacturing SaaS | TA/HR,Jim | Robotics | Customer Success,Jim | Robotics | Founder,Jim | Robotics | Marketing,Jim | Robotics | Pre-Sales,Jim | Robotics | Product,Jim | Robotics | Sales,Jim | Robotics | TA/HR,Jim Sequencing - Customer Success,Jim Sequencing - Marketing,Jim Sequencing - Product,Jim Sequencing - Sales,Jim Sequencing - TA/HR,Jim Sequencing - Technical,Jimbo - BD Flips,JN - IOT - 0 Targets,JN - IOT - 1 Leads,JN - IOT - 1.2 Leads Europe,JN - IOT - 2 Callback,JN - IOT - 3 Engaged,JN - IOT - 4 Active Clients,Lacework,LF BD List,LF NAC, IOT, ICS, OT BD-LIST,Lindae BD IoT Security,Lindae Cato Networks,Lindae Claroty,Lindae Cohesity,Lindae Crowdstrike list,Lindae EMEA Campaign General,Lindae Expel,Lindae Forcepoint,Lindae Illumio,Lindae Immersive Labs,Lindae List - New Funding - Team Build,Lindae UK BD list,Lindae Veracode,Live Roles,Magento Hiring Managers - London,mailshot list JB,Managed Services,March 2023 Leads,Martech - BD - US,martech uk BD,Max Waterhouse Spec List,MC - JAVASCRIPT MANAGERS,MC & JR combined PHP - London,MDR BD,Microsoft Managed Services,MPC target stakeholder,MPC- James Flygare / call list,MWC Barcelona 2022,NAC Vendor List,Network Digital Twin and Cybersec Platform BD,Networking Resellers,New 2020 - Javascript managers,Not Drones- Manager, VP, Director, C-Level,NYC/philly semicon,Offensive Security BD,Old terms clients,Open roles Dani US,OpenText,Payments - Strong Interviewed Candidates,Payments - Target CEO,Payments - Target Companies Contacts,Payments - Target Engineering,Payments - Target HR,Payments - Target Managing Directors,Payments - Target Marketing,Payments - Target Product,Payments - Target Sales,Payments - Target Strategy,Payments - Top 100 Contacts,Payments and Banking Infrastructure BD,Payments Enrichment List Data,Payments Infrastructure and compliance BD,Payroll, Commission, Benefits BD,PHP Hiring Managers - London,PHP Managers,Physical Security,Procure-To-Pay BD,Python Hiring Managers - London,RB 0 - Targets,RB 1 - Leads,React - Frontend,Reading tech comapnies,recruitment,relex,RSA Enrichment - CEO/Founder,RSA Enrichment - Customer Success,RSA Enrichment - Marketing,RSA Enrichment - Presales,RSA Enrichment - Product,RSA Enrichment - Sales,RSA Enrichment - Tech,saas/low-code Security,salart,Secrets Management SaaS BD,Secure Access BD,Security Automation BD,Semicon All companies,Semicon companies - Europe,semicon UK,Semiconductor Digital/ASIC,semiconductor/electronics BRISTOL,SH 0 - Targets,SH 1 - Leads,SH 2 - Callback,SH 3 - Chasing Engaged,Spend Management,SSPM BD,Supply Chain enrichment | CEO/Founder,Supply Chain enrichment | CS,Supply Chain enrichment | HR/TA,Supply Chain enrichment | Marketing,Supply Chain enrichment | Presales,Supply Chain enrichment | Product,Supply Chain enrichment | Sales,Supply Chain Security BD,Tax Compliance,Telco,Third Party Risk Management BD,Threat Detection and Response BD,Tom BD List,Tom USA  Campaign 1,Treasury Management BD,TValley .Net Hiring Manager,uk,uk semicon (NOT bristol),US List Lindae,USA Salary Report 2023,Versa AE,VP of Sales - Europe Call list,Vulnerability Management BD,Web Application Security and Testing BD,Web3/Blockchain Cyber Security BD,working capital BD,XDR BD'),
(4,51057,2,'Location','text',null),
(5,51057,2,'Phone Type','dropdown','Work,Personal,Other'),
(6,51057,2,'Secondary Phones','phonenumber',null)
;

 -- JOB
insert into tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
(1,51057,4,'Bonus','number',null),
(2,51057,4,'Comp','text',null),
(3,51057,4,'Fee','number',null),
(4,51057,4,'Fee Type','dropdown','Percentage,Flat'),
(5,51057,4,'Seniority Levels','multiselect','C Suite,Director,Entry,Mid Level,Senior,VP')
;

 """
