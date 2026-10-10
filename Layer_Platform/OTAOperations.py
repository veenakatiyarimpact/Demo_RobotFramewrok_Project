'''@author: Priti Gaikwad'''
import pywintypes
import win32com
import win32com.client as w32c
from win32com.client import gencache, Dispatch, DispatchWithEvents, constants
import ctypes
import FileFunctions
#from isobject import isobject

def vkFun():
	return "A";

#Then as second operation I include here action on login to server
def connect_server(qc, server):
	'''Connect to QC server
	input = str(http adress)
	output = bool(connected) TRUE/FALSE  '''
	return True;
	try:
		qc.InitConnectionEx(server); return "cs";			
	except:
		text = "Unable connect to Quality Center database: '%s'"%(server); 
	print "qc.Connected"
	print qc.Connected
	return qc.Connected;

def connect_login(qc, username, password):
    '''Login to QC server
    input = str(UserName), str(Password)
    output = bool(Logged) TRUE/FALSE  '''
    try:
        #return "username";#print "1" + username, password
        qc.Login(username, password);
        return username;#print qc.LoggedIn
    except pywintypes.com_error, err:
        #return "A"; print "fail"
        text = unicode(err[2][2]);
    return qc.LoggedIn;

def connect_project(qc, domainname, projectname):
    '''Connect to Project in QC server
    input = str(DomainName), str(ProjectName)
    output = bool(ProjectConnected) TRUE/FALSE  '''
    var=qc.VisibleDomains
    print var
    try:
        qc.Connect(domainname, projectname)
        print domainname, projectname
    except pywintypes.com_error, err:
        text = "Repository of project '%s' in domain '%s' doesn't exist or is not accessible. Please contact your Site Administrator"%(projectname, domainname); 
    print qc.ProjectConnected;
    return qc.ProjectConnected;
#Second of all method which will include OTAapi dll file

def qc_instance():
	'''Create QualityServer instance under variable qc
	input = None
	output = bool(True/False)'''
	qc= None;
	#try:
		#wsh=win32com.client.Dispatch("WScript.Shell")
		#wsh.Run("C:\Windows\System32\cscript.exe")
		#wsh.Run("cmd /K CD C:\ & Dir")
	print "in qc connect"
	qc = win32com.client.Dispatch("TDApiOle80.TDConnection");
		#qc = gencache.EnsureDispatch("TDApiole80.TDConnection.1");
	text = "DLL QualityCenter file correctly Dispatched"
	print text
	print qc
	return True, qc;
	

#Then main method to connect to QCserver

def qcConnect(server, username, password, domainname, projectname):
    '''Connect to a Project in ALM using given username and password
    input = str(server), str(username), str(password), str(DomainName), str(ProjectName)
    output = ALM Connection Object'''
    # return "1";#print("Getting QC running files");
	
    status,qc = qc_instance();
	#status, qc = qc_instance();return status;
	
    if qc == None: print "qc fail";
    print status;
    if status:
        print("Connecting to QC server");
        if connect_server(qc, server):
            ##connected to server
            #print("Checking username and password");			
            print username, password
            if connect_login(qc, username, password):
                return "5";#print("Connecting to QC domain and project");
                if connect_project(qc, domainname, projectname):
                    print "Connected"
                    text = "Connected"
                    connected = True;
					
					#FileFunctions.AppendInFile("C:\UnifiedRobotFramework\Defects\Log.txt","1")
                    return qc;
					
                else:
                    qcDisconnect(qc)
                    text = "Not connected to Project in QC server.\nPlease, correct DomainName and/or ProjectName";
                    connected = False;
                    return connected, text;
            else:
                text = "Not logged to QC server.\nPlease, correct UserName and/or Password";
                connected = False;
                return connected, text;
        else:
            text = "Not connected to QC server.\nPlease, correct server http address"; 
            connected = False;
            return connected, text;
    else:
        connected = False;
        text = "Unable to find QualityCenter installation files.\nPlease connect first to QualityCenter by web page to install needed files" 
        return connected, text;
	

