# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 16:44:39 2024

@author: Christian
"""

import pyperf
import pickle


runner = pyperf.Runner()

for size in [1024,2048,3072,7680]:
    with open(f'P-{size}.pickle', 'rb') as file:
        p = pickle.load(file)
    runner.timeit(name=f"P-Gen-{size}", stmt=f"pgen(p,{size})", setup=["from PG import pgen"],globals={"p":p})
