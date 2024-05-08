# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:27:57 2024

@author: Christian
"""
from Crypto.Util.number import getRandomNBitInteger
from lightphe.cryptosystems import Benaloh


def binit(key_size:int=1024, block: int=512):
    return Benaloh.Benaloh(None, key_size, block)

def bgen(b:Benaloh, key_size: int=1024, block: int=64):
    return b.generate_keys(key_size,block)

def benc (b:Benaloh, m=0):
    #c=[]
    #for i in m:
        #c.append(b.encrypt(int(i)))
    return b.encrypt(m)
   
def bdec(b:Benaloh, c=0):
    #m=0
    #for i in c:
       # m=m+(b.decrypt(int(i)))
    return b.decrypt(c)

def branmes(b:Benaloh, bits:int):
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

def badd(b:Benaloh,ce, cz):
    return b.add(ce, cz)

def bmultconst(b:Benaloh, c, k=0):
    return b.multiply_by_contant(c,k)

def baddconst(b:Benaloh, c, k=0):
    return b.add_with_constant(c,k)

def breenc(b:Benaloh, c):
    return b.reencrypt(c)
    