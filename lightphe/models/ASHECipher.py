# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 00:12:09 2024

@author: Christian

Java-Original from Cuttlefish https://github.com/ssavvides/cuttlefish by Savvas Savvides
"""

class ASHECipher():
    #v=0
    
    
    def __init__(self, v: int, ids):
        self.ids=set()
        if isinstance(ids,int):
            self.generateIds(ids)
        else:
            self.ids=ids
        self.v = v
    
    def generateIds(self, sid: int=1):
        self.ids.add(sid)