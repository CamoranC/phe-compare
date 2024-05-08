# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 19:14:03 2024

@author: Christian
"""
import pyperf
import pickle


runner = pyperf.Runner()

size=1024
with open(f'RSA-{size}.pickle', 'rb') as file:
    rsa = pickle.load(file)
ms=1023
runner.timeit(name=f"RSA-Gen-{size}", stmt=f"rsagen(rsa,{size})", setup=["from RSAG import rsagen"],globals={"rsa":rsa})