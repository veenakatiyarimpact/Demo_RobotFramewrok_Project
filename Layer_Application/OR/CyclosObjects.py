#############################     Naming Conventions   #################################################################
#
#                     Text = Txt
#                     Button= Btn
#                     Link= Lnk
#                     Label= Lbl
#                     Combo= Cmb
#                     Radio=Sel
#                     Checkbox=Chk     
#					  Tab=Tab on page                        
#
#############################     Naming Conventions   #################################################################

##############################                    Cyclos Login Page                    ##############################                             

Obj_Txt_cyclosUsername="xpath=//*[@id='cyclosUsername']"
Obj_Txt_cyclosPassword="xpath=//*[@id='cyclosPassword']"
Obj_Btn_LoginSubmit = "xpath = //*[@id='cyclosLogin']"

Obj_Lnk_Logout = "xpath=//li[@id='menu15']/span[contains(@class, 'menuText')]"

##############################                    Cyclos Create Member                    ##############################  
Obj_Lnk_UsersAndGroups = "xpath=//*[@id='menu5']/span[2]"
Obj_Lnk_ManageMembers = "xpath=//*[@id='submenu5.0']" 
Obj_List_CreateMember = "xpath=//*[@id='newMemberGroup']" 
Obj_Txt_PermissionGroup = "xpath =//*[@id='tdContents']"
Obj_Txt_FullName = "xpath=//tr[3]/td[2]/input[contains(@class, 'large InputBoxEnabled required')]"#"xpath=//*[@name='membar(name)']"
OBJ_Txt_LoginName = "xpath=//tr[2]/td[2]/input[contains(@class, 'large InputBoxEnabled required')]"#"xpath =//*[@name='member(name).username']" 
OBJ_Txt_Email = "xpath=//tr[4]/td[2]/input[contains(@class, 'large InputBoxEnabled required')]"#"xpath =//*[@name='member(email)']"
OBJ_Txt_Birthday = "xpath=//*[@fieldname='birthday']"
OBJ_Sel_Gender = "_radio_2"
OBJ_Txt_Address = "xpath =//*[@fieldname='address']"
OBJ_Txt_PostalCode = "xpath =//*[@fieldname='postalCode']"
OBJ_Txt_City = "xpath =.//*[@fieldname='city']"
OBJ_Txt_MobilePhone = "xpath =//*[@fieldname='mobilePhone']"
OBJ_Btn_OpenProfileSubmit = "xpath =.//*[@id='saveAndOpenProfileButton']"

##############################                      Payment System to Member               ###############################
OBJ_Btn_PaymentSystemToMemberSubmit = "xpath =//input[matches(@linkurl,'payment?to=.*')]"
OBJ_Txt_Amount = "xpath =.//*[@id='amount']"
OBJ_List_TransactionType = "xpath=.//*[@id='type']"
OBJ_Txt_Description = "xpath =.//*[@id='description']"
OBJ_Btn_PaymentSubmit = "xpath =.//*[@id='submitButton']"
OBJ_Btn_ConfirmAndSubmit = "xpath=.//*[@value='Submit']"
OBJ_Btn_BacktoMemberProfile ="xpath =.//*[@id='backToMemberProfileButton']"

##############################                      Member Profile Update               ###############################
OBJ_Btn_ManageNotification = "xpath =.//*[@linkurl='notificationPreferences?memberId=8']"
OBJ_Btn_ManageAdvertisements = "xpath =.//[@linkurl='memberAds?memberId=8']"
##############################                      Manage Advertisements               ###############################
OBJ_Btn_CreateNewAdvertise = "xpath =.//*[@id='newButton']"
OBJ_Txt_Title = "xpath=.//*[@name='ad(title)']"
OBJ_List_Category = "xpath=.//*[@name='ad(category)']"
OBJ_Txt_Price = "xpath=.//*[@name='ad(price)']"
OBj_Chk_Expirable = "xpath=.//*[@id='notExpirableCheck']"
OBJ_Btn_AdvertisementSubmit = "xpath=.//*[@id='saveButton']"

