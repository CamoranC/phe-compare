# -*- coding: utf-8 -*-
"""
Created on Wed May  1 03:02:15 2024

@author: Christian
"""

import pyperf
import pickle


runner = pyperf.Runner()

for size in [2048]:
    block=20
    ms=19
    with open(f'B-{size}-{block}.pickle', 'rb') as file:
        b = pickle.load(file)
    with open(f'./picklec/B-c-{size}-{block}-{ms}.pickle', 'rb') as file:
        cf = pickle.load(file)
    with open(f'./picklecl/B-c-{size}-{block}-{ms}.pickle', 'rb') as file:
        cl = pickle.load(file)
    #runner.timeit(name=f"B-Gen-{size}-{block}", stmt=f"bgen(b,{size},{block})", setup=["from BG import bgen"],globals={"b":b})
    runner.timeit(name=f"B-Enc-{size}-{block}-{ms}", stmt="benc(b,m)", setup=["from BG import branmes", "from BG import benc", f"m=branmes(b,{ms})"],globals={"b":b})
    runner.timeit(name=f"B-Dec-{size}-{block}-{ms}", stmt="bdec(b,c)", setup=["from BG import bdec", "import random", "c=random.choice(cl)"],globals={"b":b, "cl":cl})
    