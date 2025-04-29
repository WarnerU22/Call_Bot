import os
import requests
from dotenv import load_dotenv

load_dotenv()

eleven_api_key = os.getenv("ELEVENLABS_API_KEY")
voice_id = os.getenv("ELEVENLABS_VOICE_ID", "EXAVITQu4vr4xnSDxMaL")  # default to 'Rachel' voice

def generate_mp3(text, filename="output.mp3"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": eleven_api_key,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Generated {filename} successfully!")
        return filename
    else:
        raise Exception(f"Failed to generate MP3: {response.status_code} - {response.text}")
