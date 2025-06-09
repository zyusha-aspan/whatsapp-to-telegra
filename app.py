from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Получаем токен и chat_id из переменных окружения
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
MY_CHAT_ID = os.environ.get('MY_CHAT_ID')

def send_to_telegram(text)
    url = f'httpsapi.telegram.orgbot{TELEGRAM_TOKEN}sendMessage'
    data = {
        'chat_id' MY_CHAT_ID,
        'text' text
    }
    requests.post(url, data=data)

@app.route('whatsapp-incoming', methods=['POST'])
def whatsapp_webhook()
    data = request.json
    msg = data.get(message, )
    phone = data.get(from, )

    text = f📩 Новое сообщение из WhatsAppnОт {phone}nТекст {msg}
    send_to_telegram(text)
    return {'status' 'ok'}

# Render запускает сервер так
if __name__ == '__main__'
    app.run(host='0.0.0.0', port=10000)
