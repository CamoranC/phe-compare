# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:16:05 2024

@author: Christian
"""
from Crypto.Util.number import getRandomNBitInteger
from lightphe.cryptosystems import ElGamal
import random


def elginit(key_sizen:int=1024, key_sizeq: int =160, exponential:bool=False):
    return ElGamal.ElGamal(None, exponential, key_sizen, key_sizeq)

def elggen(elg:ElGamal, key_size: int=1024, key_sizeq: int=160):
    return elg.generate_keys(key_size, key_sizeq)

def elgenc (elg:ElGamal, m=0):
    return elg.encrypt(m)
   
def elgdec(elg:ElGamal, c=(0,0)):
    return elg.decrypt(c)

def elgranmes(elg:ElGamal, bits:int):
    p=elg.keys["public_key"]["p"]
    g=elg.keys["public_key"]["g"]
    q=elg.keys["public_key"]["q"]
    while True:
        x=random.randint(1,q)
        m=pow(g,x,p)
        if m.bit_length()==bits:
            break
    return m

def elgranmesn(elg:ElGamal):
    p=elg.keys["public_key"]["p"]
    g=elg.keys["public_key"]["g"]
    q=elg.keys["public_key"]["q"]
    x=random.randint(1,q)
    m=pow(g,x,p)
    return m

def elgmult(elg:ElGamal, ce, cz):
    return elg.multiply(ce, cz)

def elgadd(elg:ElGamal,ce, cz):
    return elg.add(ce, cz)

def elgmultconst(elg:ElGamal, c, k=0):
    return elg.multiply_by_contant(c,k)

def elgreenc(elg:ElGamal, c):
    return elg.reencrypt(c)