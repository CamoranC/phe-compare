# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:03:41 2024

@author: Christian
"""
import random
from lightphe.cryptosystems import RSA


def test (key_size: int=1024) -> bool:
    r = RSA.RSA()
    keys = r.generate_keys(key_size)

    r.__init__(keys)

    m = random.randint(1, r.keys["public_key"]["n"])

    c = r.encrypt(m)

    mm = r.decrypt(c)
    
    return m==mm

print(test(1024))