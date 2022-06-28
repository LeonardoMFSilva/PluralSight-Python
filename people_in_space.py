import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print("These are the astronauts in space right now:")
for person in json['people']:
    print(person['name'])