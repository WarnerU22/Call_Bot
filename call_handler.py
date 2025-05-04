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
    
    # Log all incoming request data for debugging
    print("Request data:", request.form)
    
    # The number the customer called (this should be the actual number calling your Twilio number)
    called_number = request.form.get("Called")  # This should now be the correct number
    response = VoiceResponse()

    # Log the called number to verify it is the correct customer number
    print(f"Received call from customer number: {called_number}")

    if digits == "1":
        # Check if 'called_number' is correctly received
        if called_number:
            # Write the customer's number to leads.txt
            with open("leads.txt", "a") as f:
                f.write(f"{called_number}\n")  # Save the correct phone number to leads.txt
            print(f"Customer's phone number {called_number} saved to leads.txt.")  # Confirmation in the terminal
            response.say("Thanks! We’ll reach out to you shortly.")
        else:
            print("Error: 'called_number' is empty.")  # This will help us debug if something's wrong
            response.say("Sorry, we could not capture your phone number.")
    else:
        response.say("No problem. Thank you for your time.")
    
    return Response(str(response), mimetype="application/xml")

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
