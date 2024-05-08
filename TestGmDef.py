# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 01:19:02 2024

@author: Christian
"""

import pyperf
import pickle


runner = pyperf.Runner()

for size in [1024,2048,3072,7680]:
    with open(f'GM-{size}.pickle', 'rb') as file:
        gm = pickle.load(file)
    ms=1
   # with open(f'./picklec/GM-c-{size}-{ms}.pickle', 'rb') as file:
        #cf = pickle.load(file)
    #with open(f'./picklecl/GM-c-{size}-{ms}.pickle', 'rb') as file:
        #cl = pickle.load(file)
    #if size != 2048:
    runner.timeit(name=f"GM-Enc-{size}-{ms}", stmt="gmenc(gm,m)", setup=["from GMG import gmenc","from GMG import gmranmes", f"m=gmranmes(gm,{ms})"], globals={"gm":gm})
    runner.timeit(name=f"GM-Dec-{size}-{ms}", stmt="gmdec(gm,c)", setup=["from GMG import gmdec", "from GMG import gmenc", "from GMG import gmranmes", f"m=gmranmes(gm,{ms})", "c=gmenc(gm,m)"],globals={"gm":gm})
    runner.timeit(name=f"GM-RE-{size}-{ms}",stmt="gmreenc(gm,c)", setup=["from GMG import gmreenc", "from GMG import gmenc", "from GMG import gmranmes", f"m=gmranmes(gm,{ms})", "c=gmenc(gm,m)"], globals={"gm":gm})
    msx=1
    #with open(f'./picklecl/GM-c-{size}-{msx}.pickle', 'rb') as file:
        #clx = pickle.load(file)
    runner.timeit(name=f"GM-+-{size}-{msx}", stmt="gmxor(gm,c1,c2)", setup=["from GMG import gmxor", "from GMG import gmenc", "from GMG import gmranmes", f"m1=gmranmes(gm,{ms})", "c1=gmenc(gm,m1)", f"m2=gmranmes(gm,{ms})", "c2=gmenc(gm,m2)"],globals={"gm":gm})
    
    #if size==2048:
        #for ms in [511,1535,2047]:
            #with open(f'./picklecl/GM-c-{size}-{ms}.pickle', 'rb') as file:
                #cl = pickle.load(file)
           # runner.timeit(name=f"GM-Enc-{size}-{ms}", stmt="gmenc(gm,m)", setup=["from GMG import gmenc","from GMG import gmranmes", f"m=gmranmes(gm,{ms})"], globals={"gm":gm})
            #runner.timeit(name=f"GM-Dec-{size}-{ms}", stmt="gmdec(gm,c)", setup=["from GMG import gmdec", "import random", "c=cl"],globals={"gm":gm, "cl":cl})
            #with open(f'./picklec/GM-c-{size}-{ms}.pickle', 'rb') as file:
                #cf = pickle.load(file)          
            #runner.timeit(name=f"GM-RE-{size}-{ms}",stmt="gmreenc(gm,cf)", setup=["from GMG import gmreenc"], globals={"gm":gm,"cf":cf})