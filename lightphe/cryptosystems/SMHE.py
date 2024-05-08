# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:43:48 2024

@author: Christian

Java-Original from Symmetria https://github.com/ssavvides/symmetria by Savvas Savvides
"""

from typing import Optional
from lightphe.models.Homomorphic import Homomorphic
from Crypto.Util.number import getRandomNBitInteger
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from lightphe.models import SymCipher
from sympy import totient
import random
import math

class SMHE(Homomorphic):
    
    def __init__(self, key_size: int=128, keys: Optional[dict] = None) :
        self.keys = keys or self.generate_keys(key_size)
        key = self.keys["key"]
        n = self.keys["n"]
        self.cipher = AES.new(key, AES.MODE_ECB)
        self.plaintext_modulo=n
        self.ciphertext_modulo=n
        self.nid=1
        
    def generate_keys(self, key_size: int) -> dict:
        keys={}
        n=getRandomNBitInteger(128)
        key=get_random_bytes(key_size // 8)
        phi = int(totient(n))
        while True:
            g=random.randint(1,n-1)
            if math.gcd(g,n)==1 and pow(g,phi,n)==1:
                break
        keys["key"]=key
        keys["n"]=n
        keys["k"]=key_size
        keys["phi"]=phi
        keys["g"]=g
        return keys
    
    def generate_random_key(self) -> int:
        print("not defined")
    
    def encrypt(self, plaintext: int, random_key: Optional[int] = None) :
        n = self.keys["n"]
        g = self.keys["g"]
        tid = self.nid
        fki=self.getRandNum(tid)
        gp=pow(g,fki,n)
        self.nid=self.nid+1
        v = (plaintext*gp)%n
        return SymCipher.SymCipher(v,int(tid),[])
        
        
        
    def getRandNum(self, idn: int):
        n = self.keys["n"]
        k = self.keys["k"]
        idb=idn.to_bytes(16,'big')
        fki=self.cipher.encrypt(idb)
        fkin=int.from_bytes(fki,'big')
        return fkin % n
        
    def decrypt(self, ciphertext: SymCipher) -> int:
        n = self.keys["n"]
        g = self.keys["g"]
        m = ciphertext.v
        flp=1
        fln=1
        for i in ciphertext.idsp:
            flp = flp*(pow(g,(-1)*self.getRandNum(i),n))
        for i in ciphertext.idsn:
            fln = fln*(pow(g,self.getRandNum(i),n))
        m=m*flp*fln
        return m%n

    def add(self, ciphertext1: SymCipher, ciphertext2: SymCipher) -> list:
        print("not defined")
        
    def multiply(self, ciphertext1, ciphertext2):
        n = self.keys["n"]
        return ciphertext1.mult(ciphertext2,n)
        
    def xor(self, ciphertext1: int, ciphertext2: int) -> list:
        raise ValueError("Goldwasser-Micali does not support xor")
        
    def multiply_by_contant(self, ciphertext: SymCipher, constant: int):
       n = self.keys["n"]
       return ciphertext.mmultk(constant,n)

    def reencrypt(self, ciphertext: int):
        raise ValueError("Goldwasser-Micali does not support re-encryption")

    def exp_with_constant(self, ciphertext: SymCipher, constant: int):
        n = self.keys["n"]
        return ciphertext.expk(constant,n)