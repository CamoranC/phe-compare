# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 00:05:14 2024

@author: Christian
"""

from Crypto.Util.number import getRandomNBitInteger
from lightphe.cryptosystems import ASHE
from lightphe.models import ASHECipher


def asheinit(key_size:int=128):
    return ASHE.ASHE(key_size)

def ashegen(ashe:ASHE, key_size: int=128):
    return ashe.generate_keys(key_size)

def asheenc (ashe:ASHE, m=0):
    return ashe.encrypt(m)
   
def ashedec(ashe:ASHE, c:ASHECipher):
    return ashe.decrypt(c)

def asheadd(ashe:ASHE, c1:ASHECipher, c2:ASHECipher):
    return ashe.add(c1,c2)

def asheranmes(ashe:ASHE, bits:int):
    x=getRandomNBitInteger(bits)
    n = ashe.keys["n"]
    return x%n

