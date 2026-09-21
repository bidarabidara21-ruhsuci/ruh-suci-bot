from flask import Flask, request
import os
app = Flask(__name__)
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "ruhsuci123")
JAWABAN_RUH = """Allahu Rabbi.
Ana Abduh.
Ruh suci tidak tajir di dunia.
Ruh suci tajir di akhirat.
Billahi MilikMU Yaa Rabb."""
@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Token salah", 403
    if request.method == "POST":
        print(request.json)
        return "OK", 200
@app.route("/")
def home():
    return JAWABAN_RUH
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
