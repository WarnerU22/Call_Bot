from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_number = os.environ.get("TWILIO_PHONE_NUMBER")
public_ngrok_url = os.environ.get("NGROK_PUBLIC_URL")  # e.g., "https://your-ngrok-id.ngrok-free.app"

client = Client(account_sid, auth_token)

def make_call(to_number):
    call = client.calls.create(
        to=to_number,
        from_=twilio_number,
        url=f"{public_ngrok_url}/voice"
    )
    print(f"Call initiated: {call.sid}")

if __name__ == "__main__":
    # Example usage
    make_call("+19313345875")  # Replace with the actual number
