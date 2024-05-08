# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 20:14:44 2024

@author: Christian
"""


import pyperf
import pickle


runner = pyperf.Runner()

for size in [2048,3072]:
    dlp=160
    if size==2048:
        dlp=224
    if size==3072:
        dlp=256
    block=16
    ms=15
    
    with open(f'DGK-{size}-{dlp}-{block}.pickle', 'rb') as file:
        d = pickle.load(file)
    with open(f'./picklec/DGK-c-{size}-{dlp}-{block}-{ms}.pickle', 'rb') as file:
        cf = pickle.load(file)
    with open(f'./picklecl/DGK-c-{size}-{dlp}-{block}-{ms}.pickle', 'rb') as file:
        cl = pickle.load(file)
    #runner.timeit(name=f"DGK-Gen-{size}-{dlp}-{block}", stmt=f"dgen(d,{size},{dlp},{block})", setup=["from DGKG import dgen"],globals={"d":d})
    if size != 2048:
        runner.timeit(name=f"DGK-Enc-{size}-{dlp}-{block}-{ms}", stmt="denc(d,m)", setup=["from DGKG import dranmes", "from DGKG import denc", f"m=dranmes(d,{ms})"],globals={"d":d})
        runner.timeit(name=f"DGK-Dec-{size}-{dlp}-{block}-{ms}", stmt="ddec(d,c)", setup=["from DGKG import ddec", "import random", "c=random.choice(cl)"],globals={"d":d, "cl":cl})
        runner.timeit(name=f"DGK-RE-{size}-{dlp}-{block}-{ms}",stmt="dreenc(d,cf)", setup=["from DGKG import dreenc"], globals={"d":d,"cf":cf})
        ma=block
        with open(f'./picklecl/DGK-c-{size}-{dlp}-{block}-{ma}.pickle', 'rb') as file:
            cla = pickle.load(file)
        runner.timeit(name=f"DGK-+-{size}-{dlp}-{block}-{ma}", stmt="dadd(d,c1,c2)", setup=["from DGKG import dadd", "import random", "c1=random.choice(cla)", "c2=random.choice(cla)"], globals={"d":d, "cla":cla})
        
    if size==2048:
        for block in [20]:
            with open(f'DGK-{size}-{dlp}-{block}.pickle', 'rb') as file:
                d = pickle.load(file)
            
            #if block != 32:
                #runner.timeit(name=f"DGK-Gen-{size}-{dlp}-{block}", stmt=f"dgen(d,{size},{dlp},{block})", setup=["from DGKG import dgen"],globals={"d":d})
            
            ms=block-1
            with open(f'./picklecl/DGK-c-{size}-{dlp}-{block}-{ms}.pickle', 'rb') as file:
                cl = pickle.load(file)
            #runner.timeit(name=f"DGK-Enc-{size}-{dlp}-{block}-{ms}", stmt="denc(d,m)", setup=["from DGKG import dranmes", "from DGKG import denc", f"m=dranmes(d,{ms})"],globals={"d":d})
            runner.timeit(name=f"DGK-Dec-{size}-{dlp}-{block}-{ms}", stmt="ddec(d,c)", setup=["from DGKG import ddec", "import random", "c=random.choice(cl)"],globals={"d":d, "cl":cl})
            with open(f'./picklec/DGK-c-{size}-{dlp}-{block}-{ms}.pickle', 'rb') as file:
                cf = pickle.load(file)
            runner.timeit(name=f"DGK-RE-{size}-{dlp}-{block}-{ms}",stmt="dreenc(d,cf)", setup=["from DGKG import dreenc"], globals={"d":d,"cf":cf})
            ma=block
            runner.timeit(name=f"DGK-+-{size}-{dlp}-{block}-{ma}", stmt="dadd(d,c1,c2)", setup=["from DGKG import dadd", "import random", "c1=random.choice(cl)", "c2=random.choice(cl)"], globals={"d":d, "cl":cl})
            
       