# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:48:38 2024

@author: Christian

Java-Original from Cuttlefish https://github.com/ssavvides/cuttlefish by Savvas Savvides
"""
from typing import Optional
from lightphe.models.Homomorphic import Homomorphic
from Crypto.Util.number import getRandomNBitInteger
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from lightphe.models import ASHECipher



class ASHE(Homomorphic):
    #nid=1
    #cipher = None
    
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
        
        fkip=self.getRandNum(self.nid-1)
        self.nid=self.nid+1
        v = (plaintext-fki+fkip)%n
        return ASHECipher.ASHECipher(v,int(tid))
        
        
        
    def getRandNum(self, idn: int):
        n = self.keys["n"]
        idb=idn.to_bytes(16,'big')
        fki=self.cipher.encrypt(idb)
        fkin=int.from_bytes(fki, 'big')
        return fkin % n
        
    def decrypt(self, ciphertext: ASHECipher) -> int:
        n = self.keys["n"]
        m = ciphertext.v
        if 1 in ciphertext.ids:
            m=m+self.getRandNum(len(ciphertext.ids))-self.getRandNum(0)
        else:
            for i in ciphertext.ids:
                m = m+(self.getRandNum(i)-self.getRandNum(i-1))
        #m=(m+r)%n
        return m%n

    def add(self, ciphertext1: ASHECipher, ciphertext2: ASHECipher) -> list:
        n = self.keys["n"]
        v = (ciphertext1.v + ciphertext2.v)%n
        ids=set(ciphertext1.ids)
        for i in ciphertext2.ids:
            ids.add(i)
        return ASHECipher.ASHECipher(v,ids)
        
    def multiply(self, ciphertext1, ciphertext2):
        print("not defined")
        
    def xor(self, ciphertext1: int, ciphertext2: int) -> list:
        raise ValueError("Goldwasser-Micali does not support xor")
        
    def multiply_by_contant(self, ciphertext: int, constant: int):
        raise ValueError("Goldwasser-Micali does not support multiplying with constant")

    def reencrypt(self, ciphertext: int):
        raise ValueError("Goldwasser-Micali does not support re-encryption")


    