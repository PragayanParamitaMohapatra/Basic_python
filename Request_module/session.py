import requests

s = requests.Session()
username = {"userName": "John"}
location = {"Location": "Bangalore"}
setCookieUrl = "https://httpbin.org/cookies/set"
getCookieUrl = "https://httpbin.org/cookies"
s.get( setCookieUrl, params=username )
s.get( setCookieUrl, params=location )
print( s.get( getCookieUrl ) )
