import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Square Feet':1400, 'Zip Mean HHI':75000, 'Zip Pop Density':200,'Lot Size':2400,'Bed':3,'Bath':2,'Year Built':1991})

print(r.json())