# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:48:34 2017

@author: Justin Yan
"""

class Friend:
    def __init__(self, name):
        self.name = name
        self.messages = {}
        
    def update(self, week, number):
        self.messages[week] = number
        
