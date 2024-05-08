# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:06:07 2024

@author: Christian
"""

import pyperf

runner = pyperf.Runner()
for size in [7680]:
    #runner.timeit(name=f"RSA-Gen-{size}", stmt=f"rsagen(rsa,{size})", setup=["from RSAG import rsagen","from RSAG import rsainit","rsa=rsainit(6)"])
    #runner.timeit(name=f"ElG-Gen-{size}", stmt=f"elggen(elg,{size})", setup=["from ElGG import elggen","from ElGG import elginit","elg=elginit(6)"])
    #runner.timeit(name=f"GM-Gen-{size}", stmt=f"gmgen(gm,{size})", setup=["from GMG import gmgen","from GMG import gminit","gm=gminit(6)"])
    #dlp = 160
    #dgkr=False
    #if size == 2048:
        #dgkr=True
        #dlp = 224
    #if size ==3072:
        #dlp = 256
    #if size == 7690:
    dlp=384
    runner.timeit(name=f"NS-Gen-{size}-{dlp}", stmt=f"nsgen(ns,{size},{dlp})", setup=["from NSG import nsgen","from NSG import nsinit","ns=nsinit()"])
    #if dgkr:
        #for r in [8,16,32]:
            #runner.timeit(name=f"DGK-Gen-{size}-{dlp}-{r}", stmt=f"dgen(d,{size},{dlp},{r})", setup=["from DGKG import dgen","from DGKG import dinit","d=dinit()"])
    #else:
        #runner.timeit(name=f"DGK-Gen-{size}-{dlp}-16", stmt=f"dgen(d,{size},{dlp},16)", setup=["from DGKG import dgen","from DGKG import dinit","d=dinit()"])
    runner.timeit(name=f"B-Gen-{size}-32", stmt=f"bgen(b,{size},32)", setup=["from BG import bgen","from BG import binit","b=binit()"])
    #if size == 2048:
        #for block in [16,64]:
            #runner.timeit(name=f"B-Gen-{size}-{block}", stmt=f"bgen(b,{size},{block})", setup=["from BG import bgen","from BG import binit","b=binit()"])
    #for l in [8,16,32]:
        #runner.timeit(name=f"SYY-Gen-{size}-{l}", stmt=f"syygen(syy,{size},{l})", setup=["from SYYG import syygen","from SYYG import syyinit","syy=syyinit(6,2)"])
    
