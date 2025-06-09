from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Получаем токен и chat_id из переменных окружения
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
MY_CHAT_ID = os.environ.get('MY_CHAT_ID')

def send_to_telegram(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {
        'chat_id': MY_CHAT_ID,
        'text': text
    }
    print("Telegram URL:", url)
    print("Telegram data:", data)
    response = requests.post(url, data=data)
    print("Telegram response:", response.status_code, response.text)

@app.route('/whatsapp-incoming', methods=['POST'])
def whatsapp_webhook():
    data = request.json
    msg = data.get("message", "" )
    phone = data.get("from", "")

    text = f" Новое сообщение из WhatsApp: \nОт: {phone}\nТекст: {msg}"
    send_to_telegram(text)
    return {'status': 'ok'}

# Render запускает сервер так
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
