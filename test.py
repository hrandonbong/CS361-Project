import requests

BASE = " http://127.0.0.1:5000/"

#Adding to our database
response = requests.put(BASE + "shopping/1",{"name": "A message from CS361"})
print(response.json())
input()

#Grabbing from our database
response = requests.get(BASE + "shopping/1")
print(response.json())