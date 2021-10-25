import requests

BASE = "http://127.0.0.1:5000/"

resonse = requests.get(BASE + "helloworld/gilang")

print(resonse.json())
