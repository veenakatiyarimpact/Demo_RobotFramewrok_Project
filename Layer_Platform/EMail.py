'''Install PyWin32 and import win32com object to python before using the library'''
import win32com.client
from win32com.client import Dispatch
import os
import datetime
import time

def print_mail() : 
	outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
	inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
										# the inbox. You can change that number to reference
										# any other folder
	messages = inbox.Items
	message = messages.GetFirst()
	print message.SenderName
	body_content = message.body
	print body_content
	
def check_mail(user,folder,senderAddress,content=None):
	currentTime =  datetime.datetime.now()
	currentValue = datetime.datetime.now().strftime("X%m/X%d/%Y").replace('X0','X').replace('X','')	
	print "currentValue= " 
	print currentValue
	outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
	myfolder =  outlook.Folders[user]
	inbox = myfolder.Folders[folder]
	receivedTime = ""
	text = ""
	for msg in inbox.Items :		
		timevale = msg.CreationTime
		stringTime = '%s/%s/%s' % (timevale.month, timevale.day, timevale.year)		
		if stringTime == currentValue :
			print senderAddress
			print msg.Subject
			print msg.Sender.GetExchangeUser().PrimarySmtpAddress
			outlookSenderAddress = msg.Sender.GetExchangeUser().PrimarySmtpAddress
			if outlookSenderAddress.lower() == senderAddress.lower() :
				if receivedTime == "" or receivedTime < msg.ReceivedTime :
					text = msg.body
					receivedTime  = msg.ReceivedTime
	return text	 	

## mailAttachment is an optional parameter(Set value to "None" if no attahment to attach) rest are mandatory
def Post_email(toEmailID, ccEmailID,mailSubject, mailBody, mailAttachment):
	Result = ""
	outlook = win32com.client.Dispatch('outlook.application')
	mail = outlook.CreateItem(0)
	
	mail.To = toEmailID
	if(ccEmailID<>"None"):
		mail.CC = ccEmailID
   
	mail.Subject = mailSubject
	mail.Body = mailBody
		
	#In case you want to attach a file to the email
	if(mailAttachment<>"None"):
		attachment  = mailAttachment
		mail.Attachments.Add(attachment)
	Result = mail.Send() 	