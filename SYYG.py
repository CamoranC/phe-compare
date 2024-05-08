# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:59:28 2024

@author: Christian
"""

from Crypto.Util.number import getRandomNBitInteger
from lightphe.cryptosystems import SYY


def syyinit(key_size:int=1024, vector: int=8):
    return SYY.SYY(None,key_size,vector)

def syygen(syy:SYY, key_size: int=1024, vector: int=8):
    return syy.generate_keys(key_size,vector)

def syyenc (syy:SYY, m=0):
    #c=[]
    #for i in m:
        #c.append(b.encrypt(int(i)))
    return syy.encrypt(m)
   
def syydec(syy:SYY, c=0):
    #m=0
    #for i in c:
       # m=m+(b.decrypt(int(i)))
    return syy.decrypt(c)

def syyranmes(syy:SYY, bits:int):
    #m=getRandomNBitInteger(bits)
    #print(m)
    #ms=[]
    #r=b.keys["public_key"]["r"]
    #for i in range(m,-1,-(r-1)):
        #if i >= r-1:
            #ms.append(r-1)
        #else:
            #ms.append(i)
    m=getRandomNBitInteger(bits)
    
    return m

def syymult(syy:SYY,ce, cz):
    return syy.multiply(ce, cz)

def syyreenc(syy:SYY,c):
    return syy.reencrypt(c)

def syyreencgm(syy:SYY, c):
    return syy.reencryptgm(c)

