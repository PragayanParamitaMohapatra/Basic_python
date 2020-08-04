import requests

r = requests.get( "https://github.com" )
print( r.url )
print( r.status_code )
print( r.history )
