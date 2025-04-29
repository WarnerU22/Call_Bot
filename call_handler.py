import os
from twilio.rest import Client
from dotenv import load_dotenv
from flask import Flask, request, Response

# Load environment variables
load_dotenv()

# Twilio setup
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_PHONE_NUMBER')
client = Client(account_sid, auth_token)

# Flask app setup
app = Flask(__name__)

# Your uploaded human voice MP3
mp3_url = "https://limewire.com/d/8MdA4#x4RWDku9Iv"

# Your public ngrok URL (with /voice at the end)
public_ngrok_url = "https://184f-2600-6c5d-f0-a620-b824-60f4-5646-b6a2.ngrok-free.app/voice"

def make_call(to_number):
    call = client.calls.create(
        to=to_number,
        from_=twilio_number,
        url=public_ngrok_url
    )
    print(f"Call initiated: {call.sid}")

@app.route("/voice", methods=["POST"])
def voice():
    from twilio.twiml.voice_response import VoiceResponse, Gather

    response = VoiceResponse()
    gather = Gather(num_digits=1, action="/gather", method="POST", timeout=6)
    gather.play(mp3_url)
    response.append(gather)
    return Response(str(response), mimetype="application/xml")

@app.route("/gather", methods=["POST"])
def gather():
    from twilio.twiml.voice_response import VoiceResponse

    digits = request.form.get("Digits")
    from_number = request.form.get("From")
    response = VoiceResponse()

    if digits == "1":
        save_lead(from_number)
        response.say("Thank you! We've recorded your interest. Someone will contact you soon.")
    else:
        response.say("No problem. Thanks for your time!")
    
    return Response(str(response), mimetype="application/xml")

def save_lead(phone_number):
    with open("leads.txt", "a") as f:
        f.write(f"{phone_number}\n")
    print(f"Saved lead: {phone_number}")
