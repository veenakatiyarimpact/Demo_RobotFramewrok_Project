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






##############################                    Chrome Setting Page                    ##############################  

Obj_Txt_ChromeURL="xpath=//*[@id='content-settings-exceptions-area']/div[2]/div[5]/list/div[5]/div/div/input"
Obj_Txt_ChromeURLNew="xpath=//*[@id='content-settings-exceptions-area']/div[2]/div[5]/list/div[6]/div/div/input"  
                      
Obj_Cmb_ChromeAllow="xpath=//*[@id='content-settings-exceptions-area']/div[2]/div[5]/list/div[5]/div/select"
Obj_Btn_ChromeDone="xpath=//*[@id='content-settings-exceptions-overlay-confirm']"
                       
Obj_Btn_ChromeDoneAgain="xpath=//*[@id='content-settings-overlay-confirm']"
Obj_Txt_ChromeURL1="xpath=//*[@id='content-settings-exceptions-area']/div[2]/div[5]/list/div[5]/div/div/input"                     

					
Obj_Txt_ChromeURLNew1="xpath=.//*[@id='content-settings-exceptions-area']/div[2]/div[5]/list/div[4]/div/div/input"
Obj_Cmb_ChromeAllow1="xpath=.//*[@id='content-settings-exceptions-area']/div[2]/div[5]/list/div[6]/div/select"
Obj_Lbl_ChromeSetting="xpath=.//*[@id='content-settings-exceptions-area']/h1"
Obj_Txt_ChromeURL1Test4="xpath =.//*[@id='content-settings-exceptions-area']/div[2]/div[5]/list/div[5]/div/div/input"
Obj_Cmb_ChromeAllow1Test4="Xpath=.//*[@id='content-settings-exceptions-area']/div[2]/div[5]/list/div[5]/div/select"
 

##############################################################################################################

##############################                    Upper Header         ##############################

Obj_Lbl_CardNo="xpath=//*[@id='cardNumberHeader']"

##############################################################################################################


##############################                    Login Page                    ##############################                             

Obj_Txt_Username="xpath=.//*[@name='username']"
Obj_Txt_Password="xpath=.//*[@name='password']"

##############################################################################################################

##############################                    Select Sales Link Page                    ##############################

Obj_Lnk_Sales="xpath=.//*[contains (@href,'servicepoint')]"
Obj_Lnk_SPM="xpath=.//a[contains (@href,'startSPMSearch')]"
Obj_Lnk_TransFolio="xpath=.//a[contains (@href, 'cm-gui/#')]"
#Obj_Lnk_TransFolio="xpath=//*[@id='content']/ul/li[16]/a"

##############################################################################################################

##############################                    Start Sales Page                    ##############################

Obj_Lnk_InEnglish="xpath=.//*[@id='languageChange']/a[1]"
Obj_Lnk_Logout="xpath=.//a[contains (text(),'log out')]"
Obj_Lnk_StartSales="xpath=.//a[@id='startSalesNavigator']"
Obj_Lnk_CustReg="xpath=.//*[@id='customerRegisterNavigator']"
Obj_Txt_PersonID="xpath=.//*[@id='searchText1']"
Obj_Btn_Continue="xpath=//*[@id='submitBtnId']"
Obj_Cmb_CustType="xpath=//*[@id='dropDownOption1']"
Obj_Btn_ReadCard="xpath=//*[@id='readCard1']"
Obj_Btn_CreateArtID="xpath=.//input[contains(@value,'Create')]"
Obj_Txt_BirthDateAID="xpath=.//*[@id='birthdate']"
Obj_Sel_GenderAID="genderS"
Obj_Btn_CreateIDAID="xpath=.//*[@id='closebtn']"
Obj_Btn_CloseAID="xpath=.//*[@id='invoicePersonPopup']//.//*[@class='wh-button marR5 float-left']"

Obj_Txt_PersonID1="xpath=.//*[@id='searchText2']"
Obj_Cmb_CustType1="xpath=//*[@id='dropDownOption2']"



##############################################################################################################

##############################                    Create Person Page                    ##############################

Obj_Txt_LastName="xpath=.//*[@name='lastName']"
Obj_Txt_FirstName="xpath=//*[@name='firstName']"
Obj_Cmb_Language="xpath=//*[@id='customerContactInfo.language']"
Obj_Cmb_CustGrp="xpath=.//select[contains (@name,'customerGroup')]"
Obj_Txt_StreetAddCust="xpath=//*[@id='customerContactInfo.address.addressStreet']"
Obj_Txt_PostalCode="xpath=//*[@id='customerContactInfo.address.addressPostalCode']"
Obj_Txt_City="xpath=//*[@id='customerContactInfo.address.addressCity']"
Obj_Txt_Country="xpath=//*[@id='customerContactInfo.address.addressCountry']"
Obj_Txt_Phone="xpath=//*[@id='customerContactInfo.phoneNumber']"
Obj_Txt_Email="xpath=//*[@id='customerContactInfo.emailAddress']"
Obj_Btn_SavePerson="xpath=.//*[@id='submitPerson']"  
Obj_Btn_MakePOA="xpath=.//*[@id='makePoaBtn']"
Obj_Txt_PersonID_POA="xpath=.//*[@id='searchHetu']"
Obj_Btn_SearchPOA="xpath=.//*[@id='poaCreateSearchBtn']"
Obj_Btn_ConfirmPOA="xpath=.//*[@id='poaCreateConformBtn']"
Obj_DTP_StartDate="xpath=.//*[@id='startDate']"
Obj_DTP_EndDate="xpath=.//*[@id='endDate']"
Obj_Lnk_POA="xpath=.//*[@id='poaLinkForCreate']"
Obj_Tbl_MainDiv="xpath=.//*[@id='mainDiv']"
Obj_Btn_DeletePOA="xpath=.//input[contains (@value,'Delete') and contains (@class,'button float-right')]"
Obj_Btn_ClosePOA="xpath=.//*[@id='poaCloseBtn']"
Obj_Tbl_SearchPOADiv="xpath=.//*[@id='searchPOApopupDiv']"
Obj_Btn_SearchPRCCUST="Xpath=.//*[contains (@value,'Search')]"
Obj_Lbl_StreetAdd="xpath=.//*[@id='prcAddr.addressStreet.lbl']"
Obj_Lbl_Municipality="xpath=.//*[@id='prcAddr.addressMunicipal.lbl']"
Obj_Lbl_PostalCode="xpath=.//*[@id='prcAddr.addressPostalCode.lbl']"
Obj_Lbl_City="xpath=.//*[@id='prcAddr.addressCity.lbl']"
Obj_Btn_ReturnCust="xpath=.//*[contains(@class,'button float-right') and contains (@value,'Return')]"
Obj_Btn_ClearFieldsPerson="xpath=.//*[@id='clearPerson']"
Obj_Lbl_PostalCodeNormalCust="xpath=.//*[@id='customerContactInfo.address.addressPostalCode']//preceding-sibling::label"
Obj_Lbl_CityNormalCust="xpath=.//*[@id='customerContactInfo.address.addressCity']//preceding-sibling::label"
Obj_Lbl_PRCInfo="xpath=.//*[@class='labelbox '][1]"
Obj_Lbl_InformationOnRecentlyUpdatedCard="xpath=.//*[@class='labelbox '][2]"
Obj_Chk_Entitled="xpath=.//*[@id='escortCheckBox']"
Obj_Ico_Entitled="xpath=.//li[contains (@title,'Entitled to escort')]"
Obj_Lnk_AddNote="xpath=.//a[contains (text(),'Add note')]"
Obj_Txt_NoteCust="xpath=.//*[@id='note']"
Obj_Btn_DeleteNote="xpath=.//*[@id='deleteNote']/input"
Obj_Btn_CloseNoteCust="xpath=.//*[@id='closeButton']"
Obj_Btn_SaveNoteCust="xpath=.//*[@id='noteSaveButton']"
Obj_Lbl_NoteDisplay="xpath=.//*[@id='notesDisplay']"
Obj_Btn_ConfirmCustNoteDelete="xpath=.//*[@id='noteDeleteButton']"

Obj_Popup_ProtectionOrder="xpath=.//*[@id='prcPersonProtectionOrderPopup']"


##############################################################################################################

##############################                    Create Company/Dept/Unit Page                    ##############################

Obj_Txt_CompName="xpath=.//*[@id='companyNameId']"
Obj_Txt_DeptUnitID="xpath=.//*[@id='yId']"
Obj_Txt_SignAuth1="xpath=//*[@id='signatureAuthority1.name']"
Obj_Lbl_CompNoteDisplay="xpath=.//*[@id='companyNotes']"
Obj_Btn_ClearFieldsCompany="xpath=//*[@id='clearFields']"

#######################################################      Shared Objects      #######################################################

Obj_Txt_ContactPer="xpath=//*[@id='customerContactInfo.contactPerson']"
Obj_Btn_SaveCompany="xpath=//*[@id='submitCompany']"
Obj_Btn_AddNew="xpath=.//input[contains (@value,'Add new')]"     

##############################################################################################################

##############################                    Limited View Page                  ##############################

Obj_Lnk_ShowEditPerson="xpath=.//*[contains (@href,'displayPersonInfoDetail')]"
Obj_Btn_NewCard="xpath=//*[@id='newCardBtn']"
Obj_Lnk_ShowEditCompany="xpath=.//*[contains (@href,'getCompanyDetails')]"
Obj_Lnk_ReplaceCard="xpath=.//a[contains(text(),'Replace card')]"
Obj_Btn_ContinueReplaceCard="xpath=.//*[@id='cnfReplaceCardBtn']"
Obj_Btn_ReadCardReplace="xpath=.//*[@id='readTravelCard']"
Obj_Btn_ConfirmReplaceCard="xpath=.//*[@id='confirmButton']"
Obj_Tbl_CardData="xpath=.//div[contains (@class,'scroll')]"
Obj_Lbl_CustID="xpath=.//*[@class='title']"
Obj_Lbl_CustIDCompany="xpath=.//*[@class='Ico-company-Wh']"
Obj_Lnk_CardNo="xpath=.//li[@class='trdetl cursor-pointer']/a"


##############################################################################################################
                                
##############################                    Sell Card Page                ##############################

Obj_Btn_SellCard="xpath=//*[@id='sellCardSubmit']"
Obj_Sel_CardType="cardType"

Obj_Sel_CardTypeMWOCI="xpath=.//*[@id='multiCardType']"   # Sell Card Page
Obj_Sel_CardTypeMWCI="xpath=.//*[@id='multiCardTypeWC']"     # Sell Card Page
Obj_Sel_CardTypePersonal="xpath=.//*[@id='personalCardType']"  # Sell Card Page
Obj_Cmb_HomeMunicipalitySellCard="xpath=.//*[@id='multiuserMunicipality']" # Sell Card Page
Obj_Cmb_PersonalMuncipality="xpath=.//*[@id='personalMunicipality']"  # Sell Card Page
Obj_Txt_ValidUntillPersonal="xpath=.//div[@id='personalMunicipalityValidUntil']/input"  # Sell Card Page
Obj_Txt_ValidUntilSellCard="xpath=.//div[@id='multiuserMunicipalityValidUntil']/input"  # Sell Card Page
Obj_Chk_SellCardFree="xpath=.//*[@id='sellFreeOfCharge']" # Sell Card Page
Obj_Cmb_SellCardFreeReason="xpath=.//*[@id='reasonDropdown']"  # Sell Card Page
Obj_Cmb_CustGrpSellCard="xpath=//*[@id='custGroupsMultiUser']" # Sell Card Page

Obj_Lbl_MunciLock="xpath=.//*[@id='municipality_locked']"

##############################################################################################################

##############################                    Load Card Page                ##############################

Obj_Btn_LoadVal="xpath=//*[@id='loadValueBtn']"
Obj_Cmb_TktProd="xpath=//*[@id='cardSaleVo.ticketCode']"
Obj_Cmb_Area="xpath=//*[@id='cardSaleVo.validityArea']"
Obj_Txt_NoOfDays="xpath=//*[@id='cardSaleVo.days']"
Obj_Btn_LoadSeason="xpath=//*[@id='loadSeasonTicketBtn']"
Obj_Txt_LoadVal="xpath=//*[@id='cardSaleVo.loadTicketAmount']"
Obj_Txt_ToDate ="xpath=//*[@id='cardSaleVo.toDate']"
Obj_Lbl_ValOnCard="xpath=//*[@id='cardValue']"
Obj_Lbl_Dates="xpath=.//*[@id='periodBox1']"
Obj_Lbl_PeriodDuration="xpath=//*[@id='period1Calc']"
Obj_Cmb_LanguageUpdateCard="xpath=//*[@id='languageId']"
Obj_Btn_UpdateCard="xpath=//*[@id='updateCardBtn']"
Obj_Lnk_ChangeCardStatus="xpath=.//*[@id='openCardStatusLinkId']"


Obj_Btn_ContinueCardStatus="xpath=//*[@id='saveChanges']"
Obj_Txt_NoteLost="xpath=//*[@id='noteLost']"
Obj_Btn_ConfirmLost="xpath=//*[@id='confirmlostBtn']"
Obj_Btn_PaySB="xpath=.//*[contains (@value,'Pay (')]"
Obj_Lbl_SBDeatils="xpath=.//ul[@id='shopping']"
Obj_Sel_CardStatus="test"
Obj_Btn_ConfirmDead="xpath=//*[@id='confirmbtn']"
Obj_Btn_DoNotRepalceDead="xpath=//*[@id='closeBtnreplacedBlacklistCardPopup']"
Obj_Txt_LoadCardPersonID="xpath=.//*[@id='linkedHetu']"
Obj_Txt_LoadCardBusinessID="xpath=.//*[@id='linkedYid']"
Obj_Btn_LinkCard="xpath=.//*[@id='linkPersonOrCompany']"
Obj_Lbl_CustomerID="xpath=.//*[@id='customerId']"
Obj_Txt_NoteDeactivate="xpath=.//*[@id='noteEntered']"
Obj_Btn_ConfirmDeactivate="xpath=.//*[@id='confirmDeactiveBtn']"
Obj_Lbl_TotalVal="xpath=//*[@id='totalPrice']"
Obj_Btn_ConfirmAssigneToCust="xpath=//*[@id='confirmBtnActiveConfirm']"
Obj_Cmb_ReasonBlackList="xpath=.//*[@id='reasonDropdownBlacklistCard']"
Obj_Txt_NoteBlackList="xpath=.//*[@id='notes']"
Obj_Btn_ConfirmBlackList="xpath=.//*[@id='confirmBtnBlacklistCard']"
Obj_Lnk_ToValue="xpath=.//a[contains (text(),'To value')]"
Obj_Cmb_ConvertReason="xpath=//*[@id='removalReasons']"
Obj_Btn_ConvSeason="xpath=.//*[@id='convSeasonValConfirmBtn']"
Obj_Lbl_CardNoType="xpath=.//*[contains (@class,'marB10')]//div[contains (@class,'bluebar')]"
Obj_Lbl_DatesAnother="xpath=.//*[@id='periodBox2']"
Obj_Lbl_PeriodDurationAnother="xpath=//*[@id='period2Calc']"
Obj_Txt_LoadCardBusinessIDPC="xpath=.//*[contains(@id,'linkedYid')]"
Obj_Btn_LinkCardPC="xpath=.//*[@id='linktoCompany']"
Obj_Btn_Unlink="xpath=.//*[@id='unlinkPersonOrCompany']"


Obj_Txt_FromDate="xpath=//*[@id='cardSaleVo.fromDate']"



##############################################################################################################

##############################                    Shopping Basket Page          ##############################

