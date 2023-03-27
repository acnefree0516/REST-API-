import requests

response = requests.get('http://localhost:5000/meminfo')

if response.status_code == 200:
    data = response.json()
    print(data)

else:
    print('error', response.status_code)
