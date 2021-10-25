import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"nama": "Gilang", "usia": 20},
    {"nama": "Kangketik", "usia": 21},
    {"nama": "Random Guy", "usia": 30},
]

for i in range(len(data)):
    resonse = requests.patch(BASE + "karyawan/" + str(i), data[i])
    print(resonse.json())

input()
resonse = requests.get(BASE + "karyawan/")
print(resonse)
input()
resonse = requests.get(BASE + "karyawan/1")
print(resonse.json())
input()
response = requests.delete(BASE + "karyawan/0")
print(resonse.json())
