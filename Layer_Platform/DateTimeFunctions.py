# -*- coding: utf-8 -*-
import math,random,string
from datetime import date
from datetime import timedelta
import time
from Selenium2Library.utils import BrowserCache
from Selenium2Library.keywords import _browsermanagement
import datetime
     
def AddDays(sDays):
    # Get today.
    today = date.today()
    # Subtract timedelta of 1 day.
    futureday = today + timedelta(days=int(sDays)-1)
                    
    today=today.strftime('%d.%m.%Y')
    futureday=futureday.strftime('%d.%m.%Y')
    return futureday
	
        
def GetTimeStamp():
    # Get today.
    today = date.today()                       
    today=today.strftime('%d%m%Y')
    stime=time.strftime('%H:%M:%S')
    print today+"-"+stime
    return today+"-"+stime

def GetTimeStampLong():
    # Get today's Date & Time.
    now = datetime.datetime.now()
    now=now.strftime('%d.%m.%Y_%X')
    print now
    return now


def AddDaystoDate(sDate,sDays):
    # Get today.
    
    today=sDate
    today = datetime.datetime.strptime(sDate, "%d.%m.%Y")

    # Subtract timedelta of 1 day.
    futureday = today + timedelta(days=int(sDays)-1)
                    
    #today=today.strftime('%d.%m.%Y')
    futureday=futureday.strftime('%d.%m.%Y')
    print futureday
    return futureday        
    
     
def GetTodayDate():		
    # Get today.
    today = date.today()  
                       
    today=today.strftime('%d%m%Y')
    return today+"-"+stime
	

def CompareDateWithCurrentDate(sDate):
	
	CurrentDate = datetime.now()	
	print CurrentDate
	sDate1 = datetime.strptime(sDate, "%d.%m.%Y")
	diff = CurrentDate - sDate1
	print diff
	if diff.days < 0:
		return 1
	else:
		return 0
		
	
def VerifyIsDate(sDate):	    
	sResult = datetime.datetime.strptime(sDate, '%Y-%m-%d')    
	return sResult	
	
	
def GetTodayDateYYYYMMDD():		
    # Get today.
    today = date.today()  
                       
    today=today.strftime('%Y-%m-%d')
    return today
	
def FormatDateYYYYMMDD(sDate):
	# dd.mm.yyyy to yyyy-mm-dd
	strDate=str(sDate)		
	sTemp = strDate[6:10] + "-" + strDate[3:5] + "-" + strDate[0:2]	
	return sTemp
	

def GetTimeHr():            
    
    stime=time.strftime('%H')
    return stime	

def fun_splitSec(fNumSec):
              
  iDays = None
  iHours = None
  iMinutes = None
  iSeconds = None
  iHoursTemp = None
  iMinutesTemp = None  

  fNumSec=int(fNumSec)

  iDays = fNumSec/86400
  iHoursTemp = fNumSec - (iDays * 86400)
  iHours = iHoursTemp/3600
  iMinutesTemp = iHoursTemp - (iHours * 3600)
  iMinutes = iMinutesTemp/60
  iSeconds = iMinutesTemp - (iMinutes * 60)
  
  sString=str(iDays)+" Days "+str(iHours)+" Hours  "+str(iMinutes)+ " Minutes "+str(iSeconds)+" Seconds."
  print sString
  return sString	