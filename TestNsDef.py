# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 23:43:03 2024

@author: Christian
"""

import pyperf
import pickle



runner = pyperf.Runner()

for size in [1024,2048,3072,7680]:
    dlp=160
    if size==2048:
        dlp=224
    if size==3072:
        dlp=256
    if size==7680:
        dlp=384
    ms=dlp-1
    #with open(f'NS-{size}-{dlp}.pickle', 'rb') as file:
        #ns = pickle.load(file)
    with open(f'NS-D-{size}-{dlp}.pickle', 'rb') as file:
        nsd = pickle.load(file)
    #with open(f'./picklecl/NS-c-{size}-{dlp}-{ms}.pickle', 'rb') as file:
        #cl = pickle.load(file)
    #with open(f'./picklecl/NS-D-c-{size}-{dlp}-{ms}.pickle', 'rb') as file:
        #cdl = pickle.load(file)
    #if size !=3072:
        #runner.timeit(name=f"NS-Enc-{size}-{dlp}-{ms}", stmt="nsenc(ns,m)", setup=["from NSG import nsranmes", "from NSG import nsenc", f"m=nsranmes(ns,{ms})"],globals={"ns":ns})
    #runner.timeit(name=f"NS-Dec-{size}-{dlp}-{ms}", stmt="nsdec(ns,c)", setup=["from NSG import nsdec", "import random", "c=random.choice(cl)"],globals={"ns":ns, "cl":cl})
    runner.timeit(name=f"NS-D-Enc-{size}-{dlp}-{ms}", stmt="nsenc(nsd,m)", setup=["from NSG import nsranmes", "from NSG import nsenc", f"m=nsranmes(nsd,{ms})"],globals={"nsd":nsd})
    #runner.timeit(name=f"NS-D-Dec-{size}-{dlp}-{ms}", stmt="nsdec(nsd,c)", setup=["from NSG import nsdec", "import random", "c=random.choice(cdl)"],globals={"nsd":nsd, "cdl":cdl})
    #ma=dlp-1
    #with open(f'./picklecl/NS-c-{size}-{dlp}-{ma}.pickle', 'rb') as file:
        #cla = pickle.load(file)
    #with open(f'./picklecl/NS-D-c-{size}-{dlp}-{ma}.pickle', 'rb') as file:
        #cdla = pickle.load(file)
    #runner.timeit(name=f"NS-+-{size}-{dlp}-{ma}",stmt="nsadd(ns,c1,c2)",setup=["from NSG import nsadd", "import random", "c1=random.choice(cla)", "c2=random.choice(cla)"],globals={"ns":ns, "cla":cla})
    #runner.timeit(name=f"NS-D-+-{size}-{dlp}-{ma}",stmt="nsadd(nsd,c1,c2)",setup=["from NSG import nsadd", "import random", "c1=random.choice(cdla)", "c2=random.choice(cdla)"],globals={"nsd":nsd, "cdla":cdla})
   # with open(f'./picklec/NS-c-{size}-{dlp}-{ms}.pickle', 'rb') as file:
        #cf = pickle.load(file)
    #runner.timeit(name=f"NS-RE-{size}-{dlp}-{ms}",stmt="nsreenc(ns,cf)",setup=["from NSG import nsreenc"],globals={"ns":ns,"cf":cf})

    #if size==2048:
        #for ms in [79,111,223]:
            #with open(f'./picklecl/NS-c-{size}-{dlp}-{ms}.pickle', 'rb') as file:
                #cl = pickle.load(file)
            #with open(f'./picklecl/NS-D-c-{size}-{dlp}-{ms}.pickle', 'rb') as file:
                #cdl = pickle.load(file)
            #if ms != 111:
                #runner.timeit(name=f"NS-Enc-{size}-{dlp}-{ms}", stmt="nsenc(ns,m)", setup=["from NSG import nsranmes", "from NSG import nsenc", f"m=nsranmes(ns,{ms})"],globals={"ns":ns})
                #runner.timeit(name=f"NS-Dec-{size}-{dlp}-{ms}", stmt="nsdec(ns,c)", setup=["from NSG import nsdec", "import random", "random.choice(cl)"],globals={"ns":ns, "cl":cl})
            #runner.timeit(name=f"NS-D-Enc-{size}-{dlp}-{ms}", stmt="nsenc(nsd,m)", setup=["from NSG import nsranmes", "from NSG import nsenc", f"m=nsranmes(nsd,{ms})"],globals={"nsd":nsd})
            #runner.timeit(name=f"NS-D-Dec-{size}-{dlp}-{ms}", stmt="nsdec(nsd,c)", setup=["from NSG import nsdec", "import random", "c=random.choice(cdl)"],globals={"nsd":nsd, "cdl":cdl})
            #with open(f'./picklec/NS-c-{size}-{dlp}-{ms}.pickle', 'rb') as file:
                #cf = pickle.load(file)
            #runner.timeit(name=f"NS-RE-{size}-{dlp}-{ms}",stmt="nsreenc(ns,cf)",setup=["from NSG import nsreenc"],globals={"ns":ns,"cf":cf})