import requests
import updatedb
from flask import Flask, jsonify, request

url = 'http://localhost:5000/update/'
urll = 'http://localhost:5000/leaderboard/'
myobj = {'somekey': 'somevalue'}
data = {"name": "bor", "email": "killme", "score": 69, "time": 432}

# print(updatedb.retrieve_leaderboard())

# x = requests.post(url, json = data)

# print(x.text)

print(requests.get(urll).text)

# updatedb.updatedb("iwanttodie", "plskillme@gmail.com", 69, 420)

# print(jsonify(updatedb.retrieve_leaderboard()))

