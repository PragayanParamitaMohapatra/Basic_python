import requests

header = {'content-type': 'multipart/form-data'}
r = requests.post( 'https://httpbin.org/post', headers=header )
print( r.status_code )
print( r.request.headers )
print( r.headers['content-type'] )
