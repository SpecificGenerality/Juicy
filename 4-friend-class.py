# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:48:34 2017

@author: Justin Yan
"""
class Me:
    def __init(self, name):
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
        self.sent[week] += 1
            
    def updateReceived(self, week):
        self.received[week] += 1
            
