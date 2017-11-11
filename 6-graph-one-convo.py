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
prettySoup = soup.prettify()
listTimes = soup.body.findAll("div", { "class" : "message_header" })

for msg in listTimes:
	is_me = msg.find("span",{ "class" : "user" }).getText() != friendName
	datestr = msg.find("span",{ "class" : "meta" }).getText()
	date = parser.parse("Tuesday, October 17, 2017 at 6:17pm EDT")
	timestamp = int(time.mktime(date.timetuple()))
	week = int(timestamp/(60*60*24*7))*(60*60*24*7)
	print(week)
print("You have talked to " + friendName + " " +str(len(listTimes)) + " times.")
