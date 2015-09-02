import json
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException

configFile = json.loads(open('config.json','r').read())
import phonenumbers as pn
import string

def parsePhoneNumber(n,debugging = False):
	if debugging: print (n)
	n = pn.parse(n,'GB')
	assert (pn.is_possible_number(n))	
	isUK = pn.is_valid_number_for_region(n,'GB')
	if debugging: print('valid UK number?',isUK)
	INTN = pn.format_number(n, pn.PhoneNumberFormat.INTERNATIONAL)
	if debugging: print INTN
	return INTN
	
def sendSMS(SMSNumber,message):
	global configFile

	account_sid = configFile['twilio_account_sid']# Your Account Sid and Auth Token from twilio.com/user/account
	auth_token = configFile['twilio_auth_token']
	client = TwilioRestClient(account_sid, auth_token)

	try:
		parsedNumber = parsePhoneNumber(SMSNumber)
		message = client.messages.create(body=message, to=parsedNumber, from_=configFile['twilio_number'])

	except TwilioRestException as e:
		print 'error for '+SMSNumber+' from Twillio rest exception '+ str(e) 
	except Exception, e:
		print 'other error for '+SMSNumber+' from: '+ str(e) 
