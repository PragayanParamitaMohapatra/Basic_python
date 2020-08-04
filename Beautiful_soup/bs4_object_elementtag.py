
from bs4 import BeautifulSoup
soup=BeautifulSoup("<p class='bold'>Guddi is a good girl</p>")
print(soup)
tag=soup.p
print(type(tag))