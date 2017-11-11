import codecs
f=codecs.open("archives/facebook-justinyan33/messages/1558163894202144.html", 'r', encoding='utf-8')

from bs4 import BeautifulSoup
soup = BeautifulSoup(f.read(), 'html.parser')
title = soup.title.string
friendName = title[18:]
prettySoup = soup.prettify()
listTimes = soup.body.findAll("div", { "class" : "message_header" })

index = codecs.open("archives/facebook-justinyan33/index.htm", 'r', encoding='utf-8')
soup2 = BeautifulSoup(index.read(), 'html.parser')
myName = soup2.title.string
myName = myName[:len(myName)-10]

for msg in listTimes:
	print(msg.find("span",{ "class" : "user" }).getText(), ": ", msg.find("span",{ "class" : "user" }).getText() == myName)
	print(msg.find("span",{ "class" : "meta" }).getText())
print(myName, ": You have talked to " + friendName + " " +str(len(listTimes)) + " times.")

