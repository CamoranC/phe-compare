# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 20:10:00 2024

@author: Christian

On the basis of the Homomorphic Class from LightPHE https://github.com/serengil/LightPHE by Sefik Ilkin Serengil 
"""
from typing import Optional
import lightphe.cryptosystems.GoldwasserMicali as GM
from lightphe.models.Homomorphic import Homomorphic
import numpy as np
import random

class SYY(Homomorphic):
    
    gm: GM
    
    def __init__(self, keys: Optional[dict] = None, key_size: int=1024, vector: int=8):
        self.gm = GM.GoldwasserMicali(None, key_size)
        self.keys = self.gm.keys
        self.keys["public_key"]["l"] = vector
        
    def generate_keys(self, key_size: int) -> dict:
        print("not defined")
    
    def generate_random_key(self) -> int:
        print("not defined")
    
    def generate_random_matrix(self):
        l = self.keys["public_key"]["l"]
        while True:
            matrix = np.random.randint(0,2,size=(l,l))
            if np.linalg.det(matrix) != 0:
                break
        return matrix
    
    def encrypt(self, plaintext: int, random_key: Optional[int] = None) :
        l = self.keys["public_key"]["l"]
        m_binary = bin(plaintext)[2:]
        k = len(m_binary)
        cipher=[]
        for i in range(0,k):
            cbit=[]
            mi = int(m_binary[i])
            if mi == 1:
                for _ in range(0,l):
                    cbit.append(self.gm.encrypt(0)[0])                    
            else:
                for _ in range(0,l):
                    j = random.randint(0,1)
                    cbit.append(self.gm.encrypt(j)[0])
            cipher.append(cbit)
        return np.array(cipher)
        
    def decrypt(self, ciphertext: np.array) -> int:
        """
        Decrypt a given ciphertext with Sander-Young-Yung
        Args:
            ciphertext (int): encrypted message
        Returns:
            plaintext (int): restored message
        """
        m_binaries = []
        #l = self.keys["public_key"]["l"]

        for i in ciphertext:
            zero = True
            for j in i:
                mi=self.gm.decrypt([j])
                if mi != 0:
                    zero=False
                    break
            if zero:
                m_binaries.append("1")
            else:
                m_binaries.append("0")
                
        m_binary = "".join(m_binaries)
        return int(m_binary, 2)

    def add(self, ciphertext1: list, ciphertext2: list) -> list:
        raise ValueError("Sander-Young-Yung is not homomorphic with respect to the addition")

    def multiply(self, ciphertext1: np.array, ciphertext2: np.array):
        mult=[]
        l = self.keys["public_key"]["l"]
        if len(ciphertext1) > len(ciphertext2):
            maxc=ciphertext1
            minc=ciphertext2
        else:
            maxc=ciphertext2
            minc=ciphertext1
        diff=len(maxc)-len(minc)
        for m in minc:
            #a=self.generate_random_matrix()
            #b=self.generate_random_matrix()
            #x=[]
            #y=[]
            xy=[]
            for j in range (0,l):
                xj=m[j]
                yj=maxc[diff][j]
                #for i in range(0,l):
                    #if a[i][j]==1:
                        #xj=self.gm.xor([a[i][j]],xj)
                    #if b[i][j]==1:
                        #yj=self.gm.xor([b[i][j]],yj)
                #x.append(xj)
                #y.append(yj)
                xy.append(self.gm.xor(xj,yj)[0])
            #mult.append(np.multiply(x,y))
            mult.append(xy)
            diff=diff+1
        return np.array(mult)
        
    def xor(self, ciphertext1: int, ciphertext2: int) -> list:
        raise ValueError("Sander-Young-Yung does not support xor")
        
    def multiply_by_contant(self, ciphertext: int, constant: int):
        raise ValueError("Sander-Young-Yung does not support multiplying with constant")

    def reencrypt(self, ciphertext: int):
        #y=self.gm.keys["public_key"]["x"]
        #n=self.gm.keys["public_key"]["n"]
        l = self.keys["public_key"]["l"]
        c=[]
        for cipherbit in ciphertext:
            a=self.generate_random_matrix()
            cbv=[]
            for i in range(0,l):
                cvv=1     
                for j in range(0,l):
                    cvv=cvv*pow(int(cipherbit[j]),a[i][j])
                cbv.append(cvv)
            c.append(cbv)
        return np.array(c)
    
    def reencryptgm(self, ciphertext: int):
        l = self.keys["public_key"]["l"]
        c=[]
        for cipherbit in ciphertext:
            cb=[]
            for i in range(0,l):
                cb.append(self.gm.reencrypt([cipherbit[i]])[0])
            c.append(cb)
        return np.array(c)
        
