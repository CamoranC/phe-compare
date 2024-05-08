# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:11:36 2024

@author: Christian
"""

from Crypto.Util.number import getRandomNBitInteger
from lightphe.cryptosystems import SMHE
from lightphe.models import SymCipher
import math


def smheinit(key_size:int=128):
    return SMHE.SMHE(key_size)

def smhegen(smhe:SMHE, key_size: int=128):
    return smhe.generate_keys(key_size)

def smheenc (smhe:SMHE, m=0):
    return smhe.encrypt(m)
   
def smhedec(smhe:SMHE, c:SymCipher):
    return smhe.decrypt(c)

def smhemult(smhe:SMHE, c1:SymCipher, c2:SymCipher):
    return smhe.multiply(c1,c2)

def smheranmes(smhe:SMHE, bits:int):
    n = smhe.keys["n"]
    while True:
        x=getRandomNBitInteger(bits)
        if math.gcd(x,n)==1:
            break
    return x%n

def smheexpk(smhe:SMHE, c:SymCipher, constant:int):
    return smhe.exp_with_constant(c, constant)

def smhemultk(smhe:SMHE, c:SymCipher, constant:int):
    return smhe.multiply_by_contant(c, constant)
