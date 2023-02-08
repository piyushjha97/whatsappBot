from flask import Flask
from flask import request
from twilio.rest import Client 
import os

from marketstack import get_stock_LTP
app = Flask(__name__)   #initialize the flask application

ACCOUNT_ID = os.environ.get('TWILIO_ACCOUNT')
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
client = Client(ACCOUNT_ID, TWILIO_TOKEN)
TWILIO_NUMBER = 'whatsapp:+14155238886'



def create_response(msg):
    response = ""
    if msg == "hi" or msg == "hello" or msg == "hi twilio":
        response =  "hello, welcome to the stock market bot !!"
        response += "Type sym:<stock_symbol> to get the last traded price of the stock"

    elif 'sym:' in msg:
        data = msg.split(":")
        stock_symbol = data[1]
        stock_price = get_stock_LTP(stock_symbol)
        last_price = stock_price['last_price']
        last_price = str(last_price)
        #response = "Last Traded Price for "+ stock_symbol + " is "+ last_price
        response = "Todays opening price for "+ stock_symbol + " is $"+ last_price

    else :
        response = "Please type hi/hello to get started."

    return response

def send_msg(msg, recipient):
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient
    )


@app.route("/webhook", methods=["POST"])   
def webhook():                               #getting data from the flask app sent using POST method

    f = request.form
    msg = f['Body']
    sender = f['From']
    response = create_response(msg)
    send_msg(response, sender)
    return "OK report", 200

    #TWILIO_ACCOUNT, TWILIO_TOKEN