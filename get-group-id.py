import requests

# Reemplaza 'YOUR_BOT_TOKEN' con el token de tu bot
bot_token = 'YOUR_BOT_TOKEN'
url = f'https://api.telegram.org/bot{bot_token}/getUpdates'

response = requests.get(url)
data = response.json()

for result in data['result']:
    chat_id = result['message']['chat']['id']
    chat_title = result['message']['chat']['title']
    print(f"Chat ID: {chat_id}, Chat Title: {chat_title}")
