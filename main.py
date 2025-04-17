from flask import Flask, request
import os
import requests

app = Flask(__name__)
TOKEN = os.getenv("TELEGRAM_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"

def send_message(chat_id, text):
    requests.post(f"{URL}/sendMessage", json={"chat_id": chat_id, "text": text})

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if text == "/start":
            send_message(chat_id, "Привет! Я бот питания от ТРЕЗВО.")
        else:
            send_message(chat_id, f"Ты написал: {text}")
    return {"ok": True}

@app.route('/')
def index():
    return "Bot is running!"

if __name__ == '__main__':
    app.run(debug=True)
