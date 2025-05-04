from call_handler import app, make_call

if __name__ == "__main__":
    try:
        print("📞 Attempting to make call...")
        make_call("+19313345875")  # Replace with your number
        print("✅ Call triggered successfully.")
    except Exception as e:
        print(f"❌ Error while making call: {e}")

    app.run(host="0.0.0.0", port=5000)
