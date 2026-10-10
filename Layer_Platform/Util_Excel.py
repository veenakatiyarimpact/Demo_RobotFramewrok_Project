from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook
import pywintypes
import win32com
import win32com.client as w32c
from win32com.client import gencache, Dispatch, DispatchWithEvents, constants
import xlsxwriter
import xlwt
import openpyxl
import datetime
from openpyxl.worksheet.copier import WorksheetCopy
import pyodbc

import os
import sys
import time
import subprocess
import glob
from collections import Counter
from collections import OrderedDict

from xlrd import open_workbook
from xlutils.copy import copy


## Create Excel WorkBook - Tested	
def CreateExcelFileXLSX(sFilePath):
	bFlag = False
	bFlag = os.path.isfile(sFilePath) ## Check if file already exists
	
	if bFlag == False:
		workbook = xlsxwriter.Workbook(sFilePath)
		bFlag = True
	return bFlag

	
## Add worksheet to Workbook - Tested	
def AddExcelSheet(sFilePath,sSheetName):
	try:
		wb = load_workbook(sFilePath)
		ws = wb.create_sheet(sSheetName)
		wb.save(sFilePath)
		ws = wb.get_sheet_by_name(sSheetName)
	except Exception,e:
		ws = str(e)
	return ws
	
	
## Rename worksheet in WorkBook	 - Tested
def RenameExcelSheet(sFilePath,sOldSheetName,sNewSheetName):
	try:
		wb = load_workbook(sFilePath)
		
		ws = wb.get_sheet_by_name(sOldSheetName)
		ws.title = sNewSheetName
		wb.save(sFilePath)
		ws = wb.get_sheet_by_name(sNewSheetName)
	except Exception,e:
		ws = str(e)
	return ws

	
## Copy worksheet into same workbook - Tested
def CopyWorksheet(sSourceFilePath,sSourceSheetName,sTargetSheetName):
	try:
		SourceWorkbook = load_workbook(sSourceFilePath)
		SourceWorksheet = SourceWorkbook.get_sheet_by_name(sSourceSheetName)
		TargetWorksheet = SourceWorkbook.create_sheet(sTargetSheetName)
	
		instance = WorksheetCopy(SourceWorksheet, TargetWorksheet)
	
		WorksheetCopy.copy_worksheet(instance)
		SourceWorkbook.save(sSourceFilePath)
		
		ws = SourceWorkbook.get_sheet_by_name(sTargetSheetName)
	except Exception,e:
		ws = str(e)
	return ws

	
## Copy workbook - Tested
def CopyExcelWorkBook(sSourceFilePath,sTargetFilePath):
	try:
		SourceWorkbook = load_workbook(sSourceFilePath)
		bFlag = SourceWorkbook.save(sTargetFilePath)
		
		ws = os.path.isfile(sTargetFilePath)
	except Exception,e:
		ws = str(e)
	
	return ws

	
##  Verify that Worksheet is present in WorkBook - Tested	
def VerifyWorkSheetPresent(sFilePath,sSheetName):
	try:
		wb = load_workbook(sFilePath)
		ws = wb.get_sheet_by_name(sSheetName)	
	except Exception,e:
		ws = str(e)
	return ws

	
##  Set value in a cell	- Tested
def SetCellValue(sFilePath,sSheetName,CellName,CellValue) :
	try:
		wb=load_workbook(sFilePath)
		ws=wb.get_sheet_by_name(sSheetName)
		
		ws.cell(coordinate=CellName).value= CellValue		
		wb.save(sFilePath)
		ws = ws.cell(coordinate=CellName).value
	except Exception,e:
		ws = str(e)
	
	return ws

	
##  Get value in a cell - Tested
def GetCellValue(sFilePath,sSheetName,CellName) :
	try:
		wb=load_workbook(sFilePath)
		ws=wb.get_sheet_by_name(sSheetName)
	
		ws = ws.cell(CellName).value
	except Exception,e:
		ws = str(e)
	
	return ws

	
## Open Excel workbook in visible mode - Tested	
def OpenExcelWorkBook(sFilePath) :

	bFlag = os.path.isfile(sFilePath)	
	
	if bFlag==True:
		xlApp = win32com.client.Dispatch("Excel.Application")
		workbook = xlApp.Workbooks.Open(sFilePath)
		xlApp.Visible = True
		
		return workbook
	else: 
		print "Please check excel file path"       
        return False

		
