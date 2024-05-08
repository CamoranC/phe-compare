# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 00:55:22 2024

@author: Christian
"""

import pyperf
import pickle


runner = pyperf.Runner()

for size in [1024,2048,3072,7680]:
    l=8
    with open(f'SYY-{size}-{l}.pickle', 'rb') as file:
        syy = pickle.load(file)
    ms=1
    #with open(f'./picklecl/SYY-c-{size}-{l}-{ms}.pickle', 'rb') as file:
        #cl = pickle.load(file)
    #runner.timeit(name=f"SYY-Enc-{size}-{l}-{ms}", stmt="syyenc(syy,m)", setup=["from SYYG import syyranmes", "from SYYG import syyenc", f"m=syyranmes(syy,{ms})"],globals={"syy":syy})
    #runner.timeit(name=f"SYY-Dec-{size}-{l}-{ms}", stmt="syydec(syy,c)", setup=["from SYYG import syydec", "import random", "c=random.choice(cl)"],globals={"syy":syy, "cl":cl})    
    ma=1
    with open(f'./picklecl/SYY-c-{size}-{l}-{ma}.pickle', 'rb') as file:
        cla = pickle.load(file)
    #runner.timeit(name=f"SYY-x-{size}-{l}-{ma}", stmt="syymult(syy,c1,c2)",setup=["from SYYG import syymult", "import random", "c1=random.choice(cla)", "c2=random.choice(cla)"], globals={"syy":syy, "cla":cla})
    with open(f'./picklec/SYY-c-{size}-{l}-{ma}.pickle', 'rb') as file:
        clf = pickle.load(file)
    runner.timeit(name=f"SYY-REGM-{size}-{l}-{ma}", stmt="syyreencgm(syy,clf)", setup=["from SYYG import syyreencgm"],globals={"syy":syy,"clf":clf})
    
    if size==2048:
        for l in [16,32]:
            with open(f'SYY-{size}-{l}.pickle', 'rb') as file:
                syy = pickle.load(file)
            with open(f'./picklecl/SYY-c-{size}-{l}-{ms}.pickle', 'rb') as file:
                cl = pickle.load(file)
            with open(f'./picklecl/SYY-c-{size}-{l}-{ma}.pickle', 'rb') as file:
                cla = pickle.load(file)
            #runner.timeit(name=f"SYY-Enc-{size}-{l}-{ms}", stmt="syyenc(syy,m)", setup=["from SYYG import syyranmes", "from SYYG import syyenc", f"m=syyranmes(syy,{ms})"],globals={"syy":syy})
            #runner.timeit(name=f"SYY-Dec-{size}-{l}-{ms}", stmt="syydec(syy,c)", setup=["from SYYG import syydec", "import random", "c=random.choice(cl)"],globals={"syy":syy, "cl":cl})    
            #runner.timeit(name=f"SYY-x-{size}-{l}-{ma}", stmt="syymult(syy,c1,c2)",setup=["from SYYG import syymult", "import random", "c1=random.choice(cla)", "c2=random.choice(cla)"], globals={"syy":syy, "cla":cla})
            with open(f'./picklec/SYY-c-{size}-{l}-{ma}.pickle', 'rb') as file:
                clf = pickle.load(file)
            runner.timeit(name=f"SYY-REGM-{size}-{l}-{ma}", stmt="syyreencgm(syy,clf)", setup=["from SYYG import syyreencgm"],globals={"syy":syy,"clf":clf})
            

        #l=8
       # with open(f'SYY-{size}-{l}.pickle', 'rb') as file:
            #syy = pickle.load(file)
        #for ms in [511,1535,2047]:
            #with open(f'./picklecl/SYY-{size}-{l}-{ms}.pickle', 'rb') as file:
                #cl = pickle.load(file)
            #runner.timeit(name=f"SYY-Enc-{size}-{l}-{ms}", stmt="syyenc(syy,m)", setup=["from SYYG import syyranmes", "from SYYG import syyenc", f"m=syyranmes(syy,{ms})"],globals={"syy":syy})
            #runner.timeit(name=f"SYY-Dec-{size}-{l}-{ms}", stmt="syydec(syy,c)", setup=["from SYYG import syydec", "import random", "c=random.choice(cl)"],globals={"syy":syy, "cl":cl})    

            