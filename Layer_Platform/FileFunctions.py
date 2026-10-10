# -*- coding: utf-8 -*-
import math,random,string
from datetime import date
from datetime import timedelta
import time
from Selenium2Library.utils import BrowserCache
from Selenium2Library.keywords import _browsermanagement
import datetime
import openpyxl
import xlwt
import xlrd
import datetime
import os
import glob
import operator
import shutil
import os
import subprocess

## It verifies whether file exists or not
def VerifyFileExist(sPath) :
	sResult = os.path.isfile(sPath)
	return sResult
	
def AppendInFile(sFilePath,strText):
	f = open(sFilePath, 'a') 
	f.write(strText)
	f.write("\n")
	f.close
	

	