obj_Btn_BypassCashRegister="xpath=.//input [contains (@value,'Bypass cash register')]"
Obj_Lbl_SBCard ="xpath=.//*[@id='row']//img[contains (@src,'Enabled')]//.."
Obj_Tbl_Listing="xpath=.//*[@id='allinfo'][@class='shopping-scroll']"
Obj_Btn_ContinueByPassRegister="xpath=.//*[@id='continueButton']"
Obj_Btn_MoveToCashReg="xpath=.//input [contains (@value,'Move to cash register')]"
Obj_Btn_ReturnSB="xpath=.//*[@id='returnBasketBtnGlobalId']"
Obj_Btn_PayWithEmpVoucher="xpath=.//*[@id='showVoucher']"
Obj_Btn_PayWithGiftVoucher="xpath=.//*[@id='showGift']"


Obj_Txt_VoucherCode="xpath=.//*[@id='voucherCode']"
Obj_Txt_GiftVoucherCode="xpath=//*[@id='giftVoucherCode']"
Obj_Btn_ConfirmPay="xpath=.//*[@id='voucherCodeBtn']"
Obj_Btn_GiftConfirmPay="xpath=//*[@id='giftVoucherCodeBtn']"
Obj_Lnk_CancelCardSale="xpath=.//*[contains (text(),'Travel card sale')]//preceding-sibling::td[1]//a"
Obj_Lnk_CancelLoadSeason="xpath=.//*[contains (text(),'Load season')]//preceding-sibling::td[1]//a"
Obj_Lnk_CancelLoadValue="xpath=.//*[contains (text(),'Load value')]//preceding-sibling::td[1]//a"
Obj_Lnk_CancelAll="xpath=.//*[contains (@src,'cardEnabled')]//..//preceding-sibling::li[1]//a"

Obj_Lbl_TravelCardSale="xpath=.//*[contains (text(),'Travel card sale')]"
Obj_Lbl_LoadSeason="xpath=.//*[contains (text(),'Load season')]"
Obj_Lbl_LoadValue="xpath=.//*[contains (text(),'Load value')]"


Obj_Lbl_SccCardSale="xpath=.//*[contains (text(),'Single charge card sell')]"
Obj_Lnk_CancelSCCSale="xpath=.//*[contains (text(),'Single charge card sell')]//preceding-sibling::td[1]//a"
Obj_Lnk_CancelAllSCC="xpath=.//*[contains (@src,'sccEnabled')]//..//preceding-sibling::li[1]//a"

Obj_Lnk_PayByVal="xpath=.//*[@id='showCard']"


Obj_Txt_TravelCardVal="xpath=.//*[@id='travelCardVal']"
Obj_Btn_ConfirmPayByVal="xpath=.//*[@id='travelCardValBtn']"



Obj_Lbl_CancelSeasonRefund="xpath=.//*[contains (text(),'Season refund')]//preceding-sibling::td[1]//a"   ### SIT ###

#############################################################################################################

##############################                    Read Card SCC       ##############################

Obj_Tbl_LoadSesonBox="xpath=.//*[@id='loadSeasonBox']"

##############################                   Customer_Register_Search_Person        #######################

Obj_Txt_CustRegPersonId="xpath=.//*[@id='personId']"
Obj_Cmb_Reason="xpath=.//*[@id='custRegSearchReason']"
Obj_Btn_CustRegSearch="xpath=.//*[@id='submitBtnId']"
Obj_Lnk_CustId="xpath=.//a[contains (text(),'"
Obj_Txt_CustId="xpath=.//*[@id='customerNumber']"
Obj_Txt_CustRegBusinessId="xpath=//*[@id='businessId']"

Obj_Btn_ClsLostFound="xpath=.//*[@id='saveChanges']//preceding-sibling::input[1]"   # Customer Register 
Obj_Btn_RtnLostFound="xpath=.//*[@id='confirmlostBtn']//preceding-sibling::input"   # Customer Register
Obj_Lnk_ChangeCardStatusCustReg="xpath=//div[@class='lsting'][2]//a [contains (@href,'#')]"   # Customer Register
Obj_Btn_RtnAssigntoCust="xpath=.//*[@id='confirmBtnActiveConfirm']//preceding-sibling::input"   # Customer Register
Obj_Lbl_AdditionalInfo="xpath=.//*[@id='cardStatusLostVerifyPopup']/div[2]/div[3]/ul/li[2]/div[1]"   # Customer Register
Obj_Lbl_AssignToCustPopupHeader="xpath=.//*[@id='cardStatusVerifyPopup']/div[1]"   # Customer Register
Obj_Lbl_CardIcon="xpath=.//*[@id='cardOnReader_lost']"  # Customer Register
Obj_Lbl_CardIconAssigned="xpath=.//*[@id='cardOnReader_lost']"  # Customer Register
Obj_Lbl_CardNoAssigned="xpath=.//*[@id='cardNumberHeaderActiveVerify']" # Customer Register
Obj_Lbl_CardNoLostFound="xpath=.//*[@id='cardNumberHeaderFoundVerify']" # Customer Register 
Obj_Lbl_CharacterLimit="xpath=.//*[@id='cardStatusLostVerifyPopup']/div[2]/div[3]/ul/li[2]/div[2]"    # Customer Register
Obj_Lbl_LostFoundPopupHeader="xpath=.//*[@id='cardStatusLostVerifyPopup']/div[1]"   # Customer Register
Obj_Lbl_ReplaceCard="xpath=.//a[contains (text(),'Replace card')]//.."   # Customer Register
Obj_Lbl_ServiceProName="xpath=.//*[@id='serviceProviderName']"   # Customer Register
Obj_Lbl_SearchResultInfoCompany ="xpath=.//div[@id='searchresult_info'and contains (text(),'search results for')]" # Customer Register
Obj_Lbl_LostAndFoundDate="xpath=.//*[@id='lostAndFoundChangeDateId']"  # Customer Register


##############################################################################################################

##############################                Edit and Remove_Person_Customer                     ######################

Obj_Btn_Remove_Customer="xpath=.//*[@id='removeCustomerBtn']"
Obj_Cmb_SelectRemove_Reason="xpath=.//*[@id='removalReasons']"
Obj_Btn_Remove_Continue="xpath=.//*[@id='removeCustomerPopupNextbtn']"
Obj_Btn_Remove_Confirm="xpath=.//*[@id='removeCustomerReasonConfirmPopupbtn']"
Obj_Btn_Remove_Close="xpath=.//*[@id='afterCustomerRemovedClosebtn']"
Obj_Lbl_RemoveCustMsg="xpath=.//div[@id='info']//div[contains(.,'No search result for') and contains(.,'"
Obj_Lnk_AllCards="xpath=.//a[contains(text(),'s cards')]"
Obj_Btn_ReleaseCard="xpath=//*[@id='removeTravelCard']"
Obj_Cmb_ReleaseReason="xpath=//*[@id='reasonDropdown']"
Obj_Btn_ReleaseContinue="xpath=//*[@id='continuebtn']"
Obj_Btn_ReleaseClose="xpath=//*[@id='closeBtn']"
#Obj_Btn_RelaseConfirm="xpath=//*[@id='confirmbtn']"
Obj_Btn_RelaseConfirm="xpath=//*[@id='confirmReleaseCardBtn']"

Obj_Lbl_CustomerNo_Person="xpath=.//*[@id='info']//span [contains(.,'/')]"
Obj_Lbl_CustomerNo_Company="xpath=.//*[@id='companyform']//span [contains(.,'/')]"


##############################################################################################################


##############################                SCC Read                  ######################

Obj_Btn_Read_SCC="xpath=.//*[@id='readCard2']"
Obj_Sel_HourHours_SCC="singleChargeCard.ticketType"
Obj_Sel_Custgrp_SCC="customerGroup"
Obj_Cmb_Ticket_product="xpath=.//*[@id='sellScc.singleChargeCard.proposals']"
Obj_Cmb_Validity_Area="xpath=.//*[@id='validityArea']"
Obj_Txt_Number_Of_Tickets="xpath=.//*[@id='cardPcs']"
Obj_Btn_Confirm="xpath=.//*[@id='confirmBtnId']"
Obj_Lbl_SuccessMsg="xpath=.//*[@id='successMessageTrId']/td[1] [contains(.,'Loading to card') and contains(.,'was successful') and contains(.,'"
Obj_Lnk_CardHistory="xpath=.//a[contains (text(),'Card history')]"  

##############################################################################################################

##############################                Card History                 ######################

Obj_Wnd_CardHistoryWindow="name=undefined"
Obj_Tbl_CardHistory=".//*[@id='eventTransactionsTabId']/tbody/tr"
Obj_Lbl_CardHistoryCell="xpath=.//*[@id='eventTransactionsTabId']/tbody/tr["
Obj_Lnk_StartDateCH="xpath=.//input[@id='filterStartDate']//following-sibling::a"
Obj_Txt_StartDateCH="xpath=.//*[@id='filterStartDate']"
Obj_Btn_SearchCH="xpath=.//button"
Obj_Lnk_AdvBasicSearch="xpath=.//*[@id='displayText']"

Obj_Lbl_CustDataUpdate="xpath=.//*[@id='customerDataUpdate']/following-sibling::label"
Obj_Lbl_LoadSeasonTkt="xpath=.//*[@id='loadingSeasonTicket']/following-sibling::label"
Obj_Lbl_LoadValCH="xpath=.//*[@id='loadingValue']/following-sibling::label"
Obj_Lbl_UseOfVal="xpath=.//*[@id='useOfValue']/following-sibling::label"
Obj_Lbl_CSUpdate="xpath=.//*[@id='cardStatusUpdate']/following-sibling::label"

Obj_Sel_CHEntries="xpath=.//*[@id='eventTransactionsTabId_length']/label/select"


Obj_Lbl_NoofEntriesInfo="xpath=.//*[@id='eventTransactionsTabId_info']"

Obj_Chk_CardHisCardStatusUpdate="xpath=.//*[@id='cardStatusUpdate']"


Obj_Tbl_CardDetailsTbl1="xpath=.//*[@id='allinfo']/div[1]"
Obj_Tbl_CardDetailsTbl2="xpath=.//*[@id='allinfo']/div[2]"

Obj_Lbl_CardNoCardHistory="xpath=.//*[@id='blbox']/li/h1"
Obj_Lbl_CardHistoryInfo="xpath=.//*[@id='blboxFlr']/li/span"

Obj_Lbl_CardNoImg="xpath=.//*[@id='blbox']/li/h1/img"






##############################################################################################################
    
    


##############################                Vouchers Screen                 ######################



Obj_Lnk_Wholesale="xpath=.//a[contains(@href,'Voucher')]"
Obj_Btn_VouchersContinue="xpath=//*[@id='continueBtn']"
Obj_Sel_Voucher="voucherType"   #GIFT #COMMUTER
Obj_Lnk_VoucherStock="xpath=//*[@id='voucherStockId']"
Obj_Lbl_VoucherRange="xpath=//*[@id='voucherStockResultTab']/tbody/tr[1]/td[1]"
Obj_Lbl_VoucherValue="xpath=//*[@id='voucherStockResultTab']/tbody/tr[1]/td[2]"  

Obj_Btn_VouchersClose="xpath=//*[@id='closeId']"
Obj_Txt_VoucherCode="xpath=//*[@id='voucherCode']"
Obj_Txt_VoucherSubCode="xpath=//*[@id='voucherSubCode']"
Obj_Txt_VoucherNum="xpath=//*[@id='voucherFirstSN']"
Obj_Txt_VoucherCount="Xpath=//*[@id='numberOfVouchers']"
Obj_Cmb_VoucherPricingMethod="xpath=//*[@id='pricingMethodId']"
Obj_Cmb_VoucherPaymentMethod="xpath=//*[@id='paymentMethodId']"
Obj_Txt_VoucherLast="xpath=//*[@id='voucherLastSN']"
Obj_Btn_VoucherAdd="xpath=//*[@id='addVoucherButtonId']"
Obj_Btn_SellVouchers="xpath=//*[@id='sellVouchers']"

Obj_Lnk_PrePrintedSCC="xpath=.//a[contains (@href,'wholesalePrePrinted')]"
Obj_Btn_SellSCC="xpath=.//*[@id='sellOrderBtn']"
Obj_Btn_SellConfirm="xpath=.//*[@id='sellConfirmBtn']"
Obj_Lbl_GetVoucher="xpath=.//div[@class='registerform']"      # New

Obj_Lnk_CancelVoucher="xpath=.//*[@id='"

##############################################################################################################
    
    


##############################                SPM                  ######################



##############################                Search Page                  ######################


Obj_Btn_CreateNew="xpath=.//a[contains(.,'Create new')]"      
Obj_Lnk_ServiceProvider="xpath=.//a[contains (@href,'ServiceProvider')]"
Obj_Lnk_AddGroup="xpath=.//a[contains (text(),'Add group')]"
Obj_Txt_ServiceproName="xpath=.//*[@id='serviceProviderName']"
Obj_Btn_Search="xpath=.//*[@id='submitBtnId']"
Obj_Sel_Entries="xpath=.//select[contains (@name,'groupAndSalesPointSearchResult_length')]"
Obj_Lnk_DisplayInfo="xpath=.//a[contains(@href,'Id="
Obj_Btn_Expand="xpath=.//span[contains (@class,'openmenu')]"
Obj_Txt_RangeFrom="xpath=.//*[@id='rangeBoxFrom']"
Obj_Txt_RangeTo="xpath=.//*[@id='rangeBoxTo']"


##############################################################################################################


######################################### Add Group   ##############################################


Obj_Btn_AddGrpCreateNew="xpath=.//*[@id='dropDownButton']"
Obj_Btn_AddGrpSearch="xpath=.//*[@id='searchButton']"
Obj_Btn_AddGrpBack="xpath=.//*[@id='returnBtnGlobalId']"
Obj_Btn_AddGrpBackNew="xpath=.//*[@id='returnBtnId']"
#xpath=.//*[@id='returnBtnGlobalId']
Obj_Btn_AddGrpTerminate="xpath=.//*[@id='terminateBtn']"
Obj_Btn_AddGrpAttachDetach="xpath=.//*[@id='attachedDettachedBtnId']"
Obj_Btn_AddGrpAddServiceProvider="xpath=.//*[@id='addServiceProviderBtnId']"
Obj_Btn_AddGrpConfirm="xpath=.//*[@id='confirmButton']"
Obj_Txt_AddGrpName="xpath=.//*[@id='name']"
Obj_Txt_AddGrpBussId="xpath=.//*[@id='businessId']"
Obj_Txt_AddGrpNote="xpath=.//*[@id='notes']"
Obj_Lbl_Status="xpath=.//*[@id='info']//label[contains(.,'Status')]//following-sibling::*"
Obj_Txt_TerminateNote="xpath=.//textarea[@id='terminationNote' and contains (@name,'terminationNote')]"
  
Obj_Btn_ConfirmTerminate="xpath=.//*[@id='confirmTeminateBtn']"
Obj_Lbl_Date="xpath=.//td[contains(@class,'current-month') and text()='1']"
Obj_Txt_AddGrpID="xpath=.//*[@id='idCopy']"
Obj_Lbl_DatePicker="xpath=.//*[@class='opo-form']//a[contains (@class,'input-date')]"
Obj_Btn_Activate="xpath=.//*[@id='activateBtn']"
Obj_Lbl_Error="xpath=.//*[@id='fieldErrors']"

##############################################################################################################

######################################### Add Service Provider   ##############################################



