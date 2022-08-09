import requests

URL =  "https://jsonplaceholder.typicode.com/users"

respuesta = requests.get(URL)
print(respuesta.text)