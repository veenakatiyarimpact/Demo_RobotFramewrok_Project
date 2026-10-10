# -*- coding: utf-8 -*-

TC_BROWSER="chrome"
TC_ProjectDir = "C:\Repo\UnifiedRobotFramework"

######  Test Result Config Variables  ######
ModuleFileName = "C:\Repo\UnifiedRobotFramework\Layer_Test\TestConfig\Application_Modules.xlsx"
TestCaseFilePathName = "C:\Repo\UnifiedRobotFramework\Layer_Test\TestConfig"

TestResultLogFilePath="C:\Repo\UnifiedRobotFramework\TestResultLogs"
TestResultTempFilePath = "C:\Repo\UnifiedRobotFramework\TestResultLogs\Temp"
TestResultTemp1FilePath = "C:\Repo\UnifiedRobotFramework\TestResultLogs\Temp1"
TestExecutionBatchFile = "C:\Repo\UnifiedRobotFramework\Batch\TriggerRegression.bat"

ParallelExecutionBatchFile = "C:\Repo\UnifiedRobotFramework\Batch\ParallelExecution.bat"
DefectsDirPath = "C:\Repo\UnifiedRobotFramework\Defects"
strModuleDirName = ""
TestStatusFail = "| FAIL |"
strPassedTcs = ""
strFailedTcs = ""

TestPassed="PASS"

######  Test Result Config Variables  ######


######  ALM Result Update Config Variables  ######

ALMPath = "http://alm12.qc.tieto.com/qcbin"
ALMUserName = "gaikxpri"
ALMPassword = "trade11@16"
ALMDomain = "TIETO"
ALMProject = "Automation_COE"
ALMTestSetFolderPath = "Root\\Test-RobotFramework-ALM"
ALMTestSetName = "SampleTestSet"
ALMAttachLogFile = "Yes"

ALMTestFolder = "Root\\Test-RobotFramework-ALM"
ALMTestsetName = "SampleTestSet"

## Valid values are Yes and No
ALMUpdateTestCaseStatus = "Yes"

PassedTCLog = "C:\UnifiedRobotFramework\TestResultLogs\PassedTCLog.txt"
FailedTCLog = "C:\UnifiedRobotFramework\TestResultLogs\FailedTCLog.txt"

######  ALM Result Update Config Variables  ######


######  GIT variables  ######

GIT_Path = "https://git.etb.tieto.com"
GITUserName = "katiyvee"
GITPwd = "Jaipur@128"


######  GIT variables  ######


##################################################################  TestData Input Variable  


###  Whether to fetch input test data from MySQL or Excel . Following 2 values are valid .
 ## excel
 ## mysql
FetchInputDataFrom = "excel"


######  MySQL Config Variables  ######

MySQLDB ="app_testdata"
MySQLUser ="root"
MySQLPassword="Ashlesha@128"

MySQLHost="127.0.0.1"
MySQLPort="3306"
MySQLTableName = "googletestdata"


######  Excel Config Variables  ######

TestDataFileName ="C:\Repo\UnifiedRobotFramework\TestData\Excel_Data\TestData.xls"
TestDataSheetName = "tbl_testdata"



##################################################################  TestData Input Variable


######  Email variables ######
## Yes
## No
SendLogInEmail = "Yes"
strAttachLogs = ""
EmailRegressionResultTO = "veena.katiyar@tieto.com;veena.katiyar@gmail.com"
EmailRegressionResultCC = "priti.m.gaikwad@tieto.com"
EmailSubject = "Regression on Windows server"
EmailBody = "Hi All , \nPlease find attached result for regression on Windows server.\n-Thanks & Regards ,\nVeena Katiyar"
######  Email variables ######

######  Jira variables ######
## Yes
## No
CreateDefectInJira = "Yes"
JiraProject = "TACE"
JiraUserName = "gaikxpri"
JiraPwd = "trade11@17"
JiraURL = "{'server': 'https://jira.saas.etb.tieto.com'}"

######  Jira variables ######


######  Parallel execution variables ######

ExecuteParallelly = "No"











