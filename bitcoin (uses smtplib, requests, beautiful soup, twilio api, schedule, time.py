"""This program gets the bitcoin value from worldcoinindex.com using beautfiulsoup library 
and performs profit/loss calculations with it based on user's 2 personal investments at different btc rates
using smtplib it sends different content email notificationsto user that vary depending on the high/low profit levels
using twilio client it sends similar text messages to user that vary based on the same levels """

# SMTP is simple mail transfer protocol, used for sending email
import smtplib
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import schedule
import time


def BitcoinPrice():

	base_url = 'https://www.worldcoinindex.com/coin/bitcoin'
	r = requests.get(base_url)
	soup = BeautifulSoup(r.text, 'lxml')

	# extracts all info from selected div, gets just the text and splits it into a list of items
	# in this case it's [u'$', u'16,855.84']
	current_price = soup.find('div',{'class': 'col-md-6 col-xs-6 coinprice'}).get_text().split()

	# isolates just the number part and replace comma to a dot so it fits the float form 
	btc_price = current_price[1].replace(',','.')

	# gets rid of the last 3 charachters, which are cents and a dot
	# converts number to float
	btc_price = float(btc_price[:-3])



	profit_loss(btc_price)

def profit_loss(btc_price):


	buyin1 = 0.22853543
	btc_rate1 = 10.778
	money_spent1 = (buyin1 * btc_rate1) * 1000
	revenue1 = (btc_price * buyin1) * 1000
	profit_loss1 = revenue1 - money_spent1


	buyin2 = 0.17042113
	btc_rate2 = 14.454
	money_spent2 = (buyin2 * btc_rate2) * 1000
	revenue2 = (btc_price * buyin2) * 1000
	profit_loss2 = revenue2 - money_spent2

	overall_profit_loss = (profit_loss1 + profit_loss2)

	print "The current bitcoin price is $%.3f\n" % btc_price
	print "Net profit/loss from buyin 1 is $%.2f - bought at %r\n" % (profit_loss1, btc_rate1)
	print "Net profit/loss from buyin 2 is $%.2f - bought at %r\n" % (profit_loss2, btc_rate2)
	print "Your overall profit/loss is $%.3f" % overall_profit_loss

	if overall_profit_loss < 100:
		email_notification(2, btc_price)
		sms_notification(2, btc_price)
	elif overall_profit_loss < 500:
		email_notification(1, btc_price)
		sms_notification(1, btc_price)
	elif overall_profit_loss < 1000:
		email_notification(0, btc_price)
		sms_notification(0, btc_price)

def email_notification (value, btc_price):

	# the SMTP object represents a connection to an SMTP mail server and has
	# methods for sending email. This creates an SMTP object for connecting to gmail
	# Domain name will be different for each provider
	# port number will most always be 587
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

	# important step (method) to establish 'say hello' a connection to the email server
	# example returns '250, b'mx.google.com at your service, etc.'
	smtpObj.ehlo()

	# this required step enables encryption for your connection, it returns
	# (220, '2.0.0 Ready to start TLS') 220 in the return value means that the server is ready
	smtpObj.starttls()

	# login with your username and password by using the login() method
	# returns (235, '2.7.0 Accepted') 235 means successful authentication
	smtpObj.login('p.vengrinovich@gmail.com', 'Ecology9')

	# after logging in to the SMTP server we can use sendmail() method to actually send the email
	# first agument is my email address (from), second is the recepeints, third is the email subject and body body
	# sends out different emails depending on the value of profit/loss
	if value == 1:
		smtpObj.sendmail('p.vengrinovich@gmail.com', 'p.vengrinovich@gmail.com', 'Subject: Bitcoin profit Less then $500 \nThe price is at $'+ str(btc_price))

	if value == 2:
		smtpObj.sendmail('p.vengrinovich@gmail.com', 'p.vengrinovich@gmail.com', 'Subject: Bitcoin profit Less then $100 \nThe price is at $'+ str(btc_price))

	if value == 0:
		smtpObj.sendmail('p.vengrinovich@gmail.com', 'p.vengrinovich@gmail.com', 'Subject: Bitcoin profit Less then $1000 \nThe price is at $'+ str(btc_price))

	# always disconnect your program from the SMTP server when done sending emails
	smtpObj.quit()

def sms_notification (value, btc_price):

	# these are taken directly from twilio account
	accountSID = 'AC9818e51806fa5548c74104a1c86b9313'
	authToken = '25bae8eae5700a7f2f419e2f3e87f497'
	myTwilioNumber = '+14252245945'
	myCellPhone = '+14156109726'

	# the call to the Client returns a Twilio Client object 
	twilio_client_object = Client(accountSID, authToken)

	# This object has a messages attribute which in turn has a create method
	# you can use to send text messages; 
	# sends different text messages with 'body' as the message depending on the value of profit
	if value == 0:
		message = twilio_client_object.messages.create(body = 'Bitcoin profit is less then a $1000 at $'+ str(btc_price), 
													from_ = myTwilioNumber, to = myCellPhone)
	if value == 1:
		message = twilio_client_object.messages.create(body = 'Its happening: bitcoin profit is less then a $500 at $'+ str(btc_price), 
													from_ = myTwilioNumber, to = myCellPhone)
	if value == 2:
		message = twilio_client_object.messages.create(body = 'Danger!!! Bitcoin profit is less then a $100 at $'+ str(btc_price), 
													from_ = myTwilioNumber, to = myCellPhone)	

# main function is to make importing the code later easier into other programs
# schedule uses the schedule module to run this script every hour
if __name__ == "__main__":
	
	schedule.every(60).minutes.do(BitcoinPrice)
	BitcoinPrice()

	while True:
		schedule.run_pending()



