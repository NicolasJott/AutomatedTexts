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

cellphone = +13304233291
twilio_number = +19894364933
def send_message(quote):
    account = "ACbdb2cb2993cfc52ab2a094b4793212d5"
    token  = "51c053a4d141a46c2e6b472d132df957"
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