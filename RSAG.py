# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:41:35 2024

@author: Christian
"""
from Crypto.Util.number import getRandomNBitInteger
from lightphe.cryptosystems import RSA


def rsainit (key_size: int=1024):
    return RSA.RSA(None, key_size, True)

def rsagen (rsa:RSA, key_size: int=1024):
    return rsa.generate_keys(key_size)
    
def rsaenc (rsa:RSA, m=0):
    return rsa.encrypt(m)
   
def rsadec(rsa:RSA, c=0):
    return rsa.decrypt(c)

def rsaranmes(rsa:RSA, bits:int):
    m=getRandomNBitInteger(bits)
    return m

def rsamult(rsa:RSA, ce=0, cz=0):
    return rsa.multiply(ce, cz)

def rsaexpconst(rsa:RSA, c=0,k=0 ):
    return rsa.exponentiation_by_constant(c,k)

def rsainv(rsa:RSA, c=0):
    return rsa.eekinv(c)