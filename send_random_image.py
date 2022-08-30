import requests
from telegram import Bot

from data import chat_id_me, token

bot = Bot(token=token)
URL = 'https://api.thecatapi.com/v1/images/search'
chat_id = chat_id_me

response = requests.get(URL).json()
random_cat_url = response[0].get('url')

bot.send_photo(chat_id, random_cat_url)
