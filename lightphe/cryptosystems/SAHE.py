# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:59:17 2024

@author: Christian

Java-Original from Symmetria https://github.com/ssavvides/symmetria by Savvas Savvides
"""

from typing import Optional
from lightphe.models.Homomorphic import Homomorphic
from Crypto.Util.number import getRandomNBitInteger
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from lightphe.models import SymCipher

class SAHE(Homomorphic):
    
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
        keys["key"]=key
        keys["n"]=n
        keys["k"]=key_size
        return keys
    
    def generate_random_key(self) -> int:
        print("not defined")
    
    def encrypt(self, plaintext: int, random_key: Optional[int] = None) :
        n = self.keys["n"]
        tid = self.nid
        fki=self.getRandNum(tid)
        self.nid=self.nid+1
        v = (plaintext+fki)%n
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
        m = ciphertext.v
        flp=0
        fln=0
        for i in ciphertext.idsp:
            flp = flp+(self.getRandNum(i))
        for i in ciphertext.idsn:
            fln = fln+(self.getRandNum(i))
        m=m-flp+fln
        return m%n

    def add(self, ciphertext1: SymCipher, ciphertext2: SymCipher) -> list:
        n = self.keys["n"]
        return ciphertext1.add(ciphertext2,n)
        
    def multiply(self, ciphertext1, ciphertext2):
        print("not defined")
        
    def xor(self, ciphertext1: int, ciphertext2: int) -> list:
        raise ValueError("Goldwasser-Micali does not support xor")
        
    def multiply_by_contant(self, ciphertext: SymCipher, constant: int):
       n = self.keys["n"]
       return ciphertext.amultk(constant,n)

    def reencrypt(self, ciphertext: int):
        raise ValueError("Goldwasser-Micali does not support re-encryption")

    def add_with_constant(self, ciphertext: SymCipher, constant: int):
        n = self.keys["n"]
        return ciphertext.addk(constant,n)