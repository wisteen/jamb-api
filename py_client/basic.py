import requests

url = 'http://localhost:5000/api/'

headers = {'Authorization': 'Token 10bcbad3a4d26cf3ab57dc004c8a72829092979c'}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())