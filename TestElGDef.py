# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 18:04:52 2024

@author: Christian
"""

import pyperf
import pickle


runner = pyperf.Runner()

for size in [2048,3072,7680]:
    dlp=160
    if size==2048:
        dlp=224
    if size==3072:
        dlp=256
    if size==7680:
        dlp=384
    ms=size-1
    with open(f'ElG-{size}-{dlp}.pickle', 'rb') as file:
        elg = pickle.load(file)
    with open(f'ElG-A-{size}-{dlp}.pickle', 'rb') as file:
        elga = pickle.load(file)
    with open(f'./picklec/ElG-c-{size}-{dlp}-{ms}.pickle', 'rb') as file:
        cf = pickle.load(file)
    #runner.timeit(name=f"ElG-Gen-{size}-{dlp}", stmt=f"elggen(elg,{size},{dlp})", setup=["from ElGG import elggen"],globals={"elg":elg})
    runner.timeit(name=f"ElG-Enc-{size}-{dlp}-{ms}", stmt="elgenc(elg,m)", setup=["from ElGG import elgranmes", "from ElGG import elgenc", f"m=elgranmes(elg,{ms})"],globals={"elg":elg})
    runner.timeit(name=f"ElG-A-Enc-{size}-{dlp}-{ms}", stmt="elgenc(elga,m)", setup=["from ElGG import elgranmes", "from ElGG import elgenc", f"m=elgranmes(elga,{ms})"],globals={"elga":elga})
    runner.timeit(name=f"ElG-Dec-{size}-{dlp}-{ms}", stmt="elgdec(elg,c)", setup=["from ElGG import elgranmes", "from ElGG import elgenc", "from ElGG import elgdec", f"m=elgranmes(elg,{ms})", "c=elgenc(elg,m)"],globals={"elg":elg})
    #runner.timeit(name=f"ElG-A-Dec-{size}-{dlp}-{ms}", stmt="elgdec(elga,c)", setup=["from ElGG import elgranmes", "from ElGG import elgenc", "from ElGG import elgdec", f"m=elgranmes(elga,{ms})", "c=elgenc(elga,m)"],globals={"elga":elga})
    runner.timeit(name=f"ElG-RE-{size}-{dlp}-{ms}",stmt="elgreenc(elg,cf)", setup=["from ElGG import elgreenc"], globals={"elg":elg,"cf":cf})
    mx=size-1
    ma=size-1
    runner.timeit(name=f"ElG-x-{size}-{dlp}-{mx}", stmt="elgmult(elg,c1,c2)", setup=["from ElGG import elgranmes", "from ElGG import elgenc", "from ElGG import elgmult", f"m1=elgranmes(elg,{mx})", f"m2=elgranmes(elg,{mx})", "c1=elgenc(elg,m1)", "c2=elgenc(elg,m2)"], globals={"elg":elg})
    runner.timeit(name=f"ElG-A-+-{size}-{dlp}-{ma}", stmt="elgadd(elga,c1,c2)", setup=["from ElGG import elgranmes", "from ElGG import elgenc", "from ElGG import elgadd", f"m1=elgranmes(elga,{ma})", f"m2=elgranmes(elga,{ma})", "c1=elgenc(elga,m1)", "c2=elgenc(elga,m2)"], globals={"elga":elga})
    
    #if size==2048:
        #for ms in [511,1535,2047]:
            #runner.timeit(name=f"ElG-Enc-{size}-{dlp}-{ms}", stmt="elgenc(elg,m)", setup=["from ElGG import elgranmes", "from ElGG import elgenc", f"m=elgranmes(elg,{ms})"],globals={"elg":elg})
            #runner.timeit(name=f"ElG-A-Enc-{size}-{dlp}-{ms}", stmt="elgenc(elga,m)", setup=["from ElGG import elgranmes", "from ElGG import elgenc", f"m=elgranmes(elga,{ms})"],globals={"elga":elga})
            #runner.timeit(name=f"ElG-Dec-{size}-{dlp}-{ms}", stmt="elgdec(elg,c)", setup=["from ElGG import elgranmes", "from ElGG import elgenc", "from ElGG import elgdec", f"m=elgranmes(elg,{ms})", "c=elgenc(elg,m)"],globals={"elg":elg})
            #runner.timeit(name=f"ElG-A-Dec-{size}-{dlp}-{ms}", stmt="elgdec(elga,c)", setup=["from ElGG import elgranmes", "from ElGG import elgenc", "from ElGG import elgdec", f"m=elgranmes(elga,{ms})", "c=elgenc(elga,m)"],globals={"elga":elga})    
            #with open(f'./picklec/ElG-c-{size}-{dlp}-{ms}.pickle', 'rb') as file:
                #cf = pickle.load(file)
            #runner.timeit(name=f"ElG-RE-{size}-{dlp}-{ms}",stmt="elgreenc(elg,cf)", setup=["from ElGG import elgreenc"], globals={"cf":cf})