import requests

url = "https://httpbin.org/post"
data = {"Firstname": "john", "lastname": "smith"}
response = requests.post( url, data=data )
print( response.text )
print( response.status_code )
