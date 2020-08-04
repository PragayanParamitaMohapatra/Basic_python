import requests

url = "https://api.github.com/events"
res = requests.get( url )
r1 = res.json()
print( r1[0]['id'] )
