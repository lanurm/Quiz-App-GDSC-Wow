import requests


url = 'http://localhost:5000/update/'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

print(x.text)