##############################                      Manage Notifications               ###############################
OBJ_Btn_Change = "xpath =.//*[@id='modifyButton']"
OBJ_Chk_MemberMessages = "xpath = .//*[@name='notificationPreference(FROM_MEMBER_email)']"
OBJ_Chk_AdminMessages = "xpath=.//*[@name='notificationPreference(FROM_ADMIN_TO_MEMBER_email)']"
OBJ_Btn_NotificationSubmit = "xpath =.//*[@id='submitButton']"
OBj_Btn_Back = "xpath=.//*[@id='backButton']"

##############################                      Manage Administrator               ###############################
OBJ_Lnk_ManageAdmins = "xpath=//*[@id='submenu5.3']/span[2]"
OBJ_List_CreateAdministrator = "xpath=//*[@id='newAdminGroup']"

##############################                      Create Account Administrator               ###############################
OBJ_Txt_AccountAdminLoginName = "xpath=//tr[2]/td[2]/input[contains(@class, 'large InputBoxEnabled required')]"
OBJ_Txt_AccountAdminFullName = "xpath=//tr[3]/td[2]/input[contains(@class, 'large InputBoxEnabled required')]"
OBJ_Txt_AccountAdminEmail = "xpath=//tr[4]/td[2]/input[contains(@class, 'large InputBoxEnabled required')]"
OBJ_Txt_AccountAdminPassword = "xpath=//tr[5]/td[2]/input[contains(@class, 'small InputBoxEnabled required')]"
OBJ_Txt_AccountAdminConfirmPwd = "xpath=//tr[6]/td[2]/input[contains(@class, 'small InputBoxEnabled required')]"
OBJ_Btn_AccountAdminSaveAndOpen = "xpath=//input[@id='saveAndOpenProfileButton']"

##############################                      Create New Permission Group               ###############################
OBJ_Btn_NewGroupSubmit = "xpath=//*[@id='newButton']"
OBJ_List_Type = "xpath=//*[@id='naturesSelect']"
OBJ_Txt_Name = "xpath=//tr[3]/td[2]/input[contains(@class, 'full InputBoxEnabled')]"
OBJ_Txt_AppURL = "xpath=//tr[4]/td[2]/input[contains(@class, 'full InputBoxEnabled')]"
OBJ_TxtArea_Description = "xpath=//textarea"
OBJ_Btn_SavePermissionGroup = "xpath=//*[@id='saveButton']"

##############################                      Edit Member Group Settings               ###############################
OBJ_Lnk_PermissionGroups = "xpath=//li[@id='submenu5.7']/span[contains(@class, 'subMenuText')]"
OBJ_Img_EditPGDisabledBroker = "xpath=//tr[contains(@class, 'ClassColorSelected')]/td[3]/img[contains(@class, 'edit groupDetails')]/@src"
OBJ_Btn_ChangeMemberGroupSettings = "xpath=//*[@id='modifyButton']"
OBJ_Txt_AppURLModify = "xpath=//tr[4]/td[2]/input[contains(@class, 'full InputBoxEnabled')]"
OBJ_TxtArea_DescModify = "xpath=//textarea"
OBJ_Txt_MaxProfileImages = "xpath=//tr[5]/td[2]/input[contains(@class, 'tiny number InputBoxEnabled')]"
OBJ_List_PasswordPolicy = "xpath=//fieldset[3]/table[contains(@class, 'defaultTable')]/tbody/tr[4]/td[2]/select[contains(@class, 'InputBoxEnabled')]"
OBJ_List_AdPublication = "xpath=//tr[5]/td[2]/select[contains(@class, 'InputBoxEnabled')]"
OBJ_Btn_SaveGroupSettings = "xpath=//*[@id='saveButton']"

