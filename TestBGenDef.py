# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 13:34:06 2024

@author: Christian
"""


import pyperf
import pickle


runner = pyperf.Runner()

for size in [1024,2048,3072,7680]:
    block=16
    with open(f'B-{size}-{block}.pickle', 'rb') as file:
        b = pickle.load(file)
    runner.timeit(name=f"B-Gen-{size}-{block}", stmt=f"bgen(b,{size},{block})", setup=["from BG import bgen"],globals={"b":b})
    if size==2048:
        for block in [12,20]:
            with open(f'B-{size}-{block}.pickle', 'rb') as file:
                b = pickle.load(file)
            runner.timeit(name=f"B-Gen-{size}-{block}", stmt=f"bgen(b,{size},{block})", setup=["from BG import bgen"],globals={"b":b})