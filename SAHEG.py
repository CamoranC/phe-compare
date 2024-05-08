# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 17:36:51 2024

@author: Christian
"""

from Crypto.Util.number import getRandomNBitInteger
from lightphe.cryptosystems import SAHE
from lightphe.models import SymCipher


def saheinit(key_size:int=128):
    return SAHE.SAHE(key_size)

def sahegen(sahe:SAHE, key_size: int=128):
    return sahe.generate_keys(key_size)

def saheenc (sahe:SAHE, m=0):
    return sahe.encrypt(m)
   
def sahedec(sahe:SAHE, c:SymCipher):
    return sahe.decrypt(c)

def saheadd(sahe:SAHE, c1:SymCipher, c2:SymCipher):
    return sahe.add(c1,c2)

def saheranmes(sahe:SAHE, bits:int):
    x=getRandomNBitInteger(bits)
    n = sahe.keys["n"]
    return x%n

def saheaddk(sahe:SAHE, c:SymCipher, constant:int):
    return sahe.add_with_constant(c, constant)

def sahemultk(sahe:SAHE, c:SymCipher, constant:int):
    return sahe.multiply_by_contant(c, constant)
