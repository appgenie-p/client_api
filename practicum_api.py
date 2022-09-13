
import requests
import time
import datetime

import os

from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

token_practicum = os.environ['TOKEN_PRACTICUM']


now = datetime.datetime.now()
now_unix = int(time.mktime(now.timetuple()))
then = now - datetime.timedelta(days=60)
then_unix = int(time.mktime(then.timetuple()))

url = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
headers = {'Authorization': f'OAuth {token_practicum}'}
payload = {'from_date': 0}

homework_statuses = requests.get(url, headers=headers, params=payload)
answer = homework_statuses.json()
pass