from call_handler import app, make_call

if __name__ == "__main__":
    make_call("+19313345875")  # <-- your real phone number
    app.run(host="0.0.0.0", port=5000, debug=True)

