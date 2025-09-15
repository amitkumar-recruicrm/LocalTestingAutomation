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

# SQL Server database connection configuration
postgres_config = {
    'server': 'localhost',
    'database': 'CLSPartner',
    'user': 'root',
    'password': 'Amit@1234'
}

# platform = 'sqlserver'
platform = 'postgres'
# platform = 'MySQL'

schema = 'cleaned'

# Replace with your actual file path for xlsx file of Initial data download from retool.
file_path = "/Users/amit/Documents/Work/Data Migrations/completed/KMR Rec (JobAdder)/Initial_data 70963 (KMR Recruitment ) 4.xlsx" 
# file_path = "/Users/amit/Documents/Work/Data Migrations/completed/Ambacia (LOXO)/Initial_data 23625 (Ambacia) 2.xlsx"
# file_path = "/Users/amit/Documents/Work/Data Migrations/completed/household staffing (CATS)/Initial_data 62825 (householdstaffing) 5.xlsx"
# file_path = "/Users/amit/Documents/Work/Data Migrations/completed/Carl lens Search partner (careix)/Initial_data 62124 (Carl Lens Search Partners BV) (1).xlsx"

# Add all entries in a single insert statement - This is used for custom fields type and values #
tblextrafields = """
INSERT INTO tblextrafields(columnid,accountid,entitytypeid,extrafieldname,extrafieldtype,defaultvalue) values
(2,1343554,5,'Request Action','dropdown','Request Agreement,Request Disclosure,Reference Invite'),
(3,1343554,5,'Referred By','text',null),
(5,1343554,5,'Trial Date','date',null),
(6,1343554,5,'Live In/Out','multiselect','Live In,Live Out,Live In/Out'),
(4,1343554,5,'Talent Pool','checkbox',null),
(7,1343554,5,'Full/Part Time','multiselect','Full Time,Part Time,Temporary,ROTA,Weekend'),
(8,1343554,5,'Payment Method','multiselect','W-2,1099,Other'),
(10,1343554,5,'References','file',null),
(11,1343554,5,'Driver''s License','file',null),
(12,1343554,5,'Candidate Agreement','file',null),
(13,1343554,5,'Disclosure Agreement','file',null),
(14,1343554,5,'Fast-Check','file',null),
(15,1343554,5,'Fast-Check Date','date',null),
(16,1343554,5,'Full-Check','file',null),
(17,1343554,5,'Full-Check Date','date',null),
(18,1343554,5,'Positions Held','multiselect','Accountant,Administrative Assistant,After School Care,Au Pair,Babysitter,Bookkeeper,Building Maintenance,Butler,Caretaker/Groundskeeper,CEO,CFO,CNA/HHA/PCA,Chef,Chief of Staff,Chief Steward/Stewardess,Companion,Construction Project Manager,Cook,COO,Couple,Director of Operations,Driver,Estate Manager,Executive Assistant,Executive Housekeeper,Family Assistant,Family Office Accountant,Family Office Assistant,Family Office Corporate Chef,Family Office General Counsel,Family Office HR Specialist,Family Office Lifestyle Manager,Family Office Philanthropy Manager,Family Office PR Specialist,Family Office Property Manager,Gardener,Governess,Graphic Designer,Groundskeeper,Head of Office CEO,Head of Office CFO,Head of Office COO,Hotel Housekeeper,Household Manager,Housekeeper,Housekeeper/After School Care,Housekeeper/Cook,Housekeeper/Nanny,Houseman,Lady''s Maid,Landscape Architect,Laundress,Major Domo,Nanny,Nanny Teacher/Tutor,Nanny/Family Assistant,Nanny/Housekeeper,Newborn Care Specialist,Night Nanny,No Relevant Experience,No Resume,Nurses Aide,Office,Personal Assistant,Personal Trainer,Pet Care/Nanny,Pilot,Police Officer,Preschool Teacher,Private Educator,Project Manager,Property Manager,Ranch Manager,Recruiter,Rota Nanny,Security,Special Needs Nanny,Specialty Sports Nanny,Specialty Tutor/Teacher,Stable Manager,Summer Household Staff,Summer Nanny,Teacher,Teacher - Preschool,Travel Nanny,Weekend Nanny'),
(19,1343554,5,'Desired Positions','multiselect','Accountant,Administrative Assistant,After School Care,Au Pair,Babysitter,Bookkeeper,Building Maintenance,Butler,Caretaker/Groundskeeper,CEO,CFO,CNA/HHA/PCA,Chef,Chief of Staff,Chief Steward/Stewardess,Companion,Construction Project Manager,Cook,COO,Couple,Director of Operations,Driver,Estate Manager,Executive Assistant,Executive Housekeeper,Family Assistant,Family Office Accountant,Family Office Assistant,Family Office Corporate Chef,Family Office General Counsel,Family Office HR Specialist,Family Office Lifestyle Manager,Family Office Philanthropy Manager,Family Office PR Specialist,Family Office Property Manager,Gardener,Governess,Graphic Designer,Groundskeeper,Head of Office CEO,Head of Office CFO,Head of Office COO,Hotel Housekeeper,Household Manager,Housekeeper,Housekeeper/After School Care,Housekeeper/Cook,Housekeeper/Nanny,Houseman,Lady''s Maid,Landscape Architect,Laundress,Major Domo,Nanny,Nanny Teacher/Tutor,Nanny/Family Assistant,Nanny/Housekeeper,Newborn Care Specialist,Night Nanny,No Relevant Experience,No Resume,Nurses Aide,Office,Personal Assistant,Personal Trainer,Pet Care/Nanny,Pilot,Police Officer,Preschool Teacher,Private Educator,Project Manager,Property Manager,Ranch Manager,Recruiter,Rota Nanny,Security,Special Needs Nanny,Specialty Sports Nanny,Specialty Tutor/Teacher,Stable Manager,Summer Household Staff,Summer Nanny,Teacher,Teacher - Preschool,Travel Nanny,Weekend Nanny'),
(20,1343554,5,'Days Available','multiselect','Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday'),
(21,1343554,5,'Owns Car','checkbox',null),
(22,1343554,5,'Legal to Work','checkbox',null),
(23,1343554,5,'Legal Status','multiselect','US Citizen,Green Card Holder,Work Permit,Resident Alien,Applied for Green Card,Applied for Citizenship,Tax ID,J1 VISA,Has a Social Security'),
(25,1343554,5,'Owns Car LEGACY','checkbox',null),
(1,1343554,5,'Verified References','dropdown','Yes,1 of 2,No,Not Until Considered by Client,Bad Reference,Yes: Review Notes - Depends on Role,Suspected Fake Reference,Red Flag'),
(24,1343554,5,'Driver''s License LEGACY','dropdown','Yes,No,Permit'),
(26,1343554,5,'Birth Place LEGACY','text',null),
(27,1343554,5,'Fast-Check LEGACY','checkbox',null),
(28,1343554,5,'Candidate Agreement LEGACY','checkbox',null),
(9,1343554,5,'DOB LEGACY','text',null),
(29,1343554,5,'Full-Check LEGACY','text',null),
(30,1343554,5,'Driver''s License Attached LEGACY','checkbox',null),
(31,1343554,5,'Legal to Work LEGACY','checkbox',null),
(32,1343554,5,'Private Home Experience LEGACY','checkbox',null),
(33,1343554,5,'Total Private Home Experience LEGACY','multiselect','0-3,3-5,5-8,8-10,10+'),
(34,62124,5,'References Attached','dropdown','Yes,No'),
(35,62124,5,'Disclosure Attached','dropdown','Yes,No'),
(1,1343554,3,'Email (App)','text',null),
(2,1343554,3,'Phone (App)','text',null),
(3,1343554,3,'Want to Hire','text',null),
(4,1343554,3,'Hire Type','text',null),
(5,1343554,3,'Hire Time','text',null),
(6,1343554,3,'Days to Close','text',null),
(7,1343554,3,'Placement Fee Refunded','text',null),
(8,1343554,3,'Refunded Amount','text',null),
(9,1343554,3,'Previous Hire Name','text',null),
(10,1343554,3,'Previous Hire Start Date','text',null),
(11,1343554,3,'Previous Hire End Date','text',null),
(12,1343554,3,'Paid Date','text',null),
(13,1343554,3,'gclid','text',null),
(14,1343554,3,'Percent','text',null),
(15,1343554,3,'Fee','dropdown','Default,Fee Paid,Fee Waived,Refunded,Flat Fee'),
(16,1343554,3,'Request PIA (Send Contract)','checkbox',null),
(17,1343554,3,'PIA Date Signed','date',null),
(18,1343554,3,'TEMP Percent','text',null),
(19,1343554,3,'TEMP PIA Date Signed','date',null),
(20,1343554,3,'Request TEMP PIA (Send Contract)','checkbox',null),
(21,1343554,3,'Request Trail Agreement (Send Contract)','checkbox',null),
(22,1343554,3,'Candidate Name','text',null),
(23,1343554,3,'Candidate Phone','text',null),
(24,1343554,3,'Candidate Email','text',null),
(25,1343554,3,'Trial Dates','text',null),
(26,1343554,3,'Trial Working Hours','text',null),
(27,1343554,3,'Trial Location','text',null),
(28,1343554,3,'Trial Responsibilities','longtext',null),
(29,1343554,3,'Trial Rate','text',null),
(30,1343554,3,'Request Start Date (Send Contract)','checkbox',null),
(31,1343554,3,'Request TEMP Start Date (Send Contract)','checkbox',null),
(32,1343554,3,'Start Date Candidate','text',null),
(33,1343554,3,'Start Date Compensation','text',null),
(34,1343554,3,'Start Date','date',null),
(35,1343554,3,'End Date','date',null),
(36,1343554,3,'Start Date Placement Fee','text',null),
(37,1343554,3,'Days Guaranteed','text',null),
(38,1343554,3,'Days Used','text',null),
(39,1343554,3,'Days Owed','text',null),
(40,1343554,3,'Recent Employee Name','text',null),
(41,1343554,3,'Recent Employee Start','text',null),
(42,1343554,3,'Recent Employee End','text',null),
(43,1343554,3,'Recent Employee 2 Name','text',null),
(44,1343554,3,'Recent Employee 2 Start','text',null),
(45,1343554,3,'Recent Employee 2 End','text',null),
(46,1343554,3,'Recent Employee 3 Name','text',null),
(47,1343554,3,'Recent Employee 3 Start','text',null),
(48,1343554,3,'Recent Employee 3 End','text',null),
(49,1343554,3,'Request Employee Replacement (Send Contact)','checkbox',null),
(50,1343554,3,'Request Replacement Start Date (Send Contract)','checkbox',null),
(51,1343554,3,'Original Hire','text',null),
(52,1343554,3,'Original Hire Payment','text',null),
(53,1343554,3,'Original Hire Start Date','text',null),
(54,1343554,3,'Original Hire End Date','text',null),
(55,1343554,3,'Replacement Date Expiration','text',null),
(56,1343554,3,'Replacement Hire Name','text',null),
(57,1343554,3,'Replacement Hire Start Date','text',null),
(58,1343554,3,'Post JSON','longtext',null),
(1,1343554,4,'Placement Needed','text',null),
(2,1343554,4,'Start Date','date',null),
(3,1343554,4,'Live-In Salary','text',null),
(4,1343554,4,'Live-Out Salary','text',null),
(5,1343554,4,'Work Days','text',null),
(6,1343554,4,'Live-Out Start','text',null),
(7,1343554,4,'Live-Out End','text',null),
(8,1343554,4,'Housekeeping','text',null),
(9,1343554,4,'Cooking','text',null),
(10,1343554,4,'Laundry','text',null),
(11,1343554,4,'Driving','text',null),
(12,1343554,4,'Full/Part Time','text',null),
(13,1343554,4,'Live In/Out','text',null),
(14,1343554,4,'Errands','text',null),
(15,1343554,4,'Ironing','text',null),
(16,1343554,4,'Travel','text',null),
(17,1343554,4,'Salary','text',null),
(18,1343554,4,'Health Benefits','text',null),
(19,1343554,4,'Language','text',null),
(20,1343554,4,'Child Details','text',null),
(21,1343554,4,'Current Number of Employees','text',null),
(22,1343554,4,'Position Type','dropdown','Full Time/Live In,Full Time/Live Out,Part Time/Live In,Part Time/Live Out,Full Time/Live In or Live Out,Part Time/Live In or Live Out,Weekend,Temporary/Live In,Temporary/Live Out,Temporary/Live In or Live Out,ROTA/Live In,ROTA/Live Out,ROTA/Live In or Live Out'),
(23,1343554,4,'Position Category','dropdown','After School Care,Babysitter,Butler,Chef,Chief of Staff,Companion,Cook,Couple,Driver,Estate Manager,Executive Assistant,Executive Housekeeper,Family Assistant,Gardner,Governess,Groundskeeper,Household Manager,Housekeeper,Housekeeper/After School Care,Lady''s Maid,Laundress,Nanny,Nanny Teacher/Tutor,Nanny/Housekeeper,Newborn Care Specialist,Night Nanny,Nurses Aide,Personal Assistant,Pet Care/Nanny,Pilot,Private Educator,Property Manager,ROTA Nanny,Security,Speciality Language Tutor,Speciality Sport Nanny,Stable Manager,Summer Household Staff,Summer Nanny,Yacht Crew,Project Manager,Accountant,Housekeeper/Cook,Head of Office CEO,Head of Office COO,Head of Office CFO,Family Office Assistant,Family Office General Counsel,Family Office Philanthropy Manager,Family Office Property Manager,Family Office HR Specialist,Family Office Lifestyle Manager,Family Office Accountant,Family Office PR Specialist,Family Office Corporate Chef,Nanny/Family Assistant'),
(24,1343554,4,'Requirements','longtext',null),
(25,1343554,4,'What works best for your family?','longtext',null),
(26,62124,2,'Salary LEGACY','text',null)
;

"""