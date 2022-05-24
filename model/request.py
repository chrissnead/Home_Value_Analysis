import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Square Feet':1400, 'Zip Code':97214})

print(r.json())