Obj_Btn_AddSalesPoint="xpath=.//*[@id='addSalesPointButton']"
Obj_Btn_CopyAsTemplate="xpath=.//*[@id='copyAsTemplateButton']"
Obj_Sel_ServiceProviderType="xpath=.//*[@id='type']"
Obj_Txt_ServiceProviderID="xpath=.//*[@id='serviceProviderId']"
Obj_Btn_AddGroup="xpath=.//*[@id='addGroupButton']"
Obj_Txt_InvoicingCustNo="xpath=.//*[@id='invoiceCustomerNumber']"
Obj_Txt_CustRefName="xpath=.//*[@id='customerReferenceNumber']"
Obj_Txt_ServiceProBussID="xpath=.//*[@id='businessId']"
Obj_Txt_StreetAdd="xpath=.//*[@id='streetAddress']"
Obj_Txt_ServiceProPostalCode="xpath=//*[@id='postalCode']"
Obj_Txt_ServiceProEmail="xpath=.//*[@id='emailAddress']"
Obj_Txt_ServiceProPhone="xpath=.//*[@id='phoneNumber']"
Obj_Txt_ServiceProNote="xpath=.//*[@id='notes']"
Obj_Txt_ServiceProCity="xpath=//*[@id='city']"



##############################################################################################################

######################################### Add Sales Point   ##############################################

Obj_Txt_SalesptID="xpath=.//*[@id='salesPointId']"
Obj_Txt_SptArea="xpath=//*[@id='area']"
Obj_Txt_SptContactPer="xpath=//*[@id='contactPerson']"

##############################################################################################################

######################################### Attach/Detach Service Provider   ##############################################

Obj_Txt_SearchServicePro="xpath=.//*[@id='searchId']"
Obj_Opt_ServicePro="xpath=.//option[@value='"
Obj_Btn_Attach="xpath=.//input[@value='Attach']"
Obj_Btn_ServiceProConfirm="xpath=.//*[@id='confirm']"
Obj_Btn_ServiceProSearch="xpath=.//input[@value='Search']"
Obj_Btn_Detach="xpath=.//input[@value='detach']"

                            
######################################### Card History Page   ##############################################

######################################### Card History Page   ##############################################

Obj_Lbl_CHCardNo="xpath=.//*[@id='blbox'][@class='nomar']"
Obj_Lbl_CardType="xpath=//label[text()='CARD:']//..//following-sibling::td[1]"
Obj_Lbl_TransferDate="xpath=//label[text()='CARD:']//..//following-sibling::td[2]"
Obj_Lbl_BoughtFromInfo="xpath=//label[text()='BOUGHT FROM:']//..//following-sibling::td[1]"
Obj_Lbl_CardFeeInfo="xpath=//label[text()='BOUGHT FROM:']//..//following-sibling::td[2]"
Obj_Lbl_PersonInfo="xpath=.//*[@class='Ico-blperson-cus']//..//..//following-sibling::td[1]"
Obj_Lbl_PersonInfoMulti="xpath=.//*[@class='marR5']//..//..//following-sibling::td[1]"
obj_Lbl_CustGrp="xpath=//label[text()='CUSTOMER GROUP:']//.."
Obj_Lbl_CHStatus="xpath=//label[text()='STATUS:']//..//following-sibling::td[1]"
Obj_Lbl_CHValOnCard="xpath=//label[text()='VALUE ON THE CARD:']//..//following-sibling::td[1]"
Obj_Lbl_LatestLoadingValue="xpath=//label[text()='LATEST LOADING VALUE:']//..//following-sibling::td[1]"
Obj_Lbl_LatestLoadingOFSeasonTkt="xpath=//label[text()='LATEST LOADING OF SEASON TICKETS:']//..//following-sibling::td[1]"
Obj_Btn_CHClose="xpath=.//input[contains (@value,'Close')]"

########################################################################################################## 

######################################### Serial Single Charge Card Page   ##############################################             

Obj_Lnk_SerialSingleChargeCards="xpath=.//a[contains (@href,'searchSerial')]"
Obj_Lnk_NewOrder="xpath=.//a[contains (@href,'addSerialOrder')]"
Obj_Txt_SerialBussID="xpath=.//*[@id='businessIdSearch']"
Obj_Btn_SerialSearchCust="xpath=.//*[@id='searchCustomerBtn']"
Obj_Btn_SerialContinue="xpath=.//*[@id='continueBtn']"
Obj_Txt_OrderName="xpath=.//*[@id='name']"
Obj_Sel_TicketType="ticketType"
Obj_Txt_SerialNoOfDays="xpath=.//*[@id='days']"
Obj_Txt_NoOfCards="xpath=.//*[@id='amount']"
Obj_Sel_CustGroup="customerGroup"
Obj_Sel_Language="language"
Obj_Cmb_ProdInfo="xpath=.//*[@id='ticketProductSelect']"
Obj_Cmb_SerialArea="xpath=.//*[@id='validityAreaSelect']"
Obj_Txt_CardText="xpath=.//*[@id='cardText1']"
Obj_Btn_CreateOrder="xpath=.//*[@id='createOrderBtn']"
Obj_Btn_CancelOrder="xpath=.//*[@id='cancelBtn']"
Obj_Btn_ConfirmCancel="xpath=.//*[@id='confirmCancelBtn']"
Obj_Btn_Loss="xpath=.//*[@id='lossBtn']"
Obj_Btn_ConfirmLoss="xpath=.//*[@id='confirmLossBtn']"
Obj_Lbl_OrderNumber="xpath=.//div[@class='whiteLine']//following-sibling::div//h2[contains(.,'Order information')]//..//label[contains(.,'Order number')]//..//following-sibling::td"
Obj_Lbl_OrderStatus="xpath=//div[@class='whiteLine']//following-sibling::div//h2[contains(.,'Order information')]//..//label[contains(.,'Order status')]//..//following-sibling::td"
Obj_Sel_SearchType="searchType"
Obj_Txt_Search="xpath=.//*[@id='searchWithOrderNumberOrName']"
Obj_Chk_StatusInStock="xpath=.//*[@id='statusInStock1']"
Obj_Chk_StatusSold="xpath=.//*[@id='statusSold1']"
Obj_Chk_StatusCancelled="xpath=.//*[@id='statusCancelled1']"
Obj_Chk_StatusLoss="xpath=.//*[@id='statusLoss1']"
Obj_Btn_SerialSearch="xpath=.//*[@id='searchBtn']"
Obj_Lnk_OrderNumber="xpath=.//a[contains (text(),'"
Obj_Lnk_OrderNumber1 = "xpath=.//*[@id='searchresult']/tbody/tr/td[2]/a"
Obj_Btn_ModifyOrder="xpath=.//*[@id='modifyBtn']"
Obj_Txt_NewName="xpath=.//*[@id='newNameField']"
Obj_Txt_NewAmountField="xpath=.//*[@id='newAmountField']"
Obj_Btn_SaveModify="xpath=.//*[@id='saveModifyBtn']"
Obj_Lbl_Custno="xpath=.//*[@class="" and contains (text(),'Customer number')]//..//following-sibling::td[1]"
Obj_Lnk_ManageOrder="xpath=.//a[contains (text(),'Manage orders')]"
Obj_Lbl_OrderName="xpath=.//div[@class='whiteLine']//following-sibling::div//h2[contains(.,'Order information')]//..//label[contains(.,'Order name')]//..//following-sibling::td"
Obj_Lbl_NoofCards="xpath=.//div[@class='whiteLine']//following-sibling::div//h2[contains(.,'Order information')]//..//label[contains(.,'Amount')]//..//following-sibling::td"

              
              
############################################################################################################## 

######################################### Transfolio Card Manager   ##############################################             


Obj_Lnk_Cards="xpath=.//span[contains( @title,'Cards')]"
Obj_Txt_CardNo="xpath=.//input[contains (@class,'ng-pristine')]"
Obj_Tbl_Cards="xpath=.//td[contains (@class,'columnHighlight')]"
Obj_Lnk_BlackList="xpath=.//a[contains (@class,'toolIcon blacklistRemove')]"
Obj_Btn_Remove="xpath=.//input[contains (@value,'Remove') and contains (@class,'btn major')]"


Obj_Lnk_Stocks="xpath=.//span[contains( @title,'Stocks')]"
Obj_Lnk_StockIcon="xpath=.//*[@id='leftStock']/div[1]/following-sibling::div[1]/a"
Obj_Lst_Vouchers="Xpath=.//li[contains(.,'VOUCHERS')]"
Obj_Txt_SearchDataVch="xpath=.//*[@id='vouchers']/section[2]/div[2]/div[4]/form/input"
Obj_Tbl_VoucherStock="xpath=.//*[@id='vouchersInStockGrid']"

Obj_Lnk_ProcessedTran="xpath=.//a[contains (@href,'processed-transactions')]"

Obj_Lnk_GiftVoucherDetailsVM="xpath=.//*[@id='processedTransactionsGrid']/tbody[1]/tr[1]/td[6]/div/a"
Obj_Lnk_EmpVoucherDetailsVM="xpath=.//*[@id='processedTransactionsGrid']/tbody[1]/tr[2]/td[6]/div/a"


Obj_Lbl_TranTypeVM="xpath=.//*[@class='nodeElementName' and contains(.,'Transaction Type')]//..//following-sibling::span"
Obj_Lbl_VoucherTypeVM="xpath=.//*[@class='nodeElementName' and contains(.,'Voucher Type')]/following-sibling::div[1]"
Obj_Lbl_VoucherFirstSNVM="xpath=.//*[@class='nodeElementName' and contains(.,'Voucher First SN')]/following-sibling::div[1]"






######################################### Serial Travel Cards   ##############################################  

Obj_Lnk_SerialTravelCard="xpath=.//a[contains (@href,'sellSerialTravelCard')]"
Obj_Sel_SellNewCard="xpath=.//*[@id='optionOne']"
Obj_Sel_LoadCard="xpath=.//*[@id='optionTwo']"
Obj_Btn_LinkToCompany="xpath=.//*[@id='linkToCompany']"
Obj_Chk_SellCardFree="xpath=.//*[@id='sellFreeOfCharge']"
Obj_Cmb_ReasonFreeCard="xpath=.//*[@id='reasonDropdown']"
Obj_Btn_ConfirmSellLoad="xpath=.//*[@id='confirm']"
Obj_Cmb_TktProdSTC="xpath=//*[@id='cardSaleVo.ticketCode1']"
Obj_Cmb_AreaSTC="xpath=//*[@id='cardSaleVo.validityArea1']"
Obj_Txt_NoOfDaysSTC="xpath=//*[@id='cardSaleVo.days1']"
Obj_Txt_ToDateSTC="xpath=//*[@id='cardSaleVo.toDate1']"

Obj_Tbl_MainDivSTC="xpath=.//*[@id='main']"
Obj_Btn_ContinueSellLoad="xpath=.//*[@id='confirmContinueBtnId']"
Obj_Lbl_SuccessMsgSTC="xpath=.//label[contains (@class,'Ico-green-card')]"

Obj_Lnk_FromDate2="xpath=.//*[@id='cardSaleVo.fromDate1']//following-sibling::*"
Obj_Lbl_FromDate2="xpath=.//td[contains(@class,'current-month') and text()='"
Obj_Lnk_FromDate2Next="xpath=.//*[contains (@title,'Next month')]"
Obj_Lbl_FromDate2FirstDay="xpath=.//td[contains(@class,'current-month') and text()='1']"
Obj_Txt_FromDate1="xpath=//*[@id='cardSaleVo.fromDate1']"
Obj_Div_TopBox="xpath=.//*[@id='topbluebox']"



############################################################################################################## 

######################################### Compensations   ##############################################  

Obj_Lnk_Compensations="xpath=.//a[contains (@href,'compensation')]"
Obj_Cmb_CompReason="xpath=.//*[@id='reason']"
Obj_Cmb_CompTktType="xpath=.//*[@id='ticketType']"
Obj_Cmb_PointOfSale="xpath=.//*[@id='pointOfSale']"
Obj_Txt_CompAmt="xpath=.//*[@id='compensationAmount']"
Obj_Cmb_WaytoComp="xpath=.//*[@id='type']"
Obj_Btn_CompContinue="xpath=.//*[@id='continueBtn']"
Obj_Btn_CardHistory="xpath=.//*[@id='cardNumberSearchBtn']"


######################################### Make Compensations   ##############################################  

############################################################################################################## 

Obj_Lbl_CompAmt="xpath=.//*[@id='compensatedAmount']"
Obj_Lbl_CompAmtSeason="xpath=.//*[@id='compensatedTime']"
Obj_Btn_MakeCompensation="xpath=.//*[@id='saveBtn']"
Obj_Lnk_DTPicker="xpath=.//a[contains(.,'Choose date')]"
Obj_Lnk_NextMonth="xpath=.//a[contains(@title,'Next month')]"
Obj_Lbl_SelectDate="xpath=.//*[contains (@class,'current-month week') and text()='16']"

######################################### Card History Compensations #########################################

############################################################################################################## 



Obj_Sel_SeasonCS="xpath=.//input[@type='radio']"
Obj_Btn_MakeRefund="xpath=.//input[contains (@value,'Make refund')]"


#############################################################   Chintamani Objects  ################################################# 

Obj_Txt_LoadCardFromDate ="xpath=//*[@id='cardSaleVo.fromDate']"  # Load card page 

Obj_Txt_LoadCardToDate ="xpath=//*[@id='cardSaleVo.toDate']"  # Load card page 

Obj_Lbl_CurrentSeasonGreen="xpath=.//*[@id='period1SeasonBox' and contains (@class,'green')]" # Load card page 

Obj_Lbl_UpcomingSeasonBlue="xpath=.//*[@id='period2SeasonBox' and contains (@class,'blue')]" # Load card page 

Obj_Tbl_CurrentSeason="xpath=.//*[@id='period1Box']"  # Load card page 

Obj_Tbl_UpcomingSeason="xpath=.//*[@id='period2Box']"  # Load card page 

Obj_Lbl_DisabledToValueCurrent="xpath=.//*[@id='periodPass1Value']//div" # Load card page 

Obj_Lbl_DisabledToValueUpcoming="xpath=.//*[@id='periodPass2Value']//div" # Load card page 

Obj_Lbl_SeasonAmountConvert="xpath=.//*[@id='seasonPassAmountLabel']" # Load card page 

Obj_Lnk_FromDate1="xpath=.//*[@id='cardContent.cardSaleVo.fromDate.div']/a"  # Load card page 

Obj_Div_LinkComp="xpath=.//*[@id='linkedCardBox']"   # Load card page 

Obj_Cmb_CustMuncipality="xpath=.//*[@id='personalMunicipality']"  # Load card page 

Obj_Cmb_CustGrpUpdateCard="xpath=.//select[contains (@name,'customerProfile')]"  # Load card page 

Obj_Lnk_ShowEditLoadCard="xpath=.//a[contains (.,'Show edit')]" # Load card page 

Obj_Btn_CancelConvertValue="xpath=.//*[@id='convSeasonValConfirmBtn']//preceding-sibling::input" # Load card page 

Obj_Lbl_LoadSeasonVal="//*[@id='toBeChargedPrice']" # Load card page 

Obj_Btn_RtnBlackListed="xpath=.//*[@id='confirmBtnBlacklistCard']//preceding-sibling::input"   # Load Card Page

Obj_Btn_RtnDeactivate="xpath=.//*[@id='confirmDeactiveBtn']//preceding-sibling::input"   # Load Card Page

Obj_Btn_RtnDamagedDead="xpath=.//*[@id='confirmbtn']//preceding-sibling::input"   # Load Card Page

Obj_Div_AssigntoCustPopup="xpath=.//*[@id='cardStatusVerifyPopup']/div[1]"  # Load Card Page

Obj_Div_BlacklistedPopup="xpath=.//*[@id='cardStatusBlacklistVerifyPopup']/div[1]"  # Load Card Page

Obj_Div_DeactivatePopup="xpath=.//*[@id='cardStatusDeactivateVerifyPopup']/div[1]"  # Load Card Page

Obj_Div_DamagedPopup="xpath=.//*[@id='cardStatusDamagedVerifyPopup']/div[1]"  # Load Card Page

