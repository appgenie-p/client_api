from pprint import pprint

import requests

# response = requests.get('https://swapi.dev/api/people/')
# res_lst = response.json()['results']

# response = requests.get('https://swapi.dev/api/people/?search=Luke')
# res_luke = response.json() 

response = requests.get('https://swapi.dev/api/planets/1/')
res_luke = response.json()['diameter']
pass