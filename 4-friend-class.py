# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:48:34 2017

@author: Justin Yan
"""

import matplotlib.pyplot as plt

class Me:
    def __init__(self, name):
        self.name = name
        self.convos = []
        
    def addConvo(self, convo):
        self.convos.append(convo)
        
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
            

myself = Me("bessie")

c = Convo("elsie")
c.updateSent(0)
c.updateSent(1)
c.updateSent(1)
c.updateSent(3)

myself.addConvo(c)

print(c.sent)
print(myself.convos)

lists = sorted(c.sent.items()) # sorted by key, return a list of tuples

x, y = zip(*lists) # unpack a list of pairs into two tuples

plt.plot(x, y)
plt.show()