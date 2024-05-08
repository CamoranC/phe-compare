# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:14:40 2024

@author: Christian
"""

from Crypto.Util.number import getRandomNBitInteger
from lightphe.cryptosystems import NaccacheStern as NS

def nsinit(key_sizen:int=1024, key_sizes: int=160, deterministic: bool=False):
    return NS.NaccacheStern(None, key_sizen, key_sizes, deterministic)

def nsgen(ns:NS, key_sizen:int=1024, key_sizes: int=160):
    return ns.generate_keys(key_sizen, key_sizes)

def nsenc (ns:NS, m=0):
    return ns.encrypt(m)
   
def nsdec(ns:NS, c=0):
    return ns.decrypt(c)

def nsranmes(ns:NS, bits:int):
    return getRandomNBitInteger(bits)

def nsadd(ns:NS,ce, cz):
    return ns.add(ce, cz)

def nsmultconst(ns:NS, c, k=0):
    return ns.multiply_by_contant(c,k)

def nsaddconst(ns:NS, c, k=0):
    return ns.add_with_constant(c,k)

def nsreenc(ns:NS, c):
    return ns.reencrypt(c)