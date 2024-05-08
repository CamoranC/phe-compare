# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:07:42 2024

@author: Christian
"""

from lightphe.cryptosystems import GoldwasserMicali
from Crypto.Util.number import getRandomNBitInteger

def gminit(key_size:int=1024):
    return GoldwasserMicali.GoldwasserMicali(None, key_size)

def gmgen(gm:GoldwasserMicali, key_size: int=1024):
    return gm.generate_keys(key_size)

def gmenc (gm:GoldwasserMicali, m=0):
    return gm.encrypt(m)
   
def gmdec(gm:GoldwasserMicali, c=(0,0)):
    return gm.decrypt(c)

def gmranmes(gm:GoldwasserMicali, bits:int):
    return getRandomNBitInteger(bits)

def gmxor(gm,ce,cz):
    return gm.xor(ce,cz)

def gmreenc (gm:GoldwasserMicali, c):
    return gm.reencrypt(c)
