
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
# 1549962000

url = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
headers = {'Authorization': f'OAuth {token_practicum}'}
payload = {'from_date': then_unix}

homework_statuses = requests.get(url, headers=headers, params=payload)
pprint(homework_statuses.json())
