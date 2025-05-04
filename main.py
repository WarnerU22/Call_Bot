import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

client = Client(
    os.getenv("TWILIO_ACCOUNT_SID"),
    os.getenv("TWILIO_AUTH_TOKEN")
)

def make_call(to_number):
    call = client.calls.create(
        to=to_number,
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        url=f"{os.getenv('NGROK_PUBLIC_URL')}/voice"
    )
    print(f"📞 Call started: {call.sid}")

# Example usage
make_call("+19313345875")
