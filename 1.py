
import codecs
f=codecs.open("archives/facebook-justinyan33/messages/1558163894202144.html", 'r', encoding='utf-8')

from bs4 import BeautifulSoup
soup = BeautifulSoup(f.read(), 'html.parser')
print(soup.prettify())