import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(f'https://itunes.apple.com/search?entity=song&limit=10&term={sys.argv[1]}')

json_res = response.json()
for result in json_res['results']:
    print(result['trackName'])
