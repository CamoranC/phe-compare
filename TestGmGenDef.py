# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 11:56:05 2024

@author: Christian
"""

import pyperf
import pickle


runner = pyperf.Runner()

for size in [1024,2048,3072,7680]:
    with open(f'GM-{size}.pickle', 'rb') as file:
        gm = pickle.load(file)
    runner.timeit(name=f"GM-Gen-{size}", stmt=f"gmgen(gm,{size})", setup=["from GMG import dgen"],globals={"gm":gm})