## Find text string in the WorkBook	- Tested
def FindTextInWorksheet(sFilePath,sSheetName, SearchString):
	try:
		wb=load_workbook(sFilePath)
		ws=wb.get_sheet_by_name(sSheetName)
		t = datetime.datetime.utcnow()
	
		for row in ws.iter_rows():
			for cell in row:			
				if(str(SearchString)==str(cell.value)):
					return cell
				
		print "Text : " + SearchString + "  not found in the sheet : " + sSheetName 
		return False
	except Exception,e:
		err = str(e)
		print err
		return False
    
	
## Find all occurences of text string in the WorkBook - Tested	
def FindAllTextInWorksheet(sFilePath,sSheetName, SearchString):
	try:
		wb=load_workbook(sFilePath)
		ws=wb.get_sheet_by_name(sSheetName)
		t = datetime.datetime.utcnow()
		Result =""
	
		for row in ws.iter_rows():
			for cell in row:			
				if(str(SearchString)==str(cell.value)):
					Result = Result + str(cell) + ";"
				
		if Result == "":
			Result = False
			print "Text : " + SearchString + "  not found in the sheet : " + sSheetName
		return Result
	except Exception,e:
		err = str(e)
		print err
		return False
    
	
## Find all occurences of text string in the WorkBook and replace it with new string - Tested	
def ReplaceTextInWorksheet(sFilePath,sSheetName, SearchString , ReplaceString):
	try:
		wb=load_workbook(sFilePath)
		ws=wb.get_sheet_by_name(sSheetName)
		t = datetime.datetime.utcnow()
		Result =""
		bFlag = False
		iPresent = 0
	
		for row in ws.iter_rows():
			for cell in row:			
				if(str(SearchString)==str(cell.value)):
					cell.value = ReplaceString
					bFlag = True
					iPresent = iPresent + 1
				
		wb.save(sFilePath)
				
		if bFlag == False:		
			print "Text : " + SearchString + "  not found in the sheet : " + sSheetName
		else:
			print "Found and replaced " + str(iPresent) + " occurences of " + SearchString + " replaced with " + ReplaceString
		return iPresent
	
	except Exception,e:
		err = str(e)
		print err
		return False

		
		###################################  Following functions not tested yet ###################################
		

	
	


## Find active modules		
def FindActiveModules1(sFilePath):
	wb=load_workbook(sFilePath)
	sSheetName = "tbl_modules"
	ws=wb.get_sheet_by_name(sSheetName)
	SearchString = "Yes"
	Result =""
	
	bFlag = os.path.isfile(sFilePath)
	
	return bFlag
	
	
## Read from Excel
def ReadWorkSheet():	
	#strConnection =  pyodbc.connect("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:\Robot_Framework\Layer_Test\TestConfig\Application_Modules.xls;Extended Properties=""Excel 8.0;HDR=Yes;"";")
	
	strConnection =  pyodbc.connect("DRIVER=Microsoft.Jet.OLEDB.4.0;DATABASE =C:\Robot_Framework\Layer_Test\TestConfig\Application_Modules.xls;Extended Properties=""Excel 8.0;HDR=Yes;"";")
	
	cursor = strConnection.cursor()
	sSQLQuery = "SELECT ModuleName FROM [tbl_modules$] where Active = 'Yes'" 

	cursor.execute(sSQLQuery)
	tables = cursor.fetchall()

	for row in cursor.columns(table='WORK_ORDER'):
		print row.column_name
		for field in row:
			print field
	
## Close WorkBook(objWorksheet)
def QuitExcel(objWorkbook, objExcel):
	objWorkbook.close
	objWorkbook=None
	objExcel.quit
	objExcel = None
	del objExcel
	del objWorkbook

## Save WorkBook  
def SaveWorkbook(sFilePath) :
	wb=load_workbook(sFilePath)	
	wb.save(sFilePath)
	

##########################################################################################################################


## Write to Excel
def WriteToExcel(sFilePath,sSheetName,Row,Column,Value) :
	bFlag = os.path.isfile(sFilePath)
	
	if bFlag==True:
		
		if (Row != "" and Column != ""):			
			wb=load_workbook(sFilePath)	
			return True
			ws=wb.get_sheet_by_name(sSheetName)
			return ws
			ws.cell(row=Row, column=Column, value=Value)
			wb.save(sFilePath)
			return True
		else:
			return False
	
