from requests import get
from bs4 import BeautifulSoup
url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)
soup=BeautifulSoup(response.content,'html.parser')
# print(response.text[:500])
# print(soup.prettify())
movie=soup.find_all('div',class_='lister-item mode-advanced')
print(movie)
print(len(movie))
print(type(movie))