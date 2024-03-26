import requests

url = "https://api.github.com"
response = requests.get(url)
print(response)

head = response.headers
print(head)

cont = response.content
print(cont)

head_cont = response.headers['Content-Type']
print(head_cont)

server_type = response.headers['Server']
print(server_type)

Date_added = response.headers['Date']
print(Date_added)

txt = response.text
print(txt)

json_cont = response.json
print(json_cont)

