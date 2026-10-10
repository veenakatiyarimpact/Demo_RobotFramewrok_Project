# -*- coding: utf-8 -*-
import math,random,string
from datetime import date
from datetime import timedelta
import time
from Selenium2Library.utils import BrowserCache
from Selenium2Library.keywords import _browsermanagement
import datetime
     
def mGetTwoCharStr(sInStr) :

      
      if(len(sInStr)==1) :
            sNewStr = "0"+sInStr
        
      else:
            return  sInStr
                        
      return sNewStr

	
def GetSubstringByPOS(strString,chrDelimiter):
	strTemp = strString.split(" ")[0].strip()
	return strTemp	   
	

def StrAscOrder(strString1,strString2): 
	if strString1<=strString2:		
		return 1		
	else:		
		return 0	

def StrDscOrder(strString1,strString2): 
	if strString1>=strString2:		
		return 1		
	else:		
		return 0	

def IsSubstring(MainString,SubSting1):
	Result = MainString.find(SubSting1)
	print Result
	return Result		
 

def GetSubstringByDelimiter(strString,chrDelimiter,POS):
	intPOS = int(POS)
	print intPOS
	strTemp = strString.split(chrDelimiter)[intPOS].strip()
	return strTemp	
	
def CatenateString(str1,str2,str3,str4,str5):
	Result = str1+str2+str3+str4+str5
	return Result
		
def StringContains(MainString,SearchString):
	#  returns -1 if the string cannot be found.
	iPOS=MainString.find(SearchString)
	return iPOS
	
def RemoveSpaceInString(MainString):
	#  returns -1 if the string cannot be found.
	MainString=MainString.replace(" ","")
	return MainString
	
def CapitalizeString(MainString):
	#  returns -1 if the string cannot be found.
	MainString=MainString.capitalize()
	return MainString
	