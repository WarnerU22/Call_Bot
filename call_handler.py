from flask import Flask, request, Response, send_from_directory
from twilio.twiml.voice_response import VoiceResponse, Gather
import os

app = Flask(__name__)

# Path to your local MP3 file
mp3_file = "message.mp3"

# Serve the MP3 file from the local directory
@app.route("/audio/<filename>")
def audio(filename):
    return send_from_directory(os.getcwd(), filename)

# Serve TwiML for incoming calls
@app.route("/voice", methods=["POST"])
def voice():
    response = VoiceResponse()
    gather = Gather(num_digits=1, action="/gather", method="POST")
    gather.play(f"{request.host_url}audio/{mp3_file}")  # Local MP3 file
    response.append(gather)
    return Response(str(response), mimetype="application/xml")

# Handle user input (pressing 1)
@app.route("/gather", methods=["POST"])
def gather():
    digits = request.form.get("Digits")
    from_number = request.form.get("From")  # This is where we capture the caller's phone number
    response = VoiceResponse()

    if digits == "1":
        with open("leads.txt", "a") as f:
            f.write(f"{from_number}\n")  # Save the correct phone number to leads.txt
        response.say("Thanks! We’ll reach out to you shortly.")
    else:
        response.say("No problem. Thank you for your time.")
    
    return Response(str(response), mimetype="application/xml")

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
