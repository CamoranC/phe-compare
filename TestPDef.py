# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 16:46:06 2024

@author: Christian
"""
import pickle
import pyperf

runner = pyperf.Runner()

for size in [1024,2048,3072,7680]:
    with open(f'P-{size}.pickle', 'rb') as file:
        p = pickle.load(file)
    ms=size-1
    with open(f'./picklec/P-{size}-{ms}.pickle', 'rb') as file:
        cf = pickle.load(file)
    with open(f'./picklecl/P-{size}-{ms}.pickle', 'rb') as file:
        cl = pickle.load(file)

    runner.timeit(name=f"P-Enc-{size}-{ms}", stmt="penc(p,m)", setup=["from PG import penc","from PG import pranmes", f"m=pranmes(p,{ms})"], globals={"p":p})
    runner.timeit(name=f"P-Dec-{size}-{ms}", stmt="pdec(p,c)", setup=["from PG import pdec", "import random", "c=random.choice(cl)"],globals={"p":p, "cl":cl})
    runner.timeit(name=f"P-RE-{size}-{ms}",stmt="preenc(p,cf)", setup=["from PG import preenc"], globals={"p":p, "cf":cf})
    #with open(f'./picklecl/P-c-{size}-{msx}.pickle', 'rb') as file:
        #clx = pickle.load(file)
    runner.timeit(name=f"P-+-{size}-{ms}", stmt="padd(p,c1,c2)", setup=["from PG import padd", "import random", "c1=random.choice(cl)", "c2=random.choice(cl)"],globals={"p":p, "cl":cl})
    
    