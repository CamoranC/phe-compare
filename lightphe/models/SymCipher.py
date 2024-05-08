# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 17:02:39 2024

@author: Christian

Java-Original from Symmetria https://github.com/ssavvides/symmetria by Savvas Savvides
"""

class SymCipher():
    #v=0
    
    
    def __init__(self, v: int, idsp, idsn):
        self.idsp=[]
        if isinstance(idsp,int):
            self.generateIds(idsp)
        else:
            self.idsp=idsp
        self.v = v
        self.idsn=idsn
    
    def generateIds(self, sid: int=1):
        self.idsp.append(sid)
        
    def add(self, sc, n: int=128):
        v3 = (self.v + sc.v)%n
        lp3=[]
        lp3.extend(self.idsp)
        lp3.extend(sc.idsp)
        ln3=[]
        ln3.extend(self.idsn)
        ln3.extend(sc.idsn)
        return SymCipher(v3,lp3,ln3)
    
    def mult(self, sc, n: int=128):
        v3 = (self.v * sc.v)%n
        lp3=[]
        lp3.extend(self.idsp)
        lp3.extend(sc.idsp)
        ln3=[]
        ln3.extend(self.idsn)
        ln3.extend(sc.idsn)
        return SymCipher(v3,lp3,ln3)
    
    def addk(self, k : int=0, n:int=128):
        self.v = (self.v+k)%n
        return self
    
    def mmultk(self, k: int=1, n:int=128):
        self.v = (self.v*k)%n
        return self
    
    def amultk(self, k: int=1, n:int=128):
        self.v = (self.v*k)%n
        if k==0:
            self.idsp=[]
            self.idsn=[]
        if k>0:
            sidsn=list(self.idsn)
            sidsp=list(self.idsp)
            for _ in range (1,k):
                sidsp.extend(self.idsp)
                sidsn.extend(self.idsn)
            self.idsn=sidsn
            self.idsp=sidsp
        else:
            kp = k*(-1)
            sidsn=list(self.idsp)
            sidsp=list(self.idsn)
            for _ in range(1,kp):
                sidsn.extend(self.idsp)
                sidsp.extend(self.idsn)
            self.idsn=sidsn
            self.idsp=sidsp
        return self
    
    def expk(self, k: int=1, n:int=128):
        self.v = pow(self.v,k,n)
        if k==0:
            self.idsp=[]
            self.idsn=[]
        if k>0:
            sidsn=list(self.idsn)
            sidsp=list(self.idsp)
            for _ in range (1,k):
                sidsp.extend(self.idsp)
                sidsn.extend(self.idsn)
            self.idsn=sidsn
            self.idsp=sidsp
        else:
            kp = k*(-1)
            sidsn=list(self.idsp)
            sidsp=list(self.idsn)
            for _ in range(1,kp):
                sidsn.extend(self.idsp)
                sidsp.extend(self.idsn)
            self.idsn=sidsn
            self.idsp=sidsp
        return self