def get_profile_id(varExcelFilePath, objDictionary) :
    objExcel = open_excel()
    objWorkbook = objExcel.Workbooks.Open(varExcelFilePath)
    objWorksheet = objWorkbook.Worksheets("Base Data")
    varTotalColumns = objWorksheet.UsedRange.Columns.Count
    varTotalRows = objWorksheet.UsedRange.Rows.Count
    if (objWorksheet):
        write_values_to_profile_excel(objWorksheet,objDictionary)
		#Save workbook		
        if (write_values_to_profile_excel):
            save_workbook(objWorkbook)
            #Return calculated ProfileID in excel            
            if (save_workbook):                
                #Column number for 'Result'                
                for jCnt in range(2, varTotalColumns+1):
                    cellValue = objWorksheet.Cells(1,jCnt).value                    
                    if (cellValue == "Result"):
                        varResultColumn = jCnt
                        break
        varProfileID = objWorksheet.Cells(2,varResultColumn).value
        objWorkbook.close
        objExcel.Quit
        #objExcel.close
        objWorkbook = None
        objExcel=None
        return varProfileID
    else:
	    return False
		
def write_values_to_profile_excel(objWorksheet,objDictionary) :
    #Number of rows and columns in workbook
    varTotalColumns = objWorksheet.UsedRange.Columns.Count
    varTotalRows = objWorksheet.UsedRange.Rows.Count
	#Column number for 'Input'
    for iCnt in range (2, varTotalColumns):
        cellValue = objWorksheet.Cells(1,iCnt).value
        if (cellValue == "Input"):
            varInputColumn = iCnt
            break
    #Number of rows containing keys
    for kCnt in range (2, varTotalRows):
        cellValue = objWorksheet.Cells(kCnt,1).value
        if (cellValue == None):
            varKeyRows = kCnt
            break			
    #Clear the previous values in the cells
    varRange="G2:G" + str(varKeyRows)
    objWorksheet.Range(varRange).Clear
    #Write values for the keys in Input column
    for lCnt in range(2, varKeyRows):        
        varKey = objWorksheet.Cells(lCnt,1).value
        if objDictionary.has_key(varKey):
            write_to_excel(objWorksheet, lCnt, varInputColumn, objDictionary[varKey])	
    return True

def get_profile_links(varProfileID, varExcelFilePath) :
    listLinks = []
    objExcel = open_excel()
    print varProfileID
    objWorkbook = objExcel.Workbooks.Open(varExcelFilePath)
    objWorksheet = objWorkbook.Worksheets("Profile-Links")
    if (objWorksheet):
        varTotalColumns = objWorksheet.UsedRange.Columns.count
        varTotalRows = objWorksheet.UsedRange.Rows.count
        cellProfileID =objWorksheet.UsedRange.Find(varProfileID)
        varColumn = cellProfileID.Column
        varRow = cellProfileID.Row
        for iCnt in range(varColumn, varTotalColumns+2): 
            cellValue = objWorksheet.Cells(varRow,iCnt).value		
            if (cellValue == None):
                varEndColumn = iCnt
                break
        for jCnt in range(varColumn+1 , varEndColumn):
            varLink = objWorksheet.Cells(varRow,jCnt).value
            listLinks.append(varLink)
        #continue
        #close workbook		
    objWorkbook.close
    objExcel.Quit
    objWorkbook = None
    objExcel=None
    return listLinks

'''
def getProfileLinksFromExcel(objWorksheet,varProfileID) :
    listLinks = []
	#Number of rows and columns in workbook
    varTotalColumns = objWorksheet.UsedRange.Columns.count
    varTotalRows = objWorksheet.UsedRange.Rows.count
    print varTotalColumns
    print varTotalRows
    cellProfileID =objWorksheet.UsedRange.Find(varProfileID)
    varColumn = cellProfileID.Column
    varRow = cellProfileID.Row
    for iCnt in range(varColumn, varTotalColumns+2): 
        print varTotalColumns+2	
        cellValue = objWorksheet.Cells(varRow,iCnt).value		
        print cellValue
        if (cellValue == None):
			varEndColumn = iCnt-1
        continue
    print varColumn
    print "end column"
    print varEndColumn
    for jCnt in range(varColumn+1 , varEndColumn):
        varLink = objWorksheet.Cells(varRow,jCnt).value
        listLinks.append(varLink)
        #print varLink
        #print listLinks
        continue
	return listLinks
'''
