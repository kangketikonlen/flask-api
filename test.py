import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"nama": "Gilang", "usia": 25},
    {"nama": "Kangketik", "usia": 25},
    {"nama": "Random Guy", "usia": 25},
]

for i in range(len(data)):
    resonse = requests.put(BASE + "karyawan/"+str(i), data[i])
    print(resonse.json())

input()
response = requests.delete(BASE + "karyawan/0")
print(resonse.json())
input()
resonse = requests.get(BASE + "karyawan/1")
print(resonse.json())
