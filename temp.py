from pprint import pprint as pp

import requests

from data import chat_id_me, token

chat_id = chat_id_me

text = 'Тестовое сообщение от чат-бота'

# Отправка ботом сообщения пользователю
# send_msg_url = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id='
#                 f'{chat_id}&text={text}')
# response = requests.get(send_msg_url)

# Запрос сообщений, направленных боту

polling_req = f'https://api.telegram.org/bot{token}/getUpdates'
polling_response = requests.get(polling_req)
pp(polling_response.json())