Obj_Div_DeadPopup="xpath=.//*[@id='cardStatusDamagedVerifyPopup']/div[1]"  # Load Card Page

Obj_Div_LostFoundPopup="xpath=.//*[@id='cardStatusChangePopup']/div[1]"  # Load Card Page

Obj_Div_LostFoundVerifyPopup="xpath=.//*[@id='cardStatusLostVerifyPopup']/div[1]"  # Load Card Page

Obj_Div_ChangeCardStatus="xpath=.//*[@id='dialogContentMessageBody']/div[1]"  # Load Card Page  

Obj_Div_CardNoHeaderDamaged="xpath=.//*[@id='cardNumberHeaderDamagedVerify']"  # Load Card Page

Obj_Div_ReplaceCardPopup="xpath=.//*[@id='replacedBlacklistCardPopup']/div[1]"  # Load Card Page

Obj_Div_CardNoReplaceCardPopup="xpath=.//*[@id='cardNumberHeaderConfirm']" # Load Card Page

Obj_Div_ReplaceCardMsgContent="xpath=.//*[@id='replacedBlacklistCardPopup']/div[2]/div[2]"  # Load Card Page

Obj_Div_DamagedMsg="xpath=.//*[@id='subHeadingDamagedOrDead']"  # Load Card Page

Obj_Btn_ReplaceCard="xpath=//*[@id='replacedBlacklistCardPopup']/div[2]/div[3]/div/input[2]"  # Load Card Page

Obj_Div_ReplaceCardFunPopup="xpath=//*[@id='replaceCardPopUp']"  # Load Card Page

Obj_Btn_CloseReplaceCardPopup="xpath=.//*[@id='cnfReplaceCardBtn']//preceding-sibling::input"   # Load Card Page




######################    Chintamani Objects After 18th August 2015 ##############################################################


Obj_Lbl_DamagaedStatus="xpath=.//*[@id='statusNoteForBlacklist']" # Load Card Page
Obj_Lbl_DamagedCardStatus="xpath=.//*[@id='standardHeader']" # Load Card Page
Obj_Lbl_CardNoBDeactivate="xpath=.//*[@id='cardNumberHeaderDeactivateVerify']" # Load Card Page
Obj_Div_DeactivatePopupBig="xpath=.//*[@id='cardStatusDeactivateVerifyPopup']/div[2]"  # Load Card Page
Obj_Div_BlackListedPopupBig="xpath=.//*[@id='cardStatusBlacklistVerifyPopup']/div[2]"  # Load Card Page
Obj_Lbl_CardNoBlacklist="xpath=//*[@id='cardNumberHeaderBlacklistVerify']"  # Load Card Page
Obj_Sel_DisabledBlackListed="xpath=.//*[@id='cardStatusActiveRadio']"  # Load Card Page


Obj_Btn_CompensationClearFields="xpath=.//*[@id='clear']"              # Compensation Page
Obj_Lbl_CompensationReason="xpath=.//*[@id='compensation']/div[1]"      # Compensation Page
Obj_Lbl_CompensationTypeOfTkt="xpath=.//*[@id='compensation']/div[2]"    # Compensation Page
Obj_Lbl_CompensationWayToComp="xpath=.//*[@id='compensation']/div[4]"     # Compensation Page
Obj_Lbl_CompensationAmtTobeComp="xpath=.//*[@id='compensation']/div[5]"    # Compensation Page
Obj_Btn_ReadCardComp="xpath=//*[@id='readCard']"                            # Compensation Page    
Obj_Lbl_CompMessage="xpath=.//*[@id='compensationMessage']/div"            # Compensation Page




Obj_Cmb_CustGrpSellCardPersonal="xpath=.//*[@id='custGroupsPersonal']" # Sell Card Page
Obj_Txt_ValidUntilCGSellCardPersonal="xpath=.//*[@id='customerProfileExpiryDate']"   # Sell Card Page






######################################### Reports   ##############################################  

############################################################################################################## 

Obj_Lnk_Reports="xpath=.//a[contains (@href,'Report')]"

Obj_Cmb_RptType="xpath=.//*[@id='reportType']"

#Obj_Txt_CustRegBusinessId

Obj_Lnk_Rpt_Todate="xpath=.//*[@id='toDate']//following-sibling::a"

Obj_Lbl_ToDate_PrevMonth="xpath=.//*[@class='dp-nav-prev-month']"


#Obj_Lbl_FromDate2FirstDay


#Obj_Btn_SerialSearch

#Obj_Btn_Clear





#############################################################   Chintamani Objects End ################################################# 






############################################################### Veena Katiyar Start #########################################

######################################### Customer Register #########################################

Obj_Btn_SaveChanges = "xpath=.//*[@value='Save changes (T)']"
Obj_Txt_LastNameCompanyName="xpath=.//*[@id='name']"
Obj_Txt_FirstNameCR="xpath=//*[@id='firstName']"
Obj_THdr_SearchResult = "xpath=.//div[@class='dataTables_scrollHead']"
Obj_Chk_Person = "xpath=.//*[@id='personCheckbox']"
Obj_Chk_Company = "xpath=.//*[@id='companyCheckbox']"
Obj_Lbl_NoMatchingRecords = "xpath=.//td[contains (@class,'dataTables_empty')]"

Obj_Lbl_SearchResultInfo = "xpath=.//*[contains(@id,'earchresult_info')]"

#Obj_Txt_LastNameCR = "xpath=//*[@id='lastName']"
Obj_Txt_LastNameCR = "xpath=//*[@id='lastName']"
Obj_Lnk_CustomerNameCR="xpath=.//a[contains (text(),'"
Obj_Lnk_CustomerNameCustNoCR="xpath=//a[contains (.,text())]//..//preceding-sibling::td[2]"

Obj_Lnk_CustomerNoCR= "xpath=.//a[contains (text(),'//following-sibling::td[2]"
Obj_Lnk_CompanyType = "xpath=.//a[contains (text(),'" 
Obj_Lnk_CompanyNameCR = "xpath=.//a[contains (text(),'"
Obj_Lbl_YouAreLoggedOut="xpath=.//h1[contains(text(),'Olet kirjautunut ulos palvelusta')]"

Obj_Lnk_CompanyType1 = "xpath=.//*[@id='companySearchResult']/tbody/tr[1]/td[3] and contains (text(),'" 
Obj_Lnk_CompanyType2="xpath=.//a["

#Obj_Lbl_Allthecustomerscard0pcs = "xpath=.//*[@class='links main marB10']"

Obj_Lbl_CompanyCards="xpath=.//*[@id='allinfo']/div[2]/div/ul/li/a"
Obj_Lnk_CompanyCards="xpath=.//*[@id='allinfo']/div[2]/div/ul/li/a"
Obj_Lbl_AttachTravelCardToCustomer = "xpath=.//h1[contains(text(),'Attach travel card to customer')]"
Obj_Btn_AttachTravelCardToCustomer = "xpath=.//input[contains(@value,'Attach travel card to customer')]"
Obj_Lbl_CustomerInfo="xpath=.//h2[contains(.,'"
Obj_Txt_SearchForCardToAttach = "xpath=.//*[@id='searchCardParam']"
Obj_Btn_CardSearch="xpath=.//*[@id='seacrhCardbtn']"
Obj_Btn_CancelSearchCard="xpath=.//*[@id='cancelSeacrhCardbtn']"
Obj_Btn_AttachToCustomer="xpath=.//*[@id='attachTravelCardbtn']" 
Obj_Btn_AttachToCustomerDisabled="xpath=.//*[@id='attachTravelCardbtn' and contains(@disabled,'true')]"
Obj_Lbl_CardSearchErrorMsg="xpath=.//*[@id='cardSearchErrorDispMsg' and contains(@class,'error-message')]"
Obj_Lbl_CardSearchDisp="xpath=.//*[@id='cardSearchDisp']"
Obj_Img_CardSearched="xpath=.//*[@id='imgResp']"
Obj_Lbl_AssignedToCustomer = "xpath=.//*[@id='cardSearchDispMsg' and contains(text(),'Assigned to customer')]"
Obj_Cmb_Primary_Marketing_Channel ="xpath=.//*[@id='customerContactInfo.primaryMarketingChannel']"
Obj_Cmb_LanguageCR="xpath=.//*[@id='languagedropdown']"
Obj_Sel_CustCommunicationAllowed="xpath=.//*[@name='customerContactInfo.communicationAllowed']"
Obj_Sel_DirectMarketingAllowed="xpath=.//*[@name='customerContactInfo.directMarketingAllowed']"

Obj_Img_Print ="xpath=.//*[@class='print']/a"

Obj_Lnk_Note="xpath=.//a[@class='notePopupBtn' and contains (text(),'ote')]"
Obj_Lbl_CustomerCardInstances="xpath=.//*[@id='topbluebox']/div[1]/p/span"

Obj_Lbl_CardInfoMain = "xpath=.//*[@class='lsting']/ul[@id='blbox']/li"
Obj_Lbl_CannotRemoveCustomer="xpath=.//div[@id='removeCustomerErrorPopup']/div[@class='popup_header']/ul/li/h1"
Obj_Btn_CloseRemoveCustomerErrorMsg = "xpath=.//*[@id='closeRemoveErrorPopupMessage']"


#######  Start Sales
Obj_Lbl_NoCustomerFound="xpath=.//h1[Contains(text(),'No customer information found for Business ID')]"
Obj_Lbl_StartBySearching="xpath=.//h1[contains(text(),'Start by searching')]"

##### Shared objects
Obj_Lbl_NoTransactions = "xpath=.//*[@id='shopping']/li[2 and contains(.,'No transactions')]"
Obj_Lbl_Heading  =  "xpath=.//*[@id='blbox']"
Obj_Lbl_TextLabel = "xpath=.//label[@id='"
Obj_Lbl_CompanyID="xpath=.//*[@id='"
Obj_Lbl_CompanyName="xpath=.//*[@id='"
Obj_Lnk_AnyLink="xpath=.//a[contains(.,'"

Obj_Lbl_MiniShoppingBasket = "xpath=.//*[@id='shopping']/li[1]/h2"
Obj_Lbl_LargeShoppingBasket = "xpath=.//*[@id='blbox']/li[1]/h1"
Obj_Lbl_RemoveCustomer = "xpath=.//*[@id='removeCustomerErrorPopup']/div[2]/div[1]"

#######  Remove Customer
Obj_Lbl_CustomerDetails = "xpath=.//div[@id='removeCustomerErrorPopup']/div[@class='popup_content']/ul/li[@style='padding-left: 22px' and contains(@class,'Ico-company')]"
Obj_Lbl_CustomerDetails1="xpath=.//*[@id='removeCustomerResonConfirmPopup']/div[2]/ul/li/h2"
Obj_Lbl_ReasonDetail = "xpath=.//*[@id='removeCustomerResonConfirmPopup']/div[2]/div[1]/ul/li/div"

####  Release card from customer
Obj_Img_Office="xpath=.//div[contains (@id,'releaseTravelCardFromCustPopup')]/div[2]/div/div/ul[@id='popupbox' and contains(@class,'blueline-solid padB10')]/li[@class='title']/img"
Obj_Lbl_ReleaseCardCustomerDetails ="xpath=.//div[contains (@id,'releaseTravelCardFromCustPopup')]/div[2]/div/div/ul[@id='popupbox' and contains(@class,'blueline-solid padB10')]/li[@class='title']"
Obj_Lbl_ZeroCards="xpath=.//*[@id='allinfo']/div[2]/div/ul/li/span/div"
Obj_Lbl_ContinueTravelCardRelease="xpath=.//h1[contains(text(),'Release travel card from customer')]"
Obj_Lbl_ConfirmTravelCardRelease="xpath=.//h1[contains(text(),'Confirm release of travel card from customer')]"
Obj_Btn_ReleaseReturn="xpath=.//*[@id='returnBtn']"
Obj_Lbl_NoCardCustomer ="xpath=.//*[contains(text(),'The customer does not have any cards')]"
Obj_Btn_ReleaseClose1="xpath=.//*[@id='returnBtn']//preceding-sibling::input"
Obj_Btn_Return="xpath=.//*[@id='returnBtn']"
Obj_Img_PersonIcon="xpath=.//*[contains (@src,'person-blue')]"
Obj_Img_CardEnabledIcon="xpath=.//*[@id='cardNotOnReader_releaseCard']"
Obj_Lbl_CardInfo = "xpath=.//p[@id='spanCardDetailsConfirm']"
Obj_Lbl_Strong="xpath=.//strong[contains(.,.)]"
Obj_Lbl_ReleaseCardPopupText="xpath=.//div[contains (@id,'releaseTravelCardFromCustPopup')and contains(.,'"
Obj_Lbl_Reason="xpath=.//*[@id='selectedReason']"
Obj_Lbl_RemoveCustomerConfirmMsg = "xpath=.//div[@id='removeCustomerResonConfirmPopup']/div/ul/li/h1"
##Obj_Btn_RemoveCustomerClose1 = "xpath=.//*[@id='removeCustomerPopupCanclebtn']"
Obj_Btn_RemoveCustomerClose1 = "xpath=.//*[@id='removeCustomerConfirmPopupClosebtn']"

Obj_Btn_RemoveCustomerReturn = "xpath=.//div[@id='removeCustomerResonConfirmPopup']/div[2]/div[2]/div/input[contains (@value,'Return')]"
Obj_Lbl_CustomerRemoved = "xpath=.//*[@id='removeCustomerConfirmPopup']/div[1]/ul/li/h1"

##### New objects added after 5th June 2015 by Veena

## Remove Customer     

Obj_Img_RemoveCustomerPersonImg = "xpath=.//*[@id='removeCustomerResonConfirmPopup']/div[2]/ul/li[@class='Ico-blperson-cus']"
Obj_Lbl_RemoveCustomerPersonMsg = "xpath=.//*[@id='removeCustomerErrorPopup']/div[2]/div[1]/ul/li"
Obj_Lbl_RemoveCustomerPerson ="xpath=.//*[@id='removeCustomerErrorPopup']/div/ul/li/h1"

Obj_Btn_CloseRemoveCustomerErrorMsg1 = "xpath=.//*[@id='customerRemovedErrorClosebtn']"
Obj_Btn_RemoveCustomerClose = "xpath=.//input[@id='removeCustomerPopupCanclebtn']"


## Removed Customer #####
Obj_Img_RemovedCustomerPersonImg = "xpath=.//*[@id='removeCustomerConfirmPopup']/div[2]/ul/li[@class='Ico-blperson-cus']"
Obj_Lbl_RemovedCustomerDetails = "xpath=.//*[@id='removeCustomerConfirmPopup']/div[2]/ul/li"
Obj_Lbl_NoSearchResult="xpath=.//*[@id='info']/div[3]"
#Obj_Lbl_StartSalesCustomerNotFound="xpath=.//h1[contains(.,'No customer information found')]"
#Obj_Lbl_StartSalesCustomerNotFound="xpath=.//h1[contains(.,'not found in the customer register')]"

Obj_Lbl_StartSalesCustomerNotFound="xpath=.//h1[contains (.,'No customer information found') or contains (.,'not found in the customer register') or contains(.,'is not found')]"

## Customer Register > Search Company customer
Obj_Lbl_Companycard0pcs="xpath=.//div[@class='word-wr']"

## Attach card to company
Obj_Lbl_CompanyInfo = "xpath=.//*[@id='attachTravelCardPopup']/div[2]/ul/li/h2"

