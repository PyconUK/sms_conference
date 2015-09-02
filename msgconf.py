import csv
from phone import *
import phonenumbers
def messageConference():
	actualNumbers = 0
	numberCol = 0
	NumberParseExceptions = 0
	otherExceptions = 0

	message=raw_input("Enter message to send via SMS to delegates:")
	
	#parses CSV in this format:
	#Number,Ticket Created Date,Ticket,Ticket Full Name,Ticket First Name,Ticket Last Name,Ticket Email,Ticket Company Name,Ticket Phone Number,Event,Void Status,Price,Ticket Reference,Tags,Unique Ticket URL,Unique Order URL,Order Reference,Order Name,Order Email,Order Company Name,Order Phone Number,Order Discount Code,Order IP,Order Created Date,Order Completed Date,Payment Reference,Code of Conduct,T-shirt size,Age,Sex,Twitter handle,Dietary requirements,Creche,School,Parental consent,Community helper,Mobile telephone number,About you,"Monday ""sprint"" attendance"
	
	with open('tito.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			phoneNumber = str(row[36])
			numberCol= numberCol+1
			if len(phoneNumber) > 2:
				pN = ''
				try:
					pN= parsePhoneNumber(phoneNumber)
					print phoneNumber, pN
					sendSMS(pN,message)
					actualNumbers = actualNumbers + 1
				except phonenumbers.phonenumberutil.NumberParseException as e:
					NumberParseExceptions = NumberParseExceptions + 1
				except:
					otherExceptions = otherExceptions + 1
	print (NumberParseExceptions,otherExceptions,actualNumbers,numberCol)
	messageConference()

messageConference()
