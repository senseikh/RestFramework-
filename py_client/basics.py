import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "http://localhost:8000/"


get_response = requests.get(endpoint, json={"the":"word"})
print(get_response.status_code)
