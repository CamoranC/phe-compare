# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:02:17 2024

@author: Christian
"""
from RSAG import rsadec
import pickle
for size in [1024,2048,3072,7680]:
    with open(f'RSA-{size}.pickle', 'rb') as file:
        rsa = pickle.load(file)
    with open(f'./picklec/RSA-c-{size}-1023.pickle', 'rb') as file:
        c = pickle.load(file)
    d=rsadec(rsa,c)
    print(d)