##############################                      Edit Permission Group               ###############################
OBJ_Btn_EditPermission = "xpath=//*[@id='groupPermissionsButton']"
OBJ_Btn_ChangePermission = "xpath=//*[@id='modifyButton']"
OBJ_Chk_AuthorizedPayments = "xpath=//input[@id='chk_memberAccount.authorizedInformation']"
OBJ_Chk_ScheduledPayments = "xpath=//input[@id='chk_memberAccount.scheduledInformation']"
OBJ_Chk_ViewCards = "xpath=//input[@id='chk_memberCards.view']"
OBJ_Chk_ViewInvoices = "xpath=//input[@id='chk_memberInvoices.view']"
OBJ_List_MemberProfile = "xpath=//div[@id='permission(canViewProfileOfGroups)']/table/tbody/tr/td[contains(@class, 'multiDropDownText multiDropDownLabel')]"
OBJ_Chk_DisabledBroker = "xpath=//div[contains(@class, 'multiDropDownHover')]/div[contains(@class, 'multiDropDownOption')]/input[contains(@class, 'checkbox')]"
OBJ_List_Messages = "xpath=//div[@id='permission(messageCategories)']/table/tbody/tr/td[contains(@class, 'multiDropDownText multiDropDownLabel')]"
Obj_Chk_administrator = "xpath=//div[contains(@class, 'multiDropDownHover')]/div[contains(@class, 'multiDropDownOption')]/input[contains(@class, 'checkbox')]"
OBJ_Chk_ManageNotifications = "xpath=//input[@id='chk_memberPreferences.manageNotifications']"
OBJ_Chk_ManageAdInterests = "xpath=//input[@id='chk_memberPreferences.manageAdInterests']"
OBJ_Chk_ManageReceiptPrinters = "xpath=//input[@id='chk_memberPreferences.manageReceiptPrinterSettings']"
OBJ_Btn_SubmitPermissionChanges = "xpath=//*[@id='saveButton']"

##############################  Veena
### Accounts 
Obj_Lnk_Accounts="xpath=.//*[@id='menu3']/span[2]"


### Accounts > Manage Currencies
Obj_Lnk_ManageCurrencies = "xpath=.//span[contains(.,'Manage Currencies')]"
Obj_Btn_NewCurrency="xpath=.//*[@id='newButton']"
Obj_Txt_CurrencyName="xpath=.//*[@name='currency(name)']"
Obj_Txt_CurrencySymbol="xpath=.//*[@name='currency(symbol)']"
Obj_Txt_CurrencyPattern="xpath=.//*[@name='currency(pattern)']"
Obj_Txt_DescriptionTxt="xpath=.//*[@id='descriptionText']"
Obj_Btn_SaveCurrency = "xpath=.//*[@id='saveButton']"
Obj_Btn_Back = "xpath=.//*[@id='backButton']"
Obj_Tbl_Currencies = "xpath=.//*[@class='defaultTable']/tbody"
Obj_Tbl_CurrenciesRows=".//*[@class='defaultTable']/tbody/tr"
Obj_Tbl_CurrenciesRow="xpath=.//*[@class='defaultTable']/tbody/tr"
Obj_Img_ModifyCurrency = "xpath=.//*[@class='defaultTable']/tbody/tr["
Obj_Btn_ChangeCurrency = "xpath=.//*[@id='modifyButton']"


### Accounts > Manage Accounts
Obj_Lnk_ManageAccounts= "xpath=.//span[contains(.,'Manage Accounts')]"
Obj_Btn_NewAccount="xpath=.//*[@id='newButton']"
Obj_Cmb_AccountType = "xpath=.//*[@id='natureSelect']"
Obj_Txt_AccountName="xpath=.//*[@name='accountType(name)']"
Obj_Txt_AccDesc = "xpath=.//*[@id='descriptionText']"
Obj_Cmb_AccountCurrency="xpath=.//*[@name='accountType(currency)']"
Obj_Btn_SaveAccount = "xpath=.//*[@id='saveButton']"
Obj_Img_ModifyAccount = "xpath=.//*[@class='defaultTable']/tbody/tr["
Obj_Btn_ChangeAccount = "xpath=.//*[@id='modifyButton']"

