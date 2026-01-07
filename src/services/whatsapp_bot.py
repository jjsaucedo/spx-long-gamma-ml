import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

client = Client(
    os.getenv("TWILIO_SID"),
    os.getenv("TWILIO_AUTH_TOKEN")
)

def send_whatsapp(message):
    client.messages.create(
        body=message,
        from_=os.getenv("WHATSAPP_FROM"),
        to=os.getenv("WHATSAPP_TO")
    )
