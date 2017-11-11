import codecs
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from dateutil import parser
import time

class Convo:
    def __init__(self, name):
        self.name = name
        self.sent = {}
        self.received = {}
        
    def updateSent(self, week):
        if week in self.sent:
            self.sent[week] += 1
        else:
            self.sent[week] = 1
            
    def updateReceived(self, week):
        if week in self.received:
            self.received[week] += 1
        else:
            self.received[week] = 1
            
f=codecs.open("archives/facebook-justinyan33/messages/1558163894202144.html", 'r', encoding='utf-8')

soup = BeautifulSoup(f.read(), 'html.parser')
title = soup.title.string
friendName = title[18:]
listTimes = soup.body.findAll("div", { "class" : "message_header" })

index = codecs.open("archives/facebook-justinyan33/index.htm", 'r', encoding='utf-8')
soup2 = BeautifulSoup(index.read(), 'html.parser')
myName = soup2.title.string
myName = myName[:len(myName)-10]

c = Convo(friendName)

for msg in listTimes:
	is_me = msg.find("span",{ "class" : "user" }).getText() == myName
	datestr = msg.find("span",{ "class" : "meta" }).getText()
	date = parser.parse(datestr)
	timestamp = int(time.mktime(date.timetuple()))
	week = int(timestamp/(60*60*24*7))*(60*60*24*7)
	if is_me:
		c.updateSent(week)
	else:
		c.updateReceived(week)

print("You have talked to " + friendName + " " +str(len(listTimes)) + " times.")

lists = sorted(c.received.items()) # sorted by key, return a list of tuples

x, y = zip(*lists) # unpack a list of pairs into two tuples

plt.plot(x, y)
plt.show()