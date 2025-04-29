import os
from twilio.rest import Client
from dotenv import load_dotenv
import requests
from elevenlabs_voice import generate_mp3

# Load environment variables
load_dotenv()

# Grab Twilio credentials
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_PHONE_NUMBER')

# Initialize Twilio client
client = Client(account_sid, auth_token)

def upload_file(file_path):
    with open(file_path, "rb") as f:
        response = requests.put(f'https://transfer.sh/{os.path.basename(file_path)}', data=f)
        if response.status_code == 200:
            file_url = response.text.strip()
            print(f"Uploaded MP3 at {file_url}")
            return file_url
        else:
            raise Exception(f"Upload failed: {response.status_code} - {response.text}")

def make_call(to_number):
    # Step 1: Generate the mp3 file with real human voice
    text = (
        "Hey there! This is Mike from XYZ Blinds. "
        "I'm reaching out to offer you a special fifty dollar discount on professional blind installation. "
        "If you're interested, press 1 on your keypad now, and we'll get you all set up!"
    )
    mp3_file = generate_mp3(text)

    # Step 2: Upload the mp3 file
    file_url = upload_file(mp3_file)

    # Step 3: Make the call using the uploaded MP3
    call = client.calls.create(
        to=to_number,
        from_=twilio_number,
        twiml=f'''
<Response>
  <Play>{file_url}</Play>
  <Gather numDigits="1" timeout="6" action="https://webhook.site/your-fake-endpoint" method="POST" />
</Response>
'''
    )
    print(f"Call initiated: {call.sid}")
