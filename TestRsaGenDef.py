# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 12:01:03 2024

@author: Christian
"""

import pyperf
import pickle


runner = pyperf.Runner()

for size in [1024,2048,3072,7680]:
    with open(f'RSA-{size}.pickle', 'rb') as file:
        rsa = pickle.load(file)
    runner.timeit(name=f"RSA-Gen-{size}", stmt=f"rsagen(rsa,{size})", setup=["from RSAG import rsagen"],globals={"rsa":rsa})
