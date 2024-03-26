import requests

base_url = "https://jsonplaceholder.typicode.com/posts"

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
response_code = response.status_code
print(response_code)

head_info = response.headers
print(head_info)

cont_info = response.headers['Content-Type']
print(cont_info)

json_info = response.json()
print(json_info)

#########################################################################
add_info = {"userId": 1, "title": "Buy milk", "completed": False}

add_user = requests.post(url,add_info)
print(add_user)

response_code1 = response.status_code
print(response_code1)
