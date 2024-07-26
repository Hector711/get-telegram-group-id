import requests

# Reemplaza 'YOUR_BOT_TOKEN' con el token de tu bot
bot_token = 'YOUR_BOT_TOKEN'
url = f'https://api.telegram.org/bot{bot_token}/getUpdates'

params = {'limit': 100, 'offset': -100}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if data['ok']:
        if data['result']:
            for result in data['result']:
                if 'message' in result:
                    chat = result['message']['chat']
                elif 'my_chat_member' in result:
                    chat = result['my_chat_member']['chat']
                else:
                    continue  # Saltar esta actualización si no tiene la información que necesitamos

                chat_id = chat['id']
                chat_type = chat['type']
                
                if chat_type in ['group', 'supergroup']:
                    chat_title = chat['title']
                    print(f"Grupo encontrado - ID: {chat_id}, Título: {chat_title}")
                elif chat_type == 'private':
                    print(f"Chat individual encontrado - ID: {chat_id}")
        else:
            print("No se encontraron resultados en la respuesta.")
    else:
        print(f"La respuesta no fue exitosa. Código de error: {data.get('error_code')}, Descripción: {data.get('description')}")

except requests.exceptions.RequestException as e:
    print(f"Error al hacer la solicitud: {e}")
except KeyError as e:
    print(f"Error al procesar la respuesta: {e}")
    print(f"Estructura de la respuesta: {data}")