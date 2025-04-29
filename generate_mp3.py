from elevenlabs import generate, save, set_api_key

set_api_key("sk_d7b01a01dc7e3b1ab5e2fdd74f03c96f251696c6a3392e53")  # Replace with yours

text = (
    "Hey, this is Rachel from Clarksville Blinds. "
    "We have a $50 coupon for blind installation. "
    "If you're interested, press 1 so an associate can reach out to you. Thank you."
)

audio = generate(
    text=text,
    voice="21m00Tcm4TlvDq8ikWAM",  # Or "21m00Tcm4TlvDq8ikWAM" (default voice ID)
    model="eleven_monolingual_v1"
)

save(audio, "output.mp3")
