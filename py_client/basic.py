import requests


endpoint = "http://localhost:5000/api/"
get_request = requests.get(endpoint)

print(get_request.json())
