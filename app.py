from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Получаем токен и chat_id из переменных окружения
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
MY_CHAT_ID = os.environ.get('MY_CHAT_ID')

def send_to_telegram(text):
    print("=== send_to_telegram called ===")
    if not TELEGRAM_TOKEN or not MY_CHAT_ID:
        print("⛔️ Отсутствует TELEGRAM_TOKEN или MY_CHAT_ID")
        return

    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {
        'chat_id': MY_CHAT_ID,
        'text': text
    }
    print("Telegram URL:", url)
    print("Telegram data:", data)
    try:
        response = requests.post(url, data=data)
        print("Telegram response:", response.status_code, response.text)
    except Exception as e:
        print("⛔️ Ошибка отправки в Telegram:", e)


# def send_to_telegram(text):
#     print("=== send_to_telegram called ===")
#     print("TELEGRAM_TOKEN:", TELEGRAM_TOKEN)
#     print("MY_CHAT_ID:", MY_CHAT_ID)
#     url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
#     data = {
#         'chat_id': MY_CHAT_ID,
#         'text': text
#     }
#     print("Telegram URL:", url)
#     print("Telegram data:", data)
#     response = requests.post(url, data=data)
#     print("Telegram response:", response.status_code, response.text)

@app.route('/whatsapp-incoming', methods=['POST'])
def whatsapp_webhook():
    try:
        data = request.json()
        print("=== Webhook data received ===")
        print(data)
    except Exception as e:
        print("⛔️ Ошибка при чтении JSON:", e)
        return jsonify({"status": "invalid json"}), 400
        
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok", "message": "сервер работает"})
    
# @app.route('/whatsapp-incoming', methods=['POST'])
# def whatsapp_webhook():
#     data = request.json
#     print("=== Webhook data received ===")
#     print(data)
#     msg = data.get("message", "" )
#     phone = data.get("from", "")

#     print("From:", phone)
#     print("Message:", msg)

#     if phone and msg:
#         text = f"📩 Новое сообщение из WhatsApp:\nОт: {phone}\nТекст: {msg}"
#         send_to_telegram(text)
#         return jsonify({"status": "ok"})
#     else:
#         print("⛔️ Не хватает данных в JSON")
#         return jsonify({"status": "missing data"}), 400

# Render запускает сервер так
if __name__ == '__main__':
    print("🚀 Flask-сервер запускается...")
    port = int(os.environ.get('PORT', 10000))
    print(f"Слушаем порт: {port}")
    app.run(host='0.0.0.0', port=port)
