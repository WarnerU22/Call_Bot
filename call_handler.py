import os
from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Gather
from twilio.rest import Client
from dotenv import load_dotenv

# Load .env values
load_dotenv()

# Twilio credentials and numbers
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
public_ngrok_url = os.getenv("NGROK_PUBLIC_URL")

client = Client(account_sid, auth_token)

# Flask app
app = Flask(__name__)

# 🔊 Replace this with your public .mp3 link
mp3_url = "https://files.catbox.moe/13g4pq.mp3"

# Call trigger function
def make_call(to_number):
    call = client.calls.create(
        to=to_number,
        from_=twilio_number,
        url=f"{public_ngrok_url}/voice"
    )
    print(f"📞 Call started: {call.sid}")

# Voice response route
@app.route("/voice", methods=["POST"])
def voice():
    response = VoiceResponse()
    gather = Gather(num_digits=1, action="/gather", method="POST")
    gather.play(mp3_url)
    response.append(gather)
    return Response(str(response), mimetype="application/xml")

# Handle input (press 1)
@app.route("/gather", methods=["POST"])
def gather():
    digits = request.form.get("Digits")
    from_number = request.form.get("From")
    response = VoiceResponse()

    if digits == "1":
        with open("leads.txt", "a") as f:
            f.write(f"{from_number}\n")
        response.say("Thanks! We’ll reach out to you shortly.")
    else:
        response.say("No problem. Thank you for your time.")

    return Response(str(response), mimetype="application/xml")

# Run the Flask app if executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

