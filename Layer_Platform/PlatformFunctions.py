# -*- coding: utf-8 -*-
import math,random,string
from datetime import date
from datetime import timedelta
import time
from Selenium2Library.utils import BrowserCache
from Selenium2Library.keywords import _browsermanagement
import datetime

def mGeneratePID(sCustType):
                sCheckSumBit = ""
                sCheckSumSelection = "A,B,C,D,E,F,H,J,K,L,M,N,P,R,S,T,U,V,W,X,Y"

                bAflag = False
                if "child" not in sCustType: 
                        sYear = mGetTwoCharStr(str(random.randint(1,9) + 70))
                        sYearNew=sYear
                else:
						sYear1=mGetTwoCharStr(str(random.randint(1,4)+ 98 ) )
						sYear2=mGetTwoCharStr(str(random.randint(1,13)) )
						sYear= int(sYear1)+ int(sYear2)
                if int(sYear)>=100: 
                        bAflag= True
                        sYear=int(sYear)%100
                        if sYear<10: 
                            sYear= "0"+ str(sYear)
                            sYearNew="20"+sYear
                        else:
							sYearNew="19"+str(sYear)     
							sYearNew=2014-int(sYearNew)     
                sMonth =  mGetTwoCharStr(str(random.randint(1,12) ))
                sDay = mGetTwoCharStr(str(random.randint(1,28)))
                sPID2 = mGetTwoCharStr(str(random.randint(1,99)))
                sPID3= str(random.randint(1,9))  
                sPID1= sDay + sMonth +  str(sYear)
                sPID = sPID1 +  sPID2 + sPID3
				
                if bAflag:
                        sSeparator =   "A"
                else:
                        sSeparator =  "-"
                                         
                iMod = ( int(sPID)%31)
                if iMod<10:
                        sCheckSumBit = str(iMod)
                else:
                        sCheckSumBit = sCheckSumSelection.split(",")[(iMod-10)]
                                                                  
                sPersonalID = sPID1+sSeparator+sPID2+sPID3+sCheckSumBit
		return sPersonalID
 
def mGenerateAID(sCustType):
                sCheckSumBit = ""
                sCheckSumSelection = "A,B,C,D,E,F,H,J,K,L,M,N,P,R,S,T,U,V,W,X,Y"

                bAflag = False
                if sCustType=="Adult": 
                        sYear = mGetTwoCharStr(str(random.randint(1,9) + 70))
                        sYearNew=sYear
                else:
						sYear1=mGetTwoCharStr(str(random.randint(1,4)+ 97 ) )
						sYear2=mGetTwoCharStr(str(random.randint(1,13)) )
						sYear= int(sYear1)+ int(sYear2)
                if int(sYear)>=100: 
                        bAflag= True
                        sYear=int(sYear)%100
                        if sYear<10: 
                            sYear= "0"+ str(sYear)
                            sYearNew="20"+sYear
                        else:
							sYearNew="19"+str(sYear)     
							sYearNew=2014-int(sYearNew)     
                sMonth =  mGetTwoCharStr(str(random.randint(1,12) ))
                sDay = mGetTwoCharStr(str(random.randint(1,28)))
                sPID2 = mGetTwoCharStr(str(random.randint(1,99)))
                sPID3= str(random.randint(1,9))  
                sPID1= sDay + sMonth +  str(sYear)
                sPID = sPID1 +  sPID2 + sPID3
				
                if bAflag:
                        sSeparator =   "A"
                else:
                        sSeparator =  "-"
                                         
                iMod = ( int(sPID)%31)
                if iMod<10:
                        sCheckSumBit = str(iMod)
                else:
                        sCheckSumBit = sCheckSumSelection.split(",")[(iMod-10)]
                                                                  
                sPersonalID = sPID1+sSeparator
                   
		return sPersonalID

  
def mGenerateFinnishBID():
          
		for i in range (0, 10):
			sVar1 = str(random.randint(1,8))     
			sVar2 = str(random.randint(1,9))
			sVar3 = str(random.randint(1,9))
			sVar4 = str(random.randint(1,9))
			sVar5 = str(random.randint(1,9))
			sVar6 = str(random.randint(1,9))
			sVar7 = str(random.randint(1,9))
			sMod =  ((int(int(sVar1)*7)+int(int(sVar2)*9)+int(int(sVar3)*10)+int(int(sVar4)*5)+int(int(sVar5)*8)+int(int(sVar6)*4)+int(int(sVar7)*2))%11)
			if(sMod >= 2):
				sVar8 = 11 - sMod
				break
		sBusinessID = str(sVar1)+""+str(sVar2)+""+str(sVar3)+""+str(sVar4)+""+str(sVar5)+""+str(sVar6)+""+str(sVar7)+"-"+str(sVar8)
		return  sBusinessID
	


def DeptUnitID():
          
		for i in range (0, 10):
			sVar1 = str(random.randint(1,9))     
			sVar2 = str(random.randint(1,9))
			sVar3 = str(random.randint(1,9))
			sVar4 = str(random.randint(1,9))
			sVar5 = str(random.randint(1,9))
			sVar6 = str(random.randint(1,9))
			sMod =  ((int(sVar1*7)+int(sVar2*9)+int(sVar3*10)+int(sVar4*5)+int(sVar5*8)+int(sVar6*4))%11)
			if(sMod >= 2):
				sVar8 = 11 - sMod
				break
		sBusinessID = str("9")+str(sVar1)+""+str(sVar2)+""+str(sVar3)+""+str(sVar4)+""+str(sVar5)+""+str(sVar6)+""+str(sVar8)
		return  sBusinessID
	
def mBreakCardNo(sCardNo):
    sVar1=sCardNo[0:7]
    sVar2=sCardNo[7:11]
    sVar3=sCardNo[11:18]
    sVar4=sCardNo[19:20]
    sVarFinal=sVar1+"."+sVar2+"."+sVar3+sVar4
    print sVarFinal
    return sVarFinal

def mBreakCardNoProper(sCardNo):
    sVar1=sCardNo[0:6]
    sVar2=sCardNo[6:10]
    sVar3=sCardNo[10:17]
    sVar4=sCardNo[18:19]
    sVarFinal=sVar1+"."+sVar2+"."+sVar3+sVar4
    print sVarFinal
    return sVarFinal
    
    
def GetCustNo(sCustNo):
    print sCustNo.partition("/")[0].strip()
    return sCustNo.partition("/")[0].strip()
    



def GetBrowser(url):
    obj = BrowserCache()
    open_browser = obj.get_open_browsers()
    
    obj = _browsermanagement()
    open_browser=obj.get_current_Browser()    
    print open_browser
	
	
def mGenerateCompanyAID():
	AID = str(random.randint(1000000,9999999))
	AID = "9" + AID
	return AID
	
			
def FormatVoucherNo(sVoucherNo):
	
	strVoucher=str(sVoucherNo)		
	sTemp = strVoucher[0:4] + " " + strVoucher[4:8] + " " + strVoucher[8:17] 
	return sTemp
	

def GetRandomNo():
	TempNo = str(random.randint(1,100))  
	return TempNo
	
def GetSmallRandomNo():
	TempNo = str(random.randint(10,20))  
	return TempNo
	