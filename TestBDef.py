# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 18:36:52 2024

@author: Christian
"""

import pyperf
import pickle


runner = pyperf.Runner()

for size in [1024,2048,3072,7680]:
    block=16
    ms=16
    with open(f'B-{size}-{block}.pickle', 'rb') as file:
        b = pickle.load(file)
    with open(f'./picklec/B-c-{size}-{block}-{ms}.pickle', 'rb') as file:
        cf = pickle.load(file)
    with open(f'./picklecl/B-c-{size}-{block}-{ms}.pickle', 'rb') as file:
        cl = pickle.load(file)
    #runner.timeit(name=f"B-Gen-{size}-{block}", stmt=f"bgen(b,{size},{block})", setup=["from BG import bgen"],globals={"b":b})
    runner.timeit(name=f"B-Enc-{size}-{block}-{ms}", stmt="benc(b,m)", setup=["from BG import branmes", "from BG import benc", f"m=branmes(b,{ms})"],globals={"b":b})
    runner.timeit(name=f"B-Dec-{size}-{block}-{ms}", stmt="bdec(b,c)", setup=["from BG import bdec", "import random", "c=random.choice(cl)"],globals={"b":b, "cl":cl})
    runner.timeit(name=f"B-RE-{size}-{block}-{ms}",stmt="breenc(b,cf)", setup=["from BG import breenc"], globals={"b":b,"cf":cf})
    ma=16
    runner.timeit(name=f"B-+-{size}-{block}-{ma}", stmt="badd(b,c1,c2)", setup=["from BG import badd", "import random", "c1=random.choice(cl)", "c2=random.choice(cl)"], globals={"b":b, "cl":cl})
    
    if size==2048:
        for block in [12,20]:
            ms=block
            ma=block
            with open(f'B-{size}-{block}.pickle', 'rb') as file:
                b = pickle.load(file)
            with open(f'./picklecl/B-c-{size}-{block}-{ms}.pickle', 'rb') as file:
                cl = pickle.load(file)
            #runner.timeit(name=f"B-Enc-{size}-{block}-{ms}", stmt="benc(b,m)", setup=["from BG import branmes", "from BG import benc", f"m=branmes(b,{ms})"],globals={"b":b})
            #runner.timeit(name=f"B-Dec-{size}-{block}-{ms}", stmt="bdec(b,c)", setup=["from BG import bdec", "import random", "c=random.choice(cl)"],globals={"b":b, "cl":cl})
            with open(f'./picklec/B-c-{size}-{block}-{ms}.pickle', 'rb') as file:
                cf = pickle.load(file)
            runner.timeit(name=f"B-RE-{size}-{block}-{ms}",stmt="breenc(b,cf)", setup=["from BG import breenc"], globals={"b":b,"cf":cf})
            runner.timeit(name=f"B-+-{size}-{block}-{ma}", stmt="badd(b,c1,c2)", setup=["from BG import badd", "import random", "c1=random.choice(cl)", "c2=random.choice(cl)"], globals={"b":b, "cl":cl})