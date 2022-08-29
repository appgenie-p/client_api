from telegram import Bot
from telegram.ext import Updater

token = '5623317177:AAHyQusIxfra93r9rrKdWZCP_MKDc5hL9OA'
chat_id = 283297550

bot = Bot(token=token)
updater = Updater(token=token)

text = 'Вам телеграмма!'
bot.send_message(chat_id, text)
