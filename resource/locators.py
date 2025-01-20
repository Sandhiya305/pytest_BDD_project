# XPaths for Salesforce Lead Creation and Conversion

#USECASE 1

# Lead Information XPaths
lead_name_xpath = "//div[@title='New']"
lead_first_name_xpath = "//input[@name='firstName']"
lead_last_name_xpath = "//input[@name='lastName']"
lead_company_xpath = "//input[@name='Company']"
lead_save_button_xpath = "//button[text()='Save']"

# Convert Lead to account using create new account
convert_button_xpath = "//button[@name='Convert']"
convert2_button_xpath = "(//div/span/button[@type='button'])[2]"
convert_msg_xpath = "//div[@class='title']"

# Account Xpath from lead page using create existing account
choose_existing_account_xpath = "(//span[@class='slds-form-element__label'])[2]"
account_search_box= "//input[@placeholder='Search for matching accounts']"
choose_existing_account = "(//div[contains(@title, 'Stay_Positive')])[1]"
choose_convert = "(//div/span/button[@type='button'])[2]"

# Account and Contact XPaths
select_account_xpath = "(//a[@title='Positive'])[1]"
new_contact_button_xpath = "(//button[@name='Global.NewContact'])[1]"
salutation_dropdown_xpath = "//a[@role='combobox']"
contact_lastname_xpath = "//input[@placeholder='Last Name']"
contact_save_button_xpath = "(//span[@class='label bBody'])[7]"

# Opportunity XPaths
opportunity_button_xpath = "//button[@name='Global.NewOpportunity']"
opportunity_save_button_xpath = "(//span[@class='label bBody'])[7]"

#USECASE 2

# Account Xpath from lead page
Create_account_xpath = "//one-app-nav-bar-item-root/a/span[text()='Accounts']"
Create_new_account_button = "//div[@title='New']"
create_account_name_xpath = "//input[@name='Name']"
create_account_save_button_xpath = "//button[@name='SaveEdit']"

#create new contact
Create_new_contact_xpath = "//a[@aria-describedby='popover-34']"
Create_new_contact_button = "//a[@title='New']"
Contact_firstname_xpath ="//input[@name='firstName']"
Create_new_contact_last_name_xpath= "//input[@placeholder='Last Name']"
Search_contact_name_xpath = "//input[@placeholder='Search Accounts...']"
dropdown_account_name_xpath = "(//lightning-base-combobox-formatted-text[@title='Meena'])[1]"
create_contact_save_button_xpath = "//button[@name='SaveEdit']"

#Create new opportunity
Create_new_opportunity_button = "//div[@title='New']"
opportunity_name ="//input[@name='Name']"
Search_account_name_xpath = "//input[@placeholder='Search Accounts...']"
dropdown_account_name_xpath1 = "(//lightning-base-combobox-formatted-text[@title='Meena'])[1]"
Closing_date_xpath = "//input[@name='CloseDate']"
scroll_xpath = "//div[@class='actionBody']"
stage_xpath = "//button[@aria-label='Stage']"
select_stage = "//span[@title='Qualify']"
Forecast_category_xpath = "//button[@aria-label='Forecast Category']"
select_Forecast_category = "//span[@title='Omitted']"
create_opportunity_save_button_xpath = "//button[@name='SaveEdit']"

#validate contact opportunity
locate_account = "//a[@data-recordid='001dN00000NGvQ5QAL']"
contact_created = "//article[contains(@aria-label, 'Meena murugavel')]"
scroll = "//html[@lang='en-US']"
opp_created = "//article[contains(@aria-label, 'Circle')]"



