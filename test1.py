from bson import encode
import requests
import json

html = requests.get('https://reqres.in/api/users')
html_jd = html.json()
i = 0
for title in html_jd['data']:
    print (title['first_name'])