## Customer Register > Search Personal
Obj_Img_SearchResultNextPage="xpath=.//*[@id='companySearchResult_next']"
Obj_Img_SearchResultPrevPage="xpath=.//*[@id='companySearchResult_previous']"
Obj_Lnk_ResultPageNo="xpath=.//div[@id='companySearchResult_paginate']/span/a[contains(@class,'paginate')and contains(.,'"
Obj_Lbl_CustomerGroupName="xpath=.//input[@id='latestCardInfo.customerGroupName' and contains(@value,'"
Obj_Lbl_CustomerLanguage="xpath=.//div[@class='main']/div[6]"
Obj_Btn_POAClose="xpath=.//*[@id='poaCreateCloseBtn']"
Obj_Cmb_NoOfResultsInPage = "xpath=//*[@name='companySearchResult_length']"

Obj_Lbl_SelectedSortingColumn="xpath=.//*[@class='sorting_asc' and contains(.,'"
Obj_Btn_ReturnEsc="xpath=.//input[contains(@value,'Esc')]"


#####  PERSON OR BUSINESS ID colummn
Obj_Lbl_PBIDData1="xpath=.//*[@id='companySearchResult']/tbody/tr[1]/td[1]/a"
Obj_Lbl_PBIDData2="xpath=.//*[@id='companySearchResult']/tbody/tr[2]/td[1]/a"
Obj_Lbl_PBIDData3="xpath=.//*[@id='companySearchResult']/tbody/tr[3]/td[1]/a"
Obj_Lbl_PBIDData5="xpath=.//*[@id='companySearchResult']/tbody/tr[5]/td[1]/a"
Obj_Lbl_PBIDData6="xpath=.//*[@id='companySearchResult']/tbody/tr[6]/td[1]/a"
Obj_Lbl_PBIDData10="xpath=.//*[@id='companySearchResult']/tbody/tr[10]/td[1]/a"
Obj_Lbl_PBIDData15="xpath=.//*[@id='companySearchResult']/tbody/tr[15]/td[1]/a"
Obj_Lbl_PBIDData20="xpath=.//*[@id='companySearchResult']/tbody/tr[20]/td[1]/a"

#####  Name colummn
Obj_Lbl_NameData1="xpath=.//*[@id='companySearchResult']/tbody/tr[1]/td[2]/a"
Obj_Lbl_NameData2="xpath=.//*[@id='companySearchResult']/tbody/tr[2]/td[2]/a"
Obj_Lbl_NameData3="xpath=.//*[@id='companySearchResult']/tbody/tr[3]/td[2]/a"

#####  Company Type colummn
Obj_Lbl_CompanyTypeData1="xpath=.//*[@id='companySearchResult']/tbody/tr[1]/td[3]/a"
Obj_Lbl_CompanyTypeData2="xpath=.//*[@id='companySearchResult']/tbody/tr[2]/td[3]/a"
Obj_Lbl_CompanyTypeData3="xpath=.//*[@id='companySearchResult']/tbody/tr[3]/td[3]/a"


#####  Customer No. colummn
Obj_Lbl_CustomerNoData1="xpath=.//*[@id='companySearchResult']/tbody/tr[1]/td[4]/a"
Obj_Lbl_CustomerNoData2="xpath=.//*[@id='companySearchResult']/tbody/tr[2]/td[4]/a"
Obj_Lbl_CustomerNoData3="xpath=.//*[@id='companySearchResult']/tbody/tr[3]/td[4]/a"

####    Search Result Table Columns
Obj_Lbl_PersonOrBusinessIDCol ="xpath=.//thead/tr/th[1]/label/strong"
Obj_Lbl_NameCol ="xpath=.//thead/tr/th[2]/label/strong"
Obj_Lbl_CompanyTypeCol ="xpath=.//thead/tr/th[3]/label/strong"
Obj_Lbl_CustomerNoCol ="xpath=.//thead/tr/th[4]/label/strong"

##  Reports
Obj_Lnk_Reports="xpath=.//a[contains (@href,'getReportHome')]"
Obj_Cmb_ReportTypes="xpath=.//*[@id='reportType']"

####  Attach travel card to personal customer
Obj_Lbl_AttachTravelCardCustomerInfo="xpath=.//div[@id='attachTravelCardPopup']/div[2]/ul/li"
Obj_Lbl_AllTheCustomerCards1PCS="xpath=.//*[@class='links main marB10']/a"

####   Start Sales
Obj_Sel_Language1="xpath=.//*[@id='languageCode']"

####  Customer Register > Company customer
Obj_Lbl_Company0Cards="xpath=.//ul[@class='ltd ']/li/span/div"
Obj_Lnk_Company1Cards="xpath=.//ul[@class='ltd ']/li/a"

#### WholeSale

Obj_Lnk_PageTabs="xpath=.//*[@id='topbluebox']/div/ul[2]/li/a"
Obj_Btn_WholesaleSearch="xpath=.//*[@id='searchBtn']"
Obj_Btn_SearchWS = "xpath=.//*[@id='searchCustomerBtn']"

Obj_Sel_Validity_Days = "//*[@id='ticketType1']"

Obj_Lnk_NewOrder1 = ".//*[contains(@class,'tab') and contains(.,'New order')]"
Obj_Lbl_OrderNo = "xpath=.//*[@id='orderNumber']"   ### Confirm it

Obj_Lbl_BusinessIDWS1="xpath=.//*[@id='businessIdTxt']"   
Obj_Lbl_BusinessIDWS = "xpath=.//*[@id='companyYId']"  # Test4

Obj_Lbl_BusinessIDGiftVouchers ="xpath=.//*[@id='companyYId']"
Obj_Lbl_CompanyNameWS1="xpath=.//*[@id='companyNameTxt']"  
Obj_Lbl_CompanyNameWS = "xpath=.//*[@id='companyName']"
Obj_Lbl_CompanyNameGiftVouchers = "xpath=.//*[@id='companyName']"
Obj_Txt_ContactPerson1WS="xpath=.//*[@id='name1']"  
Obj_Txt_ContactPerson2WS = "xpath=.//*[@id='name2']"
Obj_Txt_ContactPerson1 = "xpath=.//*[@id='cp1Name']"   # Test4
Obj_Txt_ContactPerson2 = "xpath=.//*[@id='cp2Name']"   # Test4

Obj_Txt_ContactPerson1SSCC = "xpath=.//*[@id='name1']"
Obj_Txt_ContactPerson2SSCC = "xpath=.//*[@id='name2']"
Obj_Txt_CompanyNameSSCC = "xpath=.//*[@id='companyStrSearch']"

Obj_Txt_ContactPerson1GiftVouchers="xpath=.//*[@id='cp1Name']"
Obj_Txt_ContactPerson2GiftVouchers="xpath=.//*[@id='cp2Name']"
Obj_Btn_ContinueWS="xpath=.//input[@id='continueBtn']"
Obj_Sel_PricingMethodWS="xpath=//*[@id='pricingMethodId']"

Obj_Lnk_PrePrintedSCC="xpath=.//ul[@class='cus-src']/li/a[2]"
Obj_Lbl_StartSaleMsg="xpath=.//*[@id='saleStartInfoMessage']"  

Obj_Txt_SearchCardOrder="xpath=.//*[@id='searchStringFld']"
Obj_Btn_SearchOrder = "xpath=.//*[@id='searchOrderBtn']"
Obj_Btn_Clear = "xpath=.//*[@id='clearBtn']"
Obj_Lbl_Wholesale_SearchCol1= "xpath=.//tr[@class='resultStart']/th[1 and contains (.,'Business ID')]"
Obj_Lbl_Wholesale_SearchCol2="xpath=.//tr[@class='resultStart']/th[1 and contains (.,'Company name')]"
Obj_Lbl_Wholesale_SearchCol3="xpath=.//tr[@class='resultStart']/th[1 and contains (.,'Customer number')]"
Obj_Btn_Close_SearchWS="xpath=.//*[@id='closeCustomerSelectBtn']"
Obj_Txt_BusinessIDWS1="xpath=.//*[contains (@id,'businessId')]"   
Obj_Txt_BusinessIDWS = "xpath=.//*[@id='businessIdSearch']" 

Obj_Txt_CustomerNoWS1="xpath=//*[@id='customerIdSearch']"  
Obj_Txt_CustomerNoWS = "xpath=.//*[@id='customerNumber']"

Obj_Txt_CompanyNameWS1="xpath=.//*[@id='companyStrSearch']"  
Obj_Txt_CompanyNameWS = "xpath=.//*[@id='name']"  # Test4

Obj_Lnk_CompanySearchResultCompanyName = "xpath =.//tbody[@id='customerSelectList']/tr[1]/td[2]"
Obj_Lbl_SearchHeaderWS="xpath=//*[@id='customerSelectDialog']/div[1]/strong"
Obj_Lnk_CompanyNameSearchWS="xpath=.//a[@class='customerNumberSelection']"

Obj_Lbl_SelectCardOrder = "xpath=.//table[@class='listTable']/tbody/tr[1]/td[3]"
Obj_Lnk_FirstOrderNo="xpath=.//table[@class='listTable']/tbody/tr[1]/td[1]/a"

Obj_Lbl_FirstOrderName="xpath=.//table[@class='listTable']/tbody/tr[1]/td[2]"
Obj_Lbl_FirstOrderNo="xpath=.//table[@class='listTable']/tbody/tr[1]/td[1]"
Obj_Sel_PricingMethod = "xpath=.//*[@id='pricingMethod']"
Obj_Btn_ClearWS="xpath=.//*[@id='clearSearchBtn']"
Obj_Lbl_OrderName_OrderInformation = "xpath=.//*[@id='orderName']"

Obj_Link_GiftAndEmployerVouchers = "xpath=.//a[contains (.,'Gift vouchers and Employer vouchers')]"
Obj_Txt_CompanyNameGiftAndEmployerVouchers = "xpath=.//*[@id='name']"
Obj_Sel_GiftVoucher = "xpath=//input[@id='giftVoucherRadio']"

Obj_Sel_EmployerVoucher="xpath=//*[@id='commuterVoucherRadio']"
Obj_Txt_CustomerNoGiftAndEmployerVouchers="xpath=.//*[@id='customerNumber']"
Obj_Lbl_VoucherRangeWS1 = "xpath=.//*[@id='voucherStockResultTab']/tbody/tr[1]/td[1]"
Obj_Lbl_VoucherDateWS1 = "xpath=.//*[@id='voucherStockResultTab']/tbody/tr[1]/td[4]"

Obj_Lbl_VoucherRangeWS2 = "xpath=.//*[@id='voucherStockResultTab']/tbody/tr[2]/td[1]"
Obj_Lbl_VoucherDateWS2 = "xpath=.//*[@id='voucherStockResultTab']/tbody/tr[2]/td[4]"

Obj_Lbl_VoucherRangeWS3 = "xpath=.//*[@id='voucherStockResultTab']/tbody/tr[3]/td[1]"
Obj_Lbl_VoucherDateWS3 = "xpath=.//*[@id='voucherStockResultTab']/tbody/tr[3]/td[4]"

Obj_Lbl_VoucherRangeWS4 = "xpath=.//*[@id='voucherStockResultTab']/tbody/tr[4]/td[1]"
Obj_Lbl_VoucherDateWS4 = "xpath=.//*[@id='voucherStockResultTab']/tbody/tr[4]/td[4]"

Obj_Lbl_VoucherRangeWS5 = "xpath=.//*[@id='voucherStockResultTab']/tbody/tr[5]/td[1]"
Obj_Lbl_VoucherDateWS5 = "xpath=.//*[@id='voucherStockResultTab']/tbody/tr[5]/td[4]"

Obj_Btn_PrintWS = "xpath=.//*[@value='Print']"
Obj_Lbl_VouchersStockHeader = "xpath=.//div[@class='popup_header']/ul[@id='blbox']/li/h1"
Obj_Lbl_VouchersStockMsg= "xpath=.//*[@id='voucherStockResult']/ul/li[1]"


Obj_Lbl_VouchersStockCol1= "xpath=.//*[@id='headTable']/thead/tr/th[1]/label/strong"
Obj_Lbl_VouchersStockCol2= "xpath=.//*[@id='headTable']/thead/tr/th[2]/label/strong"
Obj_Lbl_VouchersStockCol3= "xpath=.//*[@id='headTable']/thead/tr/th[3]/label/strong"
Obj_Lbl_VouchersStockCol4= "xpath=.//*[@id='headTable']/thead/tr/th[4]/label/strong"

Obj_Img_CancelOrder = "xpath=.//a[@class='cancel']"
Obj_Lbl_DisplayVoucherNo = "xpath=.//*[@id='voucherResult']"
Obj_Lbl_VoucherNo="xpath=.//*[@id='voucherResult']/tbody/tr[1]/td[3]"

Obj_Lbl_VoucherNo1="xpath=.//*[@id='voucherResult']/tbody/tr[2]/td[3]"

Obj_Lbl_FieldErrors = "Xpath=.//*[@id='fieldErrors']/ul/li"
Obj_Lbl_StockVoucherNo = "xpath=.//*[@id='voucherStockResultTab']/tbody/tr/td[contains(@class, 'padT5')]"
Obj_Img_CancelOrderIcon = "xpath=.//a[@class='cancel' and @id = '"

#### Customer Register > Person Customer > Change card status
Obj_Btn_CloseDeadCard = "xpath=.//input[@id='returnBtn' and @value = 'Close']"
Obj_Btn_DeactivateCard="xpath=.//*[@id='returnBtn' and @class='wh-button disable marR5 float-left icoclose disableContinueOnReturn']"
Obj_Btn_ReturnDeactivateCard="xpath=.//*[@id='confirmDeactiveBtn']//preceding-sibling::input[@id='returnBtn']"
Obj_Btn_ConfirmDisabledBlacklistCard = "xpath=.//*[@id='confirmBtnBlacklistCard']"
Obj_Btn_ReturnBlacklistCard = "xpath=.//*[@id='confirmBtnBlacklistCard']//preceding-sibling::input[@id='returnBtn']"
Obj_Btn_ReplaceCard = "xpath=.//*[@value='Replace card']"

#### Customer register >Company customer > Change card status
Obj_Lbl_CardStatus = "xpath=.//*[@id='standardHeader']"
Obj_Lbl_CardStatusHdr="xpath=.//*[@id='cardStatusHeader' or @id='openCardStatusLinkId']"

##Obj_Lbl_CardStatusHdr="xpath=.//*[@id='openCardStatusLinkId']"

Obj_Lbl_CardStatusHdr1 = "xpath=.//*[@id='headingDamagedOrDead']"
Obj_Lbl_CardStatusHdr2 = "xpath=.//*[@id='blbox']/li/h1 and contains(.,'Deactivate card')"
Obj_Lbl_CardStatusHdr3 = "xpath=.//div[@id='cardStatusDeactivateVerifyPopup']/div/ul[contains(.,'Deactivate card')]"
Obj_Lbl_CardStatusHdr4 = "xpath=.//*[@id='headingReplacedDamagedOrDead' and contains(.,'The card has been put on the Blacklist')]"
Obj_Lbl_CardStatusHdr5 = "xpath=.//div[@id='cardStatusBlacklistVerifyPopup']/div/ul/li/h1[contains(.,'Put card on the Blacklist')]"
Obj_Lbl_CardStatusHdr6 = "xpath=.//div[@id='replaceCardPopUp']/div/ul/li/h1[contains(.,'Replace the card')]"
Obj_Lbl_CardStatusHdr7 = "xpath=.//div[@id='cardStatusDeactivateVerifyPopup']/div/ul[@id='blbox']/li/h1"

#### Serial singal-charge cards
Obj_Lbl_OrderName1 = "xpath=.//table[@style='width: 100%']/tbody/tr[2]/td[2][contains(.,'"
Obj_Lbl_AmountLbl = "xpath =.//table[@style='width: 100%']/tbody/tr[4]/td[2]"
Obj_Lbl_SSCCCancelConfirmationMsg ="xpath=.//div[@class='popup_content']/form[@id='serialUpdate']/div[1]"
Obj_Lbl_OrderInfo = "xpath=.//form[@id='serialUpdate3']/div/h2"
Obj_Lbl_CustomerName = "xpath=.//form[@id='serialUpdate3']/div/table/tbody/tr[1]"
Obj_Lbl_OrderName = "xpath=.//form[@id='serialUpdate3']/div/table/tbody/tr[2]"


