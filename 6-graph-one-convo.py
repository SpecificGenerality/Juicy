import codecs
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from dateutil import parser
import time
import numpy as np
from scipy.interpolate import spline

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


def plotLine(lists):
	x, y = zip(*lists) # unpack a list of pairs into two tuples

	# x_sm = np.array(x)
	# y_sm = np.array(y)

	# x_smooth = np.linspace(x_sm.min(), x_sm.max(), 200)
	# y_smooth = spline(x, y, x_smooth)

	# plt.plot(x, y, 'o', x_smooth, y_smooth, '--')
	plt.plot(x,y)
	# plt.plot(x_smooth, y_smooth)

            
f=codecs.open("archives/facebook-justinyan33/messages/1552427911482250.html", 'r', encoding='utf-8')

soup = BeautifulSoup(f.read(), 'html.parser')
title = soup.title.string
friendName = title[18:]
listTimes = soup.body.findAll("div", { "class" : "message_header" })

index = codecs.open("archives/facebook-justinyan33/index.htm", 'r', encoding='utf-8')
soup2 = BeautifulSoup(index.read(), 'html.parser')
myName = soup2.title.string
myName = myName[:len(myName)-10]

c = Convo(friendName)
print("friend: "+friendName)

for msg in listTimes:
	is_me = msg.find("span",{ "class" : "user" }).getText() == myName
	datestr = msg.find("span",{ "class" : "meta" }).getText()
	date = parser.parse(datestr)
	timestamp = int(time.mktime(date.timetuple()))
	week = int(timestamp/(60*60*24))*(60*60*24)
	if is_me:
		c.updateSent(week)
	else:
		c.updateReceived(week)

print("You have talked to " + friendName + " " +str(len(listTimes)) + " times.")

plotLine(sorted(c.sent.items()))
plotLine(sorted(c.received.items())) # sorted by key, return a list of tuples
ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_scientific(False)
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.show()