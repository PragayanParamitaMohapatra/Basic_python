import requests

url = "https://httpbin.org/get"
payload = {"firstname": "smit"}
response = requests.get( url, params=payload )
print( response.text )
print( response.status_code )
print( response.content )