Obj_Lbl_Amount = "xpath=.//form[@id='serialUpdate3']/div/table/tbody/tr[4]"
Obj_Lbl_OrderStatus1 = "xpath=.//*[@id='serialUpdate']/div[2]/table/tbody/tr/td[1]/table/tbody/tr[5]"
Obj_Lbl_CardText = "xpath=.//form[@id='serialUpdate3']/div/table/tbody/tr[6]"
Obj_Lbl_CardLanguage = "xpath=.//form[@id='serialUpdate3']/div/table/tbody/tr[7]"
Obj_Lbl_OrderCreated = "xpath=.//form[@id='serialUpdate3']/div/table/tbody/tr[8]"
Obj_Btn_ModifyOrderClose = "xpath=.//*[@id='closeModifyBtn']"
Obj_Lbl_ModifyOrderHdr = "xpath=.//*[@id='blbox' and contains(.,'"
Obj_Lbl_CancelOrderHdr = "xpath =.//div[@id='cancelDialog']/div[1]/ul/li/h1"
Obj_Lbl_MarkAsLossOrderHdr = "xpath=.//div[@id='lossDialog']/div[@class='popup_header']/ul/li/h1"
Obj_Lbl_MarkAsLossOrderMsg = "xpath=.//div[@id='lossDialog']/div[@class='popup_content']/form/div[1]"
Obj_Btn_CloseCancelOrder = "xpath=.//*[@id='closeCancelBtn']"
Obj_Btn_PausePrinting = "xpath=.//*[@id='pausePrintBtn']"
Obj_Btn_StartPrinting = "xpath=.//*[@id='printBtn']"
Obj_Btn_ManagePrinter = "xpath=.//*[@id='managePrinterBtn']"
Obj_Btn_MarkAsLossConfirm = "xpath=.//*[@id='confirmLossBtn']"
Obj_Btn_MarkAsLossCancel = "xpath=.//*[@id='closeLossBtn']"

#### Order > New Order
Obj_Lbl_NewOrderCustomerNo = "xpath=.//*[@id='customerNumberTxt']"
Obj_Link_CompanyCustomerName= "xpath=.//tbody[@id='customerSelectList']/tr[1]/td[2]/a"
Obj_Lbl_PricePerCard = "xpath=.//*[@id='pricePerCardTxt']"
Obj_Lbl_TotalPrice = "xpath=.//*[@id='priceTotalTxt']"
Obj_Txt_SpecialEventToDate = "xpath=.//*[@id='to']"
Obj_Txt_SpecialEventFromDate = "xpath=.//*[@id='from']"
Obj_Txt_CardText1 = "xpath=.//*[@id='cardText2']"


#### Order > Manage Order
Obj_Lbl_SearchResultInfo = "xpath=.//*[@id='companySearchResult_info']"
Obj_Lbl_SearchResultInfo1 = "xpath=.//*[@id='searchresult_info']"
#Obj_Lbl_NoMatchingRecordsFound = "xpath=.//table[@id='searchresult']/tbody/tr/td[contains(.,'No matching records found')]"
Obj_Lbl_NoMatchingRecordsFound = "xpath=.//div[@id='info']"
Obj_Sel_BusinessID = "xpath=.//*[@id='searchType2']"
Obj_Lbl_SearchResultName1 = "xpath=.//*[@id='searchresult']/tbody/tr[1]/td[3]"
Obj_Lbl_SearchResultName2 = "xpath=.//*[@id='searchresult']/tbody/tr[2]/td[3]"

######################################### Transfolio Card Manager   ##############################################             

Obj_Lnk_BlacklistTab = "xpath=.//span[contains( @title,'Black list')]"
Obj_Lnk_AddtoBlacklist = "xpath=.//a[contains (@class,'toolIcon blacklist')]"  
Obj_Cmb_CardBlackListReason = "xpath=.//select[@name='blacklistSelect']"

Obj_Btn_AddReason = "xpath=.//input[@value='Add']"


############################################################################################################## 

#### Added after 18/8/2015




### Veena Katiyar
Obj_Lnk_ShowEdit="xpath=.//*[contains (@href,'Detail')]"
Obj_Lbl_NotesText = "xpath=.//*[@class='noteWrap']"
Obj_Lbl_TotalToBeCharged = "Xpath=.//*[@id='toBeChargedPrice']"
Obj_Lbl_OrderInfoAmount = "xpath=.//*[@id='amountTxt']"
Obj_Lbl_OrderInfoValue = "xpath=.//*[@id='value']"


#### Serial singal-charge cards
Obj_Lbl_OrderNoSSCC = "xpath=.//*[@id='serialUpdate3']/div/table/tbody/tr[3]"

### Shopping basket
Obj_Lbl_SingleChargeCardSale = "xpath=.//div[contains(@id,'shopBasketTB') and contains(.,'Single charge card order sale')]"
Obj_Img_DeleteSingalChargeCardFromSB = "xpath=.//*[contains(@id,'other')]"
Obj_Btn_SSCCNewOrderSearch = "xpath=//*[@id='searchCustomerBtn']"
Obj_Txt_SearchBusinessID="xpath=.//*[@id='searchWithYID']"

### Start Sales > Find Person > Goto Cards page > Deactivate card
Obj_Img_CardIconDeactivate = "xpath=.//*[@id='cardOnReader_deactivate']"
Obj_Lbl_CardNoDeactivate = "xpath=.//*[@id='cardNumberHeaderDeactivateVerify']"
Obj_Lbl_AdditionalInfoDeactivateCard = "xpath=.//*[@id='cardStatusDeactivateVerifyPopup']/div[2]/div[3]/ul/li[1]/div[1]"

Obj_Lbl_AnyLabel = "xpath=.//*[contains(.,'"
Obj_Lbl_CharsEntered = "xpath=.//span[@id='charsEntered']"
Obj_Lbl_CharsEnteredBlacklistCard = "xpath=//*[@id='characters']"
Obj_Lbl_InvalidCharsErrMsg = "xpath=.//*[@id='error_deac_msg']"

### Start Sales > Find Person > Goto Cards page > Blacklist card
Obj_Img_CardEnabledIconBlackList = "xpath=.//*[@id='cardOnReader_blacklist_confirm_popup']"
Obj_Lbl_BlackListReasonShown = "xpath=.//*[@id='reasonConfirm']"
Obj_Lbl_DoYouWishReplaceCard = "xpath=.//*[@id='replacedBlacklistCardPopup']/div[2]/div[2]/div[3]/p"
Obj_Lbl_AdditionalInfoBlacklistCard = "xpath=.//*[@id='additionalDetailsConfirm']"


Obj_Lbl_CardNoPutCardOnBlacklist = "xpath=.//*[@id='cardNumberHeaderBlacklistVerify']"
Obj_Img_CardGreenPutCardOnBlacklist = "xpath=.//*[@id='cardOnReader_blacklist_popup']"
Obj_Lbl_BlackListDate = "xpath=.//*[@id='person']/div[2]/div[1]/div[2]/p[1]"

#####  added after 23/9/2014
Obj_Lbl_BlacklistedCardHdr = "xpath =.//*[@id='cardStatusPopUpHeaderId']"

### WholeSale
Obj_Txt_NoOfVouchers = "xpath=.//*[@id='numberOfVouchers']"

###Customer Register
Obj_Btn_ConfirmCustomerRemovalClose = "xpath=.//*[@id='removeCustomerConfirmPopupCanclebtn']//preceding-sibling::*[@id='removeCustomerPopupCanclebtn']"

### Compensations


Obj_Txt_SearchCardNo = "xpath=.//*[@id='cardNumberSearch']"
Obj_Lbl_CardHistoryComp = "xpath=.//*[@id='blboxFlr']/li/span"
Obj_Btn_ClearFieldsComp = "xpath=.//*[@id='clear']"
Obj_Lbl_CompensationReasonCompDetails = "xpath=.//*[@id='compensation']/div[1]/span"
Obj_Lbl_TypeOfTicketToBeCompensatedCompDetails = "xpath=.//*[@id='compensation']/div[2]/span[1]/span"
Obj_Lbl_WayToCompensateCompDetails = "xpath=.//*[@id='compensation']/div[4]/span"
Obj_Btn_ReadCardComp = "xpath=.//*[@id='readCard']"
Obj_Lbl_RefundAsValue = "xpath=.//*[@id='listingtable']/table/tbody/tr[2]"
Obj_Lbl_RefundAsValue1 = "xpath=.//*[@id='listingtable']/table/tbody/tr[3]"
Obj_Lbl_RefundAsValue2 = "xpath=.//*[@id='listingtable']/table/tbody/tr[4]"

Obj_Lbl_RefundAsValueLargeSB = "xpath=.//*[@id='listingtable']/table/tbody/tr[3]"

Obj_Lbl_OtherValueRefundSB = "xpath=.//div[@id='shoppingBasketTbl_247330']/div/div[2]/table/tbody/tr[1]"
#Obj_Lbl_OtherValueRefund = "xpath=.//*[contains(@id,'shoppingBasketTbl')][2]/div/table/tbody/tr[1]"
Obj_Lbl_OtherValueRefund = "xpath=.//*[contains(@id,'shoppingBasketTbl')][2]"

#Obj_Lbl_OtherValueRefund1 = "xpath=.//*[contains(@id,'shoppingBasketTbl')][2]/div/table/tbody/tr[2]"
Obj_Lbl_OtherValueRefund1 = "xpath=.//*[contains(@id,'shoppingBasketTbl')][2]"

#Obj_Lbl_OtherValueRefund2 = "xpath=.//*[contains(@id,'shoppingBasketTbl')][2]/div/table/tbody/tr[3]"
Obj_Lbl_OtherValueRefund2 = "xpath=.//*[contains(@id,'shoppingBasketTbl')][2]"

Obj_Lbl_PointOfSaleValue = "xpath=.//*[@id='compensation']/div[2]/span[2]/span"

Obj_Lbl_ShoppingBasketTable = "xpath=.//*[@id='shoppingBasketTable']"


#### Start Sales
Obj_Lbl_ValueOnCard = "xpath=.//*[@id='valueAmountOnCard']"
Obj_Btn_CreateID = "xpath=.//*[@value='Create ID']"

#### Main Page UI
Obj_Img_HSLMS = "xpath=.//*[@id='header']/ul[1]/li[1]/img"
Obj_Lbl_ServicePointMS="xpath=.//*[@id='header']/ul[1]/li[2 and contains(.,'Service Point')]"
Obj_Lbl_CompensationsMS = "xpath=.//*[@id='headerBullet'and contains(.,'Compensations')]"
Obj_Img_EnabledCardImgMS = "xpath=.//*[@id='cardEnabledIcon']"
Obj_Lbl_CardNoMS = "xpath=.//*[@id='cardNumberHeader']"
Obj_Lbl_TodayDate = "xpath = .//*[@id='header']/ul[2]/li[1]"
Obj_Lnk_FinnishLanguage = "xpath=.//*[@id='languageChange']/a[2]"

#### Service Point
Obj_Btn_CloseServicePoint = "xpath=.//input[@value='Close']"

### PRC objects
Obj_Lnk_CheckMunicipality = "xpath=.//*[@id='checkMunicipalityLinkId']"
Obj_Lbl_CheckMuncipalityDisabled = "xpath=.//*[@id='checkMunicipalityLinkId' and @class = 'disabled']"
Obj_Lbl_ChangeHMErrorMsg = "xpath=.//*[@id='checkMunicipalityPopup']/div[2]/div/ul"
Obj_Lbl_ChangeHMErrorMsg1 = "xpath=.//*[@id='checkMunicipalityDeterminationConfirmPopup']/div[2]/div[1]/ul"
Obj_Btn_ConfirmPRC = "xpath=.//*[@id='confirmbtnCheckMunicipality']"
Obj_Hdr_ChangeInformation = "xpath=.//*[@id='checkMunicipalityPopup']/div/ul/li/h1"
Obj_Hdr_ChangeInformation1 = "xpath=.//*[@id='checkMunicipalityNotChangedPopup']/div/ul/li/h1"
Obj_Hdr_ChangeInformation2 = "xpath=.//*[@id='checkMunicipalitySameDiedPopup']/div/ul/li/h1"
Obj_Hdr_ChangeInformation3 = "xpath=.//*[@id='checkMunicipalityDeterminationConfirmPopup']/div/ul/li/h1"

Obj_Hdr_PersonIDNotFoundPRC = "xpath=.//*[@id='checkMunicipalityPersonNotFound']/div/ul/li/h1"
Obj_Hdr_PersonDeactivatedPRC = "xpath=.//*[@id='checkMunicipalityPersonDeactivatedPopup']/div[1]/ul/li/h1"
Obj_Lbl_OldMunicipality = "xpath=.//*[@id='oldMunicipalitySpanId']"
Obj_Lbl_NewMunicipality = "xpath=.//*[@id='newMunicipalitySpanId']"
Obj_Btn_CancelPRC = "xpath=.//*[@id='canclebtn']"
Obj_Lbl_Checked = "xpath=.//*[@id='sameMunicipalitySpanId']"
# Obj_Lbl_SameHMErrorMsg = "xpath=.//*[@id='checkMunicipalityNotChangedPopup']/div/ul/li/h1"
Obj_Lbl_SameHMErrorMsg = "xpath=//*[@id='checkMunicipalityNotChangedPopup']/div[2]/div[1]/ul/li"
Obj_Btn_Close_PRC = "xpath=.//*[@id='closebtnCheckMunicipalitySame']"
Obj_Btn_Close_PRC1 = "xpath=.//*[@id='checkMunicipalitySameDiedPopup']/div[2]/div[2]/div/input[@id='closebtn']"
Obj_Btn_Close_PRC2 = "xpath=.//*[@id='checkMunicipalityPersonNotFound']/div[2]/div[2]/div/input[@value='Close']"
Obj_Btn_Close_PRC3 = "xpath=.//*[@id='checkMunicipalityPersonDeactivatedPopup']/div[2]/div[2]/div/input[@value='Close']"
Obj_Btn_Close_PRC4 = "xpath=.//*[@id='checkMunicipalityDeterminationConfirmPopup']/div[2]/div[2]/div/input[@value='Close']"
Obj_Lbl_DeadCardHolderErrorMsg = "xpath=.//*[@id='checkMunicipalitySameDiedPopup']/div[2]/div/ul/li[1]"
Obj_Lbl_PersonDeactivatedErrorMsg = "xpath=.//*[@id='checkMunicipalityPersonDeactivatedPopup']/div[2]/div[1]/ul/li[1]"
Obj_Lbl_PersonIDNotFoundPRC ="xpath=.//*[@id='checkMunicipalityPersonNotFound']/div[2]/div[1]/ul/li[1]"
Obj_Lbl_DateOfDeath = "xpath=.//*[@id='personDeceasedDateSpanId']"

####  Added after 1/1/2016

Obj_Lbl_Allthecustomerscard0pcs = "xpath=.//*[contains(.,'cards (0 pcs)')]"
###Obj_Lbl_Allthecustomerscard0pcs = "xpath=.//div[@class='form-body']/div/div[contains(.,'cards (0 pcs)')]"

Obj_Lbl_CardStatusCMM = "xpath=.//*[@id='cardsGridId']/tbody[1]/tr/td[4]/div"
Obj_Sel_PricingMethod_Disabled = "xpath=.//*[@id='pricingMethod' and @disabled = 'disabled']"
Obj_Img_Cancel_SSCC_OrderSale = "xpath=.//*[@class='can-dis cancel']"

