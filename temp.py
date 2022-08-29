from pprint import pprint as pp

import requests

chat_id = '283297550'
token = '5623317177:AAHyQusIxfra93r9rrKdWZCP_MKDc5hL9OA'

text = 'Тестовое сообщение от чат-бота'

# Отправка ботом сообщения пользователю
# send_msg_url = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id='
#                 f'{chat_id}&text={text}')
# response = requests.get(send_msg_url)

# Запрос сообщений, направленных боту
polling_req = f'https://api.telegram.org/bot{token}/getUpdates'
polling_response = requests.get(polling_req)
pp(polling_response.json())
