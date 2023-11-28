import requests


endpoint = "https://httpbin.org/anything"
get_request = requests.get(endpoint)

print(get_request.json())
