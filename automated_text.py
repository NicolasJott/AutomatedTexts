#create an array that stores text messages

TEXT_MESSAGES = [
    "Hello World!",
    "You have an assignment due at 11:59 PM."
]

#Send preset message using API send_message
import os
from twilio.rest import Client
import schedule 
import random, time

cellphone =             #Enter number you want to send to
twilio_number =         #Enter twilio api phone number
def send_message(quote):
    account = ""
    token  = ""
    client = Client(account,token)

    client.messages.create(to=cellphone,
                            from_=twilio_number,
                            body=quote)
 # Use schedule library to schedule when texts are sent  
quote = TEXT_MESSAGES[random.randint(0,len(TEXT_MESSAGES))]                         
#schedule.every().day.at("14:56").do(send_message,quote)
send_message(quote)
while True:
    schedule.run_pending()
    time.sleep(2)
