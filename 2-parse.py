import codecs
f=codecs.open("archives/facebook-justinyan33/messages/1558163894202144.html", 'r', encoding='utf-8')

from bs4 import BeautifulSoup
soup = BeautifulSoup(f.read(), 'html.parser')
title = soup.title.string
friendName = title[18:]
prettySoup = soup.prettify()
listTimes = soup.body.findAll("div", { "class" : "message_header" })

for msg in listTimes:
	print(msg.find("span",{ "class" : "user" }).getText(), ": ", msg.find("span",{ "class" : "user" }).getText() == friendName)
	print(msg.find("span",{ "class" : "meta" }).getText())
print("You have talked to " + friendName + " " +str(len(listTimes)) + " times.")
