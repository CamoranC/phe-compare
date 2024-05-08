# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 00:31:09 2024

@author: Christian
"""
from Crypto.Util.number import getRandomNBitInteger
from lightphe.cryptosystems import DGK

def dinit(key_sizek:int=1024, key_sizet: int=160, key_sizel: int=32):
    return DGK.DGK(None, key_sizek, key_sizet, key_sizel)

def dgen(d:DGK, key_sizek:int=1024, key_sizet: int=160, key_sizel: int=32):
    return d.generate_keys(key_sizek, key_sizet, key_sizel)

def denc (d:DGK, m=0):
    return d.encrypt(m)
   
def ddec(d:DGK, c=0):
    return d.decrypt(c)

def dranmes(d:DGK, bits:int):
    u=d.keys["public_key"]["u"]
    while True:
        m=getRandomNBitInteger(bits)
        if m<=u:
            break
    return getRandomNBitInteger(bits)

def dadd(d:DGK,ce, cz):
    return d.add(ce, cz)

def dmultconst(d:DGK, c, k=0):
    return d.multiply_by_contant(c,k)

def daddconst(d:DGK, c, k=0):
    return d.add_with_constant(c,k)

def dreenc(d:DGK, c):
    return d.reencrypt(c)

def diszero(d:DGK, c):
    return d.isZero(c)
    