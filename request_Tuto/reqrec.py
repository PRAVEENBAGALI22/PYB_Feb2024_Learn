import requests

url = "https://reqres.in/"
response = requests.get(url)
response_code = response.status_code
print(response_code)

cont = response.headers['Content-Type']
print(cont)

info = response.text
print(info)