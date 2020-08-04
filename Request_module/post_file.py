import requests

url = "https://httpbin.org/post"
files = {'files': open( 'Computer list.csv', 'r' )}
r1 = requests.post( url, files=files )
print( r1.text )
print( r1.status_code )
