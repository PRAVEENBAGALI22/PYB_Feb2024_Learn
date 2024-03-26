import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
response.raise_for_status()
joke_data = response.json()
print(joke_data)

joke_value = joke_data['value']
print(joke_value)