#### Added after 25/2/2016
####  Serial travel card
Obj_Cmb_STC_ProductInfo1 = "xpath=.//*[@id='cardSaleVo.ticketCode']"
Obj_Cmb_STC_ProductInfo2 ="xpath=.//*[@id='cardSaleVo.ticketCode1']"


Obj_Cmb_STC_ValidityArea2 = "xpath=.//*[@id='cardSaleVo.validityArea1']"
Obj_Lbl_CustInfo_CustGrp = "xpath=.//*[@id='customerGroupId']"
Obj_Lbl_CustInfo_HomeMunicipality = "xpath=.//*[@id='homemuncipalityId']"
Obj_Txt_NextToDate = "xpath=.//*[@id='cardSaleVo.toDate1']"
Obj_Lbl_LoadingCardInfo = "xpath=.//*[@id='loadingAfterSoldCardDivId']"
Obj_Lbl_LoadingCardInfo1 = "xpath=.//*[@id='loadMessageTrId']"
Obj_Lbl_LoadingCardInfo2 = "xpath=.//*[@id='loadingAfterSoldCardDivId']/ul[1]/li[2]"
Obj_Txt_SBDetails = "xpath=.//*[@id='listingtable']/table/tbody"
Obj_Txt_SBDetails1 = "xpath=.//*[@id='listingtable']/table/tbody/tr[2]"
Obj_Txt_SBDetails2 = "xpath=.//*[@id='listingtable']/table/tbody/tr[3]"
Obj_Txt_SBDetails3 = "xpath=.//*[@id='listingtable']/table/tbody/tr[4]"
Obj_Txt_NoOfDays1="xpath=//*[@id='cardSaleVo.days1']"

Obj_Lbl_CustomerType = "xpath=.//*[@id='type']"
Obj_Lbl_STC_ProdInfoValue = "xpath=.//*[@id='loadValueAmt']"

Obj_Cmb_STC_New_CustGrp = "xpath=.//*[@id='customerGroup']"
Obj_Lbl_STC_SalesAndLoading = "xpath=.//div[@id='topbluebox']/div/ul[@id='blbox']/li/h1"
Obj_Lbl_CardSaleTotalPrice = "xpath=.//*[contains(@id,'totalPriceWithTaxes')]"
Obj_Lbl_CardSaleVatPrice = "xpath=.//*[contains(@id,'totalPriceWithVatWithTaxes')]"
Obj_Btn_StartOver = "xpath=.//*[@value='Start over']"
Obj_Lbl_BusinessIDnotFound = "xpath=.//*[@id='cardLinkToCustomerPopup']/div[1]/h1[contains(.,'Business ID not found')]"
Obj_Lbl_BusinessIDnotFoundMsg = "xpath=.//*[@id='popup_content' and contains(.,'Business ID not found. Please enter a new Business ID. If the company is not yet in the customer register, go to Start Sales and create the new customer before linking the card.')]"
Obj_Chk_ToBeInvoiced = "xpath=.//*[@id='toBeInvoiced']"
Obj_LBL_SB_TotalPriceWithTax = "xpath=.//*[contains(@id,'totalPriceWithTaxes')]"
Obj_LBL_SB_TotalPriceWithVATWithTax = "xpath=.//*[contains(@id,'totalPriceWithVatWithTaxes')]"
Obj_Lbl_NoCustomerInfo = "xpath=.//*[@id='blbox']/li/h1[contains(.,'No customer info')]"

#######  Transfolio Transaction Manager   ####################

Obj_Tbl_Transactions_TM = "xpath=.//table[@id='transactions']"

Obj_Txt_SearchText_TM = "xpath=.//html/body/div[4]/section/div[3]/div[4]/form/input"
Obj_Lnk_ShowTransaction_TM = "xpath=.//*[@id='transactions']/tbody[1]/tr[1]/td[6]/div/a[1]"
Obj_Lnk_ShowTransaction1_TM = "xpath=.//*[@id='transactions']/tbody[1]/tr[2]/td[6]/div/a[1]"

Obj_Lbl_DistributionType_TM = "xpath=.//*[@class='simpleNode' and contains(.,'Distribution Type')]"
Obj_Lbl_TransacionType_TM = "xpath=.//*[@class='simpleNode' and contains(.,'Transaction Type')]"
Obj_Lbl_PointOfSaleIDSold_TM = "xpath=.//*[@class='simpleNode' and contains(.,'Point Of Sale Identifier Sold')]"
Obj_Lbl_DistributionEvent_TM = "xpath =.//*[@class='simpleNode' and contains(.,'Distribution Event')]"
Obj_Lbl_ACLPRocessingResult_TM = "xpath=.//*[@class='simpleNode' and contains(.,'Action List Processing Result')]"

Obj_Lbl_OperatorIDSold_TM = "xpath = .//*[@class='simpleNode' and contains(.,'Identifier Sold')]"
Obj_Lbl_GroupSize_TM = "xpath= .//*[@class='simpleNode' and contains(.,'Group Size')]"
Obj_Lbl_ProductCode_TM = "xpath=.//*[@class='simpleNode' and contains(.,'Product Code')]"
Obj_Lbl_Status_TM = "xpath=.//*[@class='simpleNode' and contains(.,'Status')]"
Obj_Lbl_TrafficDay_TM = "xpath=.//*[@class='simpleNode' and contains(.,'Traffic Day')]"
Obj_Lbl_PaidAmount_TM = "xpath =.//*[@class='simpleNode' and contains(.,'Paid Amount')]"
Obj_Lbl_Blacklist_Addition_Reason_TM = "xpath =.//*[@class='simpleNode' and contains(.,'Blacklist Addition Reason')]"
Obj_Lbl_Dispose_Reason_TM = "xpath =.//*[@class='simpleNode' and contains(.,'Dispose Reason')]"

Obj_Lbl_AgentID_TM = "xpath=.//*[@class='simpleNode' and contains(.,'Agent Identifier')]"
Obj_Lbl_OperatorID_TM = "xpath=.//*[@class='simpleNode' and contains(.,'Operator Identifier')]"
Obj_Lbl_TicketType_TM = "xpath=.//*[@class='simpleNode' and contains(.,'Ticket Type')]"
Obj_Lbl_SaleSpecialEvent_TM = "xpath=.//*[@class='simpleNode' and contains(.,'Sale Special Events')]"

Obj_Lbl_PriceReason_TM = "xpath=.//*[@class='nodeElement' and contains(.,'Price Reason')]"
Obj_Lbl_VatPercent_TM = "xpath = .//*[@class='nodeElement' and contains(.,'Vat Percentage')]"
Obj_Lbl_VatValue_TM = "xpath = .//*[@class='nodeElement' and contains(.,'Vat Value')]"
Obj_Lbl_PricingMethod_TM = "xpath=.//*[@class='nodeElement' and contains(.,'Pricing Method')]"
Obj_Lbl_PriceOfPeriod_TM = "xpath=.//*[@class='nodeElement' and contains(.,'Price Of Period')]"

Obj_Lbl_StartCashBalance_TM = "xpath=.//*[@class='nodeElement' and contains(.,'Start Cash Balance')]"
Obj_Lbl_EndCashBalance_TM = "xpath=.//*[@class='nodeElement' and contains(.,'End Cash Balance')]"
Obj_Lbl_POSID_TM = "xpath=.//*[@class='nodeElement' and contains(.,'Point Of Sale Identifier')]"


Obj_Lbl_ValidityAreaType_TM = "xpath=.//*[@class='nodeElement' and contains(.,'Validity Area Type')]"
Obj_Lbl_ValidityArea_TM = "xpath=.//*[@class='nodeElement' and contains(.,'Validity Area Type')]//following-sibling::*[contains(.,'Validity Area')]"

Obj_Lbl_PeriodStartDate_TM = "xpath=.//*[@class='nodeElement' and contains(.,'Period Start Date')]"
Obj_Lbl_PeriodEndDate_TM = "xpath=.//*[@class='nodeElement' and contains(.,'Period End Date')]"


Obj_Lbl_TotalAmount_TM = "xpath=.//*[@class='nodeElement' and contains(.,'Total Amount')]"
Obj_Lbl_TotalPrice_TM = "xpath=.//*[@class='nodeElement' and contains(.,'Total Price')]"
Obj_Lbl_PaymentMeanType_TM = "xpath=.//*[@class='nodeElement' and contains(.,'Payment Mean Type')]"
Obj_Lbl_OriginOfSale_TM = "xpath=.//*[@class='nodeElement' and contains(.,'Origin Of Sale')]"

Obj_Lbl_TransactionTime_TM = "xpath=.//*[@id='transactions']/tbody[1]/tr[1]/td[1]"
Obj_Lnk_ValidTransactionsList = "xpath=.//*[@class='ng-binding' and contains(.,'List Of Valid Transactions')]"

Obj_Lbl_RefundReason_TM = "xpath=.//*[@class='nodeElement' and contains(.,'Refund Reason')]"
Obj_Lbl_ValueCounter_TM = "xpath=.//*[@class='nodeElement' and contains(.,'Value Counter')]"
Obj_Lbl_LoadedValue_TM = "xpath=.//*[@class='nodeElement' and contains(.,'Loaded Value')]"



#######  Transfolio Transaction Manager   ####################

#######  Corrections

Obj_Lnk_Corrections="xpath=.//*[@title='Corrections']"
Obj_Tab_Corrections = "xpath=.//*[@id='topbluebox']/div/ul/li/a[contains(.,'Sum corrections')]"
Obj_Cmb_ProviderType = "xpath=.//*[@id='serviceProviderTypeOptions']"
Obj_Cmb_Provider = "xpath=.//*[@id='servicePorviderOptions']"
Obj_Cmb_POS = "xpath=.//*[@id='pointOfSaleOptions']"
Obj_Cmb_TicketType = "xpath=.//*[@id='correctionTicketTypeOptions']"
Obj_Cmb_Effect = "xpath=.//*[@id='effectOptions']"

Obj_Cmb_CustomerGroup = "xpath=.//*[@id='sccCustomerGroupOptions']"
Obj_Cmb_CustomerGroup1 = "xpath=.//*[@id='seasonTicketCustomerGroupOptions']"
Obj_Cmb_ProductInformation = "xpath=.//*[@id='sccProdInfoOptions']"
Obj_Cmb_ProductInformation1 = "xpath=.//*[@id='seasonTicketProdInfoOptions']"
Obj_Cmb_Zone = "xpath=.//*[@id='sccZoneOptions']"
Obj_Cmb_Zone1 = "xpath=.//*[@id='seasonTicketZoneOptions']"

Obj_Txt_DaysOrHours = "xpath=.//*[@id='sccDaysOrHours']"
Obj_Txt_DaysOrHours1 = "xpath=.//*[@id='sccDaysOrHours']"

Obj_Txt_Pieces = "xpath=.//*[@id='sccPieces']"
Obj_Txt_Pieces1 = "xpath=.//*[@id='travelCardPieces']"
Obj_Txt_Pieces2 = "xpath=.//*[@id='voucherPieces']"
Obj_Txt_Pieces3 = "xpath=.//*[@id='singleValueTicketPieces']"


Obj_Txt_UnitPrice = "xpath=.//*[@id='sccUnitPrice']"
Obj_Txt_UnitPrice1 = "xpath=.//*[@id='travelCardUnitPrice']"
Obj_Txt_UnitPrice2 = "xpath=.//*[@id='voucherUnitPrice']"
Obj_Txt_UnitPrice3 = "xpath=.//*[@id='singleValueTicketUnitPrice']"

Obj_Txt_AmountToBeCorrected = "xpath=.//*[@id='sccAmountToBeCompensated']"
Obj_Txt_AmountToBeCorrected1 = "xpath=.//*[@id='travelCardAmountToBeCompensated']"
Obj_Txt_AmountToBeCorrected2 = "xpath=.//*[@id='voucherAmountToBeCompensated']"
Obj_Txt_AmountToBeCorrected3 = "xpath=.//*[@id='paymentByStoredValueAmountToBeCompensated']"
Obj_Txt_AmountToBeCorrected4 = "xpath=.//*[@id='valueAmountToBeCompensated']"
Obj_Txt_AmountToBeCorrected5 = "xpath=.//*[@id='singleValueTicketAmountToBeCompensated']"
Obj_Txt_AmountToBeCorrected6 = "xpath=.//*[@id='seasonTicketAmountToBeCompensated']"

Obj_Txt_VATPercentage = "xpath=.//*[@id='sccVatPercentage']"
Obj_Txt_VATPercentage1 = "xpath=.//*[@id='travelCardVatPercentage']"
Obj_Txt_VATPercentage2 = "xpath=.//*[@id='voucherVatPercentage']"
Obj_Txt_VATPercentage3 = "xpath=.//*[@id='paymentByStoredValueVatPercentage']"
Obj_Txt_VATPercentage4 = "xpath=.//*[@id='valueVatPercentage']"
Obj_Txt_VATPercentage5 = "xpath=.//*[@id='singleValueTicketVatPercentage']"
Obj_Txt_VATPercentage6 = "xpath=.//*[@id='seasonTicketVatPercentage']"


Obj_Cmb_PricingMethod = "xpath=.//*[@id='sccPricingMethodCode']"
Obj_Cmb_PricingMethod1 = "xpath=.//*[@id='travelCardPricingMethodCode']"
Obj_Cmb_PricingMethod2 = "xpath=.//*[@id='valuePricingMethodCode']"
Obj_Cmb_PricingMethod3 = "xpath=.//*[@id='seasonTicketPricingMethodCode']"

Obj_Cmb_PaymntMethod = "xpath=.//*[@id='sccPaymentMethodCode']"
Obj_Cmb_PaymntMethod1 = "xpath=.//*[@id='travelCardPaymentMethodCode']"
Obj_Cmb_PaymntMethod2 = "xpath=.//*[@id='voucherPaymentmethodCode']"
Obj_Cmb_PaymntMethod3 = "xpath=.//*[@id='valuePaymentMethodCode']"
Obj_Cmb_PaymntMethod4 = "xpath=.//*[@id='singleValueTicketPaymentMethodCode']"
Obj_Cmb_PaymntMethod5 = "xpath=.//*[@id='seasonTicketPaymentMethodCode']"

Obj_Btn_ClearFields = "xpath=.//*[@id='correctionClear']"
Obj_Btn_CorrectionContinue = "xpath=.//*[@id='correctionContinue']"
Obj_Btn_MakeCorrection = "xpath=.//*[@id='saveBtn']"

Obj_Lbl_ServiceProvider_SalesPoint = "xpath=.//*[@id='corrections']/div[1]"
Obj_Lbl_CorrectionEffect = "xpath=.//*[@id='corrections']/div[2]"
Obj_Lbl_TicketType = "xpath=.//*[@id='corrections']/div[3]"
Obj_Lbl_CustomerGroup = "xpath=.//*[@id='corrections']/div[4]"
Obj_Lbl_ProductInfo = "xpath=.//*[@id='corrections']/div[5]"
Obj_Lbl_Zone = "xpath=.//*[@id='corrections']/div[6]"
Obj_Lbl_DaysOrHours = "xpath=.//*[@id='corrections']/div[7]"
Obj_Lbl_Pieces = "xpath=.//*[@id='corrections']/div[8]"
Obj_Lbl_Pieces1 = "xpath=.//*[@id='corrections']/div[4]"

Obj_Lbl_UnitPrice = "xpath=.//*[@id='corrections']/div[9]"
Obj_Lbl_UnitPrice1 = "xpath=.//*[@id='corrections']/div[5]"
Obj_Lbl_CorrectionAmount = "xpath=.//*[@id='corrections']/div[10]"
Obj_Lbl_CorrectionAmount1 = "xpath=.//*[@id='corrections']/div[6]"
Obj_Lbl_CorrectionAmount2 = "xpath=.//*[@id='corrections']/div[4]"

