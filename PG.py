# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:58:53 2024

@author: Christian
"""

from Crypto.Util.number import getRandomNBitInteger
from lightphe.cryptosystems import Paillier

def pinit(key_size:int=1024):
    return Paillier.Paillier(None, key_size)

def pgen(p:Paillier, key_size:int=1024):
    return p.generate_keys(key_size)

def penc (p:Paillier, m=0):
    return p.encrypt(m)
   
def pdec(p:Paillier, c=0):
    return p.decrypt(c)

def pranmes(p:Paillier, bits:int):
    n=p.keys["public_key"]["n"]
    while True:
        m=getRandomNBitInteger(bits)
        if m<=n:
            break
    return getRandomNBitInteger(bits)

def padd(p:Paillier,ce, cz):
    return p.add(ce, cz)

def pmultconst(p:Paillier, c, k=0):
    return p.multiply_by_contant(c,k)

def paddconst(p:Paillier, c, k=0):
    return p.add_with_constant(c,k)

def preenc(p:Paillier, c):
    return p.reencrypt(c)


    