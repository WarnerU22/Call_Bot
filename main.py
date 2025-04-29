from call_handler import app, make_call

if __name__ == "__main__":
    # Make the first call manually
    make_call("+19313345875")  # <-- Put YOUR phone number or a customer's number here
    app.run(host="0.0.0.0", port=5000, debug=True)

