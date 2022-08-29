from pprint import pprint as pp

import requests

response = requests.get('https://api.github.com')

pp(
    response.status_code
)