Obj_Lbl_Vat = "xpath=.//*[@id='corrections']/div[11]"
Obj_Lbl_Vat1 = "xpath=.//*[@id='corrections']/div[7]"
Obj_Lbl_Vat2 = "xpath=.//*[@id='corrections']/div[5]"

Obj_Lbl_PricingMethod = "xpath=.//*[@id='corrections']/div[12]"
Obj_Lbl_PricingMethod1 = "xpath=.//*[@id='corrections']/div[8]"
Obj_Lbl_PricingMethod2 = "xpath=.//*[@id='corrections']/div[6]"

Obj_Lbl_PaymentMethod = "xpath=.//*[@id='corrections']/div[13]"
Obj_Lbl_PaymentMethod1 = "xpath=.//*[@id='corrections']/div[9]"
Obj_Lbl_PaymentMethod2 = "xpath=.//*[@id='corrections']/div[8]"
Obj_Lbl_PaymentMethod3 = "xpath=.//*[@id='corrections']/div[7]"

Obj_Btn_CorrectionReturn = "xpath=.//*[@id='correctionConfirmReturnBtn']"

Obj_Cmb_Muncipality = "xpath=.//*[@id='seasonTicketMunicipalityCode']"

Obj_Lnk_SeasonTicketFromDate = "xpath=.//a[@class='input-date'][1]"
Obj_Lnk_SeasonTicketToDate = "xpath=.//a[@class='input-date'][2]"

Obj_Lbl_SeasonFromDate = "xpath=.//*[@class='current-month weekday' and contains(.,'13')]"
Obj_Lbl_SeasonToDate = "xpath=.//*[@class='current-month weekday' and contains(.,'20')]"


#############  Role-Based  ######################

Obj_Lnk_SPM_App = "xpath=.//a[contains(.,'SPM')]"
Obj_Lnk_PRC_App = "xpath=.//a[contains(.,'PRC')]"
Obj_Lnk_SalesPoint_App = "xpath=.//a[contains(.,'Salespoint')]"
Obj_Lnk_Main_InEnglish = "xpath=.//*[@id='btn-en']"
Obj_Lbl_Message = "xpath=.//*[@id='allinfo']"
Obj_Lbl_PRC_Hdr = "xpath=.//*[@id='blbox' and contains(.,'PRC Batch Jobs')]"
Obj_Lbl_SPM_Hdr = "xpath=.//*[@id='blbox' and contains(.,'Search')]"



#############  PRC  ######################

Obj_Cmb_BatchType = "xpath=.//*[@id='batchType']"
Obj_Cmb_JobStatus = "xpath=.//*[@id='status']"
Obj_Lnk_PRCFromDate = "xpath=.//*[@id='blbox']/a[@class='input-date'][1]"
Obj_Lnk_PRCToDate = "xpath=.//*[@id='blbox']/a[@class='input-date'][2]"
Obj_Tbl_PRCDataTable = "xpath=.//*[@id='prcDataTable']"
Obj_Btn_SearchPRC = "xpath=.//*[@id='blbox']/input[@value='Search']"

Obj_Lnk_NextPRC = "xpath=.//*[@id='prcDataTable_next']"
Obj_Lnk_PrevPRC = "xpath=.//*[@id='prcDataTable_previous']"


#############  Card Status  ######################

Obj_Lbl_ChangeCardStatusOptions ="xpath=.//div[@class='ch-status']"
Obj_Lnk_AllTheCustomersCards = "xpath=.//a[contains(.,'All the customer')]"
Obj_Lnk_DeadCard = "xpath=.//a[(contains(.,'Dead card'))]"
Obj_Lnk_Close_BlacklistedCard = "xpath=.//div[@id='cardStatusChangePopup']/div[2]/div/div[5]/input[@id='returnBtn']"


#############  Card History  ######################

Obj_Img_Organization = "xpath=.//*[@id='blbox']/li/img"
Obj_Sel_LoadingValue = "xpath=.//*[@id='loadingValue']"


#############  Card History  ######################

Obj_Lbl_Customer_ID = "xpath=.//div[@class='bluebar']/ul[@id='blbox']/li[@class='Ico-profile']"
Obj_Lbl_SeasonPrice = "xpath=.//*[@id='priceCalc']"

Obj_Lnk_Note1="xpath=.//a[@class='notePopupBtn' and contains (text(),'ote')]"

Obj_Btn_LinkCardPC1="xpath=.//*[@id='linkPersonOrCompany']"

Obj_Lbl_oneTimeQuery = "xpath=.//*[@id='prcDataTable' and contains(.,'One-time query') or contains(.,'No data available in table')]"
Obj_Lbl_WeeklyUpdate = "xpath=.//*[@id='prcDataTable' and contains(.,'Weekly update') or contains(.,'No data available in table')]"
Obj_Lbl_Running = "xpath=.//*[@id='prcDataTable' and contains(.,'Running') or contains(.,'No data available in table')]"
Obj_Tbl_CardHistory1 = "xpath=.//*[@id='eventTransactionsTabId']/tbody/tr"


#############  Reports  ######################

Obj_Btn_SearchReports = "xpath=.//*[@id='searchBtn']"
Obj_Txt_BusinessIDReports = "xpath=.//*[@id='businessId']"

#############  WholeSale  ######################


#############  SSCC  ######################
Obj_Sel_CustomerGroup = "xpath=.//*[@id='customerGroup' and @value='01']"


#############  Customer Register  ######################
Obj_Lnk_CardNo_Cust_Reg = "xpath=.//*[@id='blbox']/li/a"
Obj_Btn_Return1 = "xpath=.//*[@id='returnBtnTravelCard']"
Obj_Lnk_1_Card = "xpath=.//a[contains(.,'1 pcs')]"

#############  Compensations  ######################

Obj_Lbl_CompDetails = "xpath=.//*[@id='compensation']"
###Obj_Lbl_SB_VAT = "xpath=.//*[@id='listingtable']/table/tbody/tr[contains(.,'vat') and contains(.,'-')]"
Obj_Lbl_SB_VAT = "xpath=.//*[@id='listingtable']/table/tbody/tr/td[contains(.,'vat')]"


#############  Card Manager  ######################


Obj_Lnk_Card_Manager = "xpath=.//a[contains(.,'Card Manager')]"
Obj_Lnk_TransactionHistory = "xpath=.//a[@data-original-title='Transaction history']"
Obj_Txt_SearchCard_CM = "xpath=.//input[@type='search']"
Obj_Lnk_ShowTransaction_CM = "xpath=.//*[@id='transactions']/tbody/tr/td[5]/div/div/div/button"

Obj_Lbl_CardStatus_CM = "xpath=.//*[@id='cardsGridId']/tbody/tr/td[4]"
##"xpath=.//*[@id='dialogContentMessageBody']/div[5]/input[@id='returnBtn']"

#### Card Status

Obj_Sel_Deactivate = "xpath=.//input[@value='Deactivate']"
Obj_Sel_LostAndFound = "xpath=.//input[@id='cardStatusFoundRadio']"
Obj_Sel_MarkAsDamaged = "xpath=.//input[@value='Mark as Damaged']"
Obj_Sel_MarkAsDead = "xpath=.//input[@value='Mark as Dead']"
Obj_Sel_PutOnTheBlacklist = "xpath=.//input[@value='Put on the Blacklist']"
Obj_Sel_AssignToCustomer = "xpath=.//input[@value='Assign to customer']"
Obj_Lbl_StatusNotChanged = "xpath=.//*[@id='deactivatedHeader']"


#### Special Compensations


Obj_Lnk_SpecialCompensations = "xpath=.//*[@id='specalcompensationID']"
Obj_Cmb_ProviderType_SC = "xpath=.//*[@id='serviceProviderTypeOptions']"
Obj_Cmb_Provider_SC = "xpath=.//*[@id='serviceProviderOptions']"
Obj_Cmb_POS_SC = "xpath=.//*[@id='pointOfSaleOptions']"
Obj_Btn_Start_SC = "xpath=.//*[@id='specialCompStart']"
Obj_Cmb_CompReason_SC = "xpath=.//*[@id='reasonOptions']"
Obj_Cmb_TicketType_SC = "xpath=.//*[@id='ticketTypeOptions']"
Obj_Cmb_Effect_SC = "xpath=.//*[@id='effectOptions']"
Obj_Lbl_SingleChargeCard = "xpath=.//h2[contains(.,'Single C. C.')]"
Obj_Lbl_SingleValueCard = "xpath=.//h2[contains(.,'Single And Value Ticket')]"
Obj_Lbl_Value = "xpath=.//h2[contains(.,'Value:')]"

Obj_Txt_Total = "xpath=.//*[@id='sccAmount']"
Obj_Txt_VAT = "xpath=.//*[@id='sccVat']"

Obj_Txt_Total1 = "xpath=.//*[@id='singleValueTicketAmount']"
Obj_Txt_VAT1 = "xpath=.//*[@id='singleValueTicketVatPercentage']"

Obj_Btn_ClearFields1 = "xpath=.//*[@id='specialCompClear']"
Obj_Btn_ContinueSCMP = "xpath=.//*[@id='specialCompContinue']"

Obj_Lbl_SCMP_ServiceProvider = "xpath=.//*[@id='compensation']/div[1]/span[1]"
Obj_Lbl_SCMP_SalesPoint = "xpath=.//*[@id='compensation']/div[1]/span[2]"
Obj_Lbl_SCMP_CompReason = "xpath=.//*[@id='compensation']/div[2]/span"
Obj_Lbl_SCMP_TicketType = "xpath=.//*[@id='compensation']/div[3]/span"
Obj_Lbl_SCMP_Effect = "xpath=.//*[@id='compensation']/div[4]/span"
Obj_Lbl_SCMP_CompTransaction = "xpath=.//*[@id='compensation']/div[6]/div[1]/span"


Obj_Lbl_SCMP_CompAmount = "xpath=.//*[@id='compensation']/div[6]"
Obj_Lbl_SCMP_VAT = "xpath=.//*[@id='compensation']/div[6]"
Obj_Lbl_SCMP_VAT1 = "xpath=.//*[@id='compensation']/div[6]/div[2]"
Obj_Lbl_SCMP_CompWay = "xpath=.//*[@id='compensation']/div[8]/div[1]"

Obj_Lbl_SCMP_TotalCompAmount = "xpath=.//*[@id='compensation']/div[8]/div[2]"
Obj_Lbl_SCMP_TotalVAT = "xpath=.//*[@id='compensation']/div[8]/div[3]"

Obj_Btn_SCMP_CardHistory = "xpath=.//*[@id='cardHistoryButton']"

########################  Value

Obj_Lbl_SCMP_Value = "xpath=.//*[@id='valueDiv']/table/thead/tr/th[1]"
Obj_Txt_SCMP_Amount = "xpath=.//*[@id='valueAmount']"
Obj_Txt_SCMP_Vat = "xpath=.//*[@id='valueVat']"


Obj_Lbl_OneLoadinSeasonTicket = "xpath=.//label[contains(.,'Loading season ticket (1)')]"

########################  Special rules

Obj_Txt_MuncipalityValidUntilDate = "xpath=.//*[@id='muncipalityValidUntilDate']"



Obj_Btn_CloseInvalidCompany = "xpath=.//*[@id='closeButtonForCompany']"

########################  Action List

Obj_Img_ActionListPopup = "xpath=.//*[@id='loadAnimationG']"
Obj_Cmb_LoadTicketProduct = "xpath=.//*[@id='cardSaleVo.ticketCode']"
Obj_Tab_ActionList = "xpath=.//*[@id='actionListProcessingID']"
Obj_Txt_CardNoAL = "xpath=.//*[@id='cardNumberBox']"

Obj_Cmb_StatusAL = "xpath=.//*[@id='statusList']"
Obj_Btn_SearchAL = "xpath=.//*[@id='searchBtn']"
Obj_Tbl_SearchResultAL = "xpath=.//*[@id='actionListSearchResultTbl']"
Obj_Tbl_SearchResultALRow1 = "xpath=.//*[@id='actionListSearchResultTbl']/tbody/tr[1]"
Obj_Tbl_SearchResultALRow2 = "xpath=.//*[@id='actionListSearchResultTbl']/tbody/tr[2]"
Obj_Lbl_ActionListStatus = "xpath=.//*[@id='actionListSearchResultTbl']/tbody/tr[1]/td[2]"


Obj_Chk_LoadingSeasonTicket = "xpath=.//*[@id='loadingSeasonTicket']"
Obj_Tbl_SearchResultCH = "xpath=.//table[@id='eventTransactionsTabId']/tbody"
Obj_Lnk_CM_ActionList = "xpath=.//a[contains (@class,'toolIcon actionList')]"
Obj_Btn_ActionListDetails1 = "xpath=.//*[@id='actionListGridId']/tbody[1]/tr[1]/td[5]/div/div/button"  
Obj_Btn_ActionListDetails2 = "xpath=.//*[@id='actionListGridId']/tbody[1]/tr[2]/td[5]/div/div/button"


Obj_Txt_ALData = "xpath=.//*[@id='actionListGridId']/tbody[1]/tr["
Obj_Lbl_CardHistoryData = "xpath=.//*[@id='eventTransactionsTabId']/tbody"



Obj_Lbl_CurrentSeasonFromDate = "xpath=.//*[@id='periodBox1']/span[2]"
Obj_Lbl_CurrentSeasonToDate = "xpath=.//*[@id='period1ProductToDate']"

Obj_Lbl_NextSeasonFromDate = "xpath=.//*[@id='periodBox2']/span[2]"
Obj_Lbl_NextSeasonToDate = "xpath=.//*[@id='period2ProductToDate']"

Obj_Lnk_AreaA = "xpath=.//*[@id='validityAreaSId_1']"
Obj_Lnk_AreaB = "xpath=.//*[@id='validityAreaSId_2']"
Obj_Lnk_AreaC = "xpath=.//*[@id='validityAreaSId_3']"
Obj_Lnk_AreaD = "xpath=.//*[@id='validityAreaSId_4']"


Obj_Lnk_AreaASTC = "xpath=.//a[@id='validityAreaAId1_1' ]"
Obj_Lnk_AreaBSTC = "xpath=.//a[@id='validityAreaAId1_2']"
					                


Obj_Lnk_AreaCSTC = "xpath=.//a[@id='validityAreaAId1_3']"
Obj_Lnk_AreaDSTC = "xpath=.//a[@id='validityAreaAId1_4']"

Obj_Lbl_CurrentDate = "xpath=.//*[@class='current-month weekday today']"

Obj_Lnk_ACLST_ActionList = "xpath=.//*[@data-original-title='Action list']"
Obj_Lbl_ACLSTData = "xpath=.//table[@id='actionListGridId']/tbody/tr[1]"

Obj_Lbl_STC_LoadValue = "xpath=.//*[@id='loadValueId']"
Obj_Btn_WriteToCard = "xpath=.//*[@id='writeToCardBtn']"

Obj_Cmb_CustGrpSTC = "xpath=.//*[@id='allCustomerGroup']"

Obj_Lnk_ActionListStatusChange = "xpath=.//*[@id='actionListProcessingID']"
Obj_Chk_Cancelled = "xpath=.//*[@id='cancelled_1']"

Obj_ACLST_SearchResultRow1 = "xpath=.//table[@id='actionListSearchResultTbl']/tbody/tr[1]"
Obj_ACLST_SearchResultRowNo = ".//table[@id='actionListSearchResultTbl']/tbody/tr"
Obj_ACLST_SearchResultRows = "xpath=.//table[@id='actionListSearchResultTbl']/tbody/tr["


######################
