import codecs
import sys
fileNum = sys.argv[1]
f=codecs.open("archives/facebook-justinyan33/messages/"+fileNum+".html", 'r', encoding='utf-8')

from bs4 import BeautifulSoup
soup = BeautifulSoup(f.read(), 'html.parser')
title = soup.title.string
friendName = title[18:]
prettySoup = soup.prettify()
print(prettySoup)
