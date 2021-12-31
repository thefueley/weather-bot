import os
from twilio.rest import Client
import requests

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_service_num = os.environ['TWILIO_PHONE']
twilio_subscriber = os.environ['TWILIO_SUBSCRIBER']

client = Client(account_sid, auth_token)

def send_sms():
    # send message
    message = client.messages.create(
        body = text_body,
        from_ = twilio_service_num,
        to = twilio_subscriber
    )
    print(message.status)

# grab forecast for Columbia, MD
response = requests.get("https://api.weather.gov/gridpoints/LWX/101,85/forecast")
response.raise_for_status()

forecast = response.json()

# grab forecast for today only
today_forecast = forecast["properties"]["periods"][:2]

text_body = ""
for weather in today_forecast:
    text_body += f"{weather['name']}.\n"
    text_body += f"{weather['detailedForecast']}\n"

# send weather report
send_sms()
