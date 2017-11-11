import codecs
f=codecs.open("archives/facebook-justinyan33/messages/1558163894202144.html", 'r', encoding='utf-8')

from bs4 import BeautifulSoup
soup = BeautifulSoup(f.read(), 'html.parser')
title = soup.title.string
friendName = title[18:]
prettySoup = soup.prettify()
listTimes = soup.body.findAll(text = friendName)

print("You have talked to " + friendName + " " +str(len(listTimes)) + " times.")
print(soup.prettify())
