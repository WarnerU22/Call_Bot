# 📞 Call_Bot – Automated AI Phone Call System

This project lets you automatically call a list of phone numbers using Twilio, play a realistic AI-generated voice message, and log interested leads when someone presses `1`.

---

## 🚀 Features

- Make outbound calls to multiple numbers.
- Play a high-quality, pre-recorded voice message.
- Log interested leads to `leads.txt` if the user presses `1`.
- Simple setup using Twilio, Flask, and ngrok.

---

## 📁 Project Structure

```
Call_Bot/
│
├── call_handler.py       # Flask app handling voice routes
├── bulk_caller.py        # Script that triggers bulk calls
├── message.mp3           # Local audio file played during the call
├── numbers.txt           # List of numbers to call
├── leads.txt             # Stores numbers that press 1
├── calls.log             # Optional log of all call attempts
├── .env                  # Environment variables (Twilio + ngrok)
└── README.md             # This file
```

---

## 🔧 Setup Guide

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Call_Bot.git
cd Call_Bot
```

### 2. Install Required Packages
```bash
pip install twilio flask python-dotenv
```

### 3. Create `.env` File
Create a file named `.env` in the root directory with:

```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1XXXXXXXXXX
NGROK_PUBLIC_URL=https://your-ngrok-subdomain.ngrok-free.app
```

> 🔑 Get your credentials at https://twilio.com/console  
> 🌐 Get a public URL using [ngrok](https://ngrok.com/download):
```bash
./ngrok http 5000
```

---

## 🎵 Add a Voice Message

Place your AI-generated audio message in the root folder and name it:

```
message.mp3
```

You can generate one using tools like [ElevenLabs.io](https://elevenlabs.io) or any TTS platform.

---

## 📞 How to Make Calls

### Step 1: Start the Flask App
```bash
python call_handler.py
```

This runs the server that Twilio interacts with.

### Step 2: Add Phone Numbers

Open or create `numbers.txt` and add numbers in E.164 format (one per line):

```
+16175551234
+14045557890
+18557402065
```

### Step 3: Run the Bulk Caller
```bash
python bulk_caller.py
```

This reads numbers from `numbers.txt` and makes the calls.

---

## ✅ What Happens During a Call

1. The recipient receives a call from your Twilio number.
2. The `message.mp3` file plays.
3. If they press `1`, their number is saved to `leads.txt`.

---

## 🧪 How to Test

- Add your own number to `numbers.txt`.
- Run both `call_handler.py` and `bulk_caller.py`.
- Answer the call, listen to the message, press `1`.
- Check `leads.txt` to confirm your number was recorded.

---

## 📄 Output Files

- `leads.txt`: Contains phone numbers that pressed `1`.
- `calls.log`: Optional file that logs all call attempts and SIDs.

---

## ⚠️ Important Notes

- Twilio trial accounts can only call verified numbers.
- Add a delay (`time.sleep`) between calls to avoid rate limits.
- Be compliant with robocall laws (e.g., TCPA in the U.S.).
- Don’t use for spam or without recipient consent.

---

## 🔮 Future Ideas

- Add retry logic for failed calls.
- Visual dashboard or Google Sheets integration.
- Automatic SMS follow-up.
- CRM/webhook sync.

---

## 👨‍💻 Tech Stack

- Python 3
- Flask
- Twilio Voice API
- ngrok for local tunneling

---

## 📬 Questions?

Fork, contribute, or open an issue if you have questions or ideas!
