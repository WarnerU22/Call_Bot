from twilio.rest import Client
import time
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
ngrok_url = os.getenv("NGROK_PUBLIC_URL")  # Your public URL for /voice

client = Client(account_sid, auth_token)

def make_call(to_number):
    try:
        call = client.calls.create(
            to=to_number,
            from_=twilio_number,
            url=f"{ngrok_url}/voice"
        )
        print(f"📞 Calling {to_number} - SID: {call.sid}")
        with open("calls.log", "a") as log:
            log.write(f"Called {to_number} - SID: {call.sid}\n")
    except Exception as e:
        print(f"❌ Failed to call {to_number}: {e}")

def call_all_numbers(filename="numbers.txt"):
    if not os.path.exists(filename):
        print(f"⚠️ File not found: {filename}")
        return

    with open(filename, "r") as file:
        numbers = [line.strip() for line in file if line.strip()]

    print(f"🔢 Calling {len(numbers)} numbers...")
    for number in numbers:
        make_call(number)
        time.sleep(2)  # ⏱ Delay to stay under Twilio rate limits

if __name__ == "__main__":
    call_all_numbers()