def qcConnect1(server, username, password, domainname, projectname):
    '''Connect to a Project in ALM using given username and password
    input = str(server), str(username), str(password), str(DomainName), str(ProjectName)
    output = ALM Connection Object'''
	
    print("Getting QC running files");	
	
	
    status, qc = qc_instance();
    if qc == None: print "qc fail"
    print status
    if status:
        print("Connecting to QC server");
        if connect_server(qc, server):
            ##connected to server
            print("Checking username and password");
            print username, password
            if connect_login(qc, username, password):
                print("Connecting to QC domain and project");
                if connect_project(qc, domainname, projectname):
                    print "Connected"
                    text = "Connected"
                    connected = True;
					
					#FileFunctions.AppendInFile("C:\UnifiedRobotFramework\Defects\Log.txt","1")
                    return qc;
					
                else:
                    qcDisconnect(qc)
                    text = "Not connected to Project in QC server.\nPlease, correct DomainName and/or ProjectName";
                    connected = False;
                    return connected, text;
            else:
                text = "Not logged to QC server.\nPlease, correct UserName and/or Password";
                connected = False;
                return connected, text;
        else:
            text = "Not connected to QC server.\nPlease, correct server http address"; 
            connected = False;
            return connected, text;
    else:
        connected = False;
        text = "Unable to find QualityCenter installation files.\nPlease connect first to QualityCenter by web page to install needed files" 
        return connected, text;
def qcDisconnect(qc):
	'''Disconnect from ALM'''
	strType = type(qc)
	print strType
	if (strType <> str and strType<>tuple): 
		qc.Disconnect
		qc.Logout
		qc = None
		print "Disconnected from ALM"

def UpdateResultInALM(objTDConnection, argTestSetFolderPath, argTestSetName, argTestCaseResult):
	strType = type(objTDConnection)
	print strType
	if (strType <> str and strType<>tuple): 
		
		objTestSetTreeMgr = objTDConnection.TestSetTreeManager
		print argTestSetFolderPath
		objTestSetFolder = objTestSetTreeMgr.NodeByPath(argTestSetFolderPath)
		objTestSetFactory = objTestSetFolder.TestSetFactory
		objTestSetList = objTestSetFactory.NewList("")
		print objTestSetList.count	
		print argTestCaseResult
		for item in objTestSetList:
			print item.Name        
			if (item.Name == argTestSetName):
				print True
				objItemAttachment = item.Attachments
				objAttachment = objItemAttachment.AddItem(None)
				objAttachment.FileName = argTestCaseResult
				objAttachment.Type = 1
				objAttachment.Post()
				objAttachment.Refresh
				objItemAttachment = None			
				break
	else:
		print"QC not connected"
		return "false"
    
		
def UpdateTCStatusInALM(objALMConnection, varTestFolder, varTestsetName, varTestNameinALM, passFailStatus):
	#testfolder="Root\TestAutomation" #Path to the folder contains test sets
	#Selecting required testcase
	strType = type(objALMConnection)
	print strType
	if (strType <> str and strType<>tuple): 
		tFactory = objALMConnection.TestFactory
		tsFactory = objALMConnection.TestSetFactory
		tsTreeMgr = objALMConnection.TestSetTreeManager

		tsFolder = tsTreeMgr.NodeByPath(varTestFolder) #use this when we are not working with fixed locations
		TestSetList = tsFolder.FindTestSets(varTestsetName)
		if (TestSetList.Count > 1 ):
			print "FindTestSets found more than one test set: refine search" 
		elif (TestSetList.Count < 1 ):
			print "FindTestSets: test set not found"
		tsTestSet = TestSetList.Item(1)
		tsTestFactory = tsTestSet.tsTestFactory
		tsTestList = tsTestFactory.NewList("")
		for tsTest in tsTestList:
			varALMTest = tsTest.Name
			varIndex = varALMTest.find(varTestNameinALM)
			if (varIndex > 0) :
				print "Test found"
				oRunInstance = tsTest.RunFactory
				oRun=oRunInstance.AddItem("Automated") #Run Name
				print passFailStatus
				oRun.Status = passFailStatus #Run Status
				oRun.Post()   
				oRun.Refresh
				break
			else:
				print "Test not found"
	else:
		print"QC not connected"
		return "false"