Obj_Lnk_SystemAccounts = "xpath=.//span[contains(.,'System Accounts')]"
Obj_Btn_Search = "xpath=.//input[@value='Search']"
Obj_Txt_AccountBalance = "xpath=.//tr[contains(.,'Account balance')]/td[@class='headerField']"
Obj_Lnk_MemberPayment = "xpath=.//span[contains(.,'Member Payment')]"
Obj_Txt_RecipientLogin = "xpath=.//*[@id='memberUsername']"
Obj_Txt_RecipientName = "xpath=.//*[@id='memberName']"
Obj_Lnk_SystemPayment="xpath=.//span[contains(.,'System Payment')]"


#####  Bookkeeping
Obj_Lnk_Bookkeeping = "xpath=.//span[contains(.,'Bookkeeping')]"
Obj_Lnk_ManageExternalAccounts = "xpath=.//span[contains(.,'Manage External Accounts')]"
Obj_Lnk_ExternalAccounts = "xpath=.//li[@id='submenu4.1']"
Obj_Txt_ExternalAccountName = "xpath=.//input[@name='externalAccount(name)']"
Obj_Cmb_SystemAccountType = "xpath=.//select[@name='externalAccount(systemAccountType)']"
Obj_Cmb_MemberAccountType = "xpath=.//select[@name='externalAccount(memberAccountType)']"
Obj_Btn_ChangeExternalAccount = "xpath=.//input[@value='Change']"

Obj_Btn_NewPaymentType="xpath=.//*[@id='newButton']"
Obj_Txt_externalTransferName = "Xpath=.//input[@name='externalTransferType(name)']"
Obj_Txt_externalTransferCode = "Xpath=.//input[@name='externalTransferType(code)']"
Obj_Txt_externalTransferAction = "Xpath=.//*[@id='actionSelect']"
Obj_Tbl_PaymentTypeRows=".//*[@class='tdContentTableLists innerBorder']/table/tbody/tr"
Obj_Tbl_PaymentTypeRow="xpath=.//*[@class='tdContentTableLists innerBorder']/table/tbody/tr"
Obj_Img_ModifyPayment = "xpath=.//*[@class='tdContentTableLists innerBorder']/table/tbody/tr["
Obj_Lnk_ExternalAccounts="xpath=.//span[contains(.,'External accounts')]"

Obj_Btn_ExternalPayment = "xpath=.//*[@id='newPaymentButton']"
Obj_Cmb_ExternalTransferType = "xpath=.//select[@name='externalTransfer(type)']"
Obj_Txt_ExternalPaymentDate="xpath=.//input[@name='externalTransfer(date)']"
Obj_Txt_ExternalAmount = "xpath=.//input[@name='externalTransfer(amount)']"


##############  Access Device

Obj_Lnk_AccessDevices="xpath=.//span[contains(.,'Access Devices')]"
Obj_Lnk_ManageCardTypes="xpath=.//span[contains(.,'Manage card types')]"
Obj_Btn_NewCardType="xpath=.//*[@id='newButton']"

Obj_Txt_CardTypeName="xpath=.//input[@name='cardType(name)']"
Obj_Txt_CardTypeFormat="xpath=.//input[@name='cardType(cardFormatNumber)']"
Obj_Txt_CardTypeExpiry="xpath=.//*[@id='recurrenceNumberText']"
Obj_Btn_CardTypeSave = "xpath=.//*[@id='saveButton']"


##############  Personal
#Obj_Lnk_Personal="xpath=.//li[contains(.,'Personal')]"
#Obj_Lnk_Profile="xpath=.//span[contains(.,'Profile')]"
#Obj_Lnk_ChangePassword="xpath=.//span[contains(.,'Change Password')]"
##Obj_Lnk_EMailNotifications="xpath=.//span[contains(.,'E-Mail Notifications')]"
##Obj_Btn_ChangeProfile = "xpath=.//*[@id='modifyButton']"
##Obj_Txt_FullName="xpath=.//input[@name='admin(name)']"
##Obj_Txt_AdminEmail="xpath=.//input[@name='admin(email)']"
##Obj_Btn_SaveProfile = "xpath=.//*[@id='saveButton']"




