from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
import os

app = Flask(__name__)

# URL to your hosted MP3 file
mp3_url = "https://your-public-mp3-link.com/output.mp3"  # Replace with your actual URL

@app.route("/voice", methods=["GET", "POST"])
def voice():
    response = VoiceResponse()
    gather = response.gather(num_digits=1, action="/gather", method="POST")
    gather.play(mp3_url)
    return Response(str(response), mimetype="text/xml")

@app.route("/gather", methods=["GET", "POST"])
def gather():
    digit_pressed = request.values.get("Digits", "")
    caller_number = request.values.get("From", "")
    response = VoiceResponse()

    if digit_pressed == "1" and caller_number:
        with open("leads.txt", "a") as f:
            f.write(f"{caller_number}\n")
        response.say("Thank you. We will contact you shortly.")
    else:
        response.say("Thank you for your time.")

    return Response(str(response), mimetype="text/xml")
