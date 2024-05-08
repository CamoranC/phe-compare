# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:22:18 2024

@author: Christian
"""

import pyperf
from RSAG import rsainit
from GMG import gminit
from NSG import nsinit

runner = pyperf.Runner()
for size in [2048,3072,7680]:
    if size == 2048:
        dlp = 224
        rsa=rsainit(size)
        gm=gminit(size)
        ns=nsinit(size,dlp)
        nsd=nsinit(size,dlp,True)
        for msf in [0.75,1.0]:
            ms = int(size*msf)-1
            
            if msf==1.0:
                runner.timeit(name=f"RSA-Enc-{size}-{ms}", stmt="rsaenc(rsa,m)", setup=["from RSAG import rsaenc","from RSAG import rsaranmes", f"m=rsaranmes(rsa,{ms})"], globals={"rsa":rsa})
                runner.timeit(name=f"GM-Enc-{size}-{ms}", stmt="gmenc(gm,m)", setup=["from GMG import gmenc","from GMG import gmranmes", f"m=gmranmes(gm,{ms})"], globals={"gm":gm})
            #runner.timeit(name=f"B-Enc-{size}-32-{ms}", stmt="benc(b,m)", setup=["from BG import benc","from BG import binit","from BG import branmes", f"b=binit({size},32)", f"m=branmes(b,{ms})"])
            #for block in [16,64]:
                #runner.timeit(name=f"B-Enc-{size}-{block}-{ms}", stmt="benc(b,m)", setup=["from BG import benc","from BG import binit","from BG import branmes", f"b=binit({size},{block})", f"m=branmes(b,{ms})"])
            ms = int(msf*dlp)-1
            runner.timeit(name=f"NS-Enc-{size}-{dlp}-{ms}", stmt="nsenc(ns,m)", setup=["from NSG import nsenc","from NSG import nsranmes",f"m=nsranmes(ns,{ms})"], globals={"ns":ns})
            runner.timeit(name=f"NS-D-Enc-{size}-{dlp}-{ms}", stmt="nsenc(ns,m)", setup=["from NSG import nsenc","from NSG import nsranmes",f"m=nsranmes(ns,{ms})"],globals={"ns":nsd})
            #for l in [8,16,32]:
                #runner.timeit(name=f"SYY-Enc-{size}-{l}-{ms}", stmt="syyenc(syy,m)", setup=["from SYYG import syyenc","from SYYG import syyinit","from SYYG import syyranmes", f"syy=syyinit({size},{l})", f"m=syyranmes(syy,{ms})"])
    else:
        dlp = 160
        if size ==3072:
            dlp = 256
        if size == 7680:
            dlp = 384
        ns=nsinit(size,dlp)
        if size != 1024:
            rsa=rsainit(size)
            gm=gminit(size)
            ms = 1023
            runner.timeit(name=f"RSA-Enc-{size}-{ms}", stmt="rsaenc(rsa,m)", setup=["from RSAG import rsaenc","from RSAG import rsaranmes", f"m=rsaranmes(rsa,{ms})"],globals={"rsa":rsa})
            runner.timeit(name=f"GM-Enc-{size}-{ms}", stmt="gmenc(gm,m)", setup=["from GMG import gmenc","from GMG import gmranmes", f"m=gmranmes(gm,{ms})"], globals={"gm":gm})
            #runner.timeit(name=f"B-Enc-{size}-32-{ms}", stmt="benc(b,m)", setup=["from BG import benc","from BG import binit","from BG import branmes", f"b=binit({size},32)", f"m=branmes(b,{ms})"])
            #l=8
            #runner.timeit(name=f"SYY-Enc-{size}-{l}-{ms}", stmt="syyenc(syy,m)", setup=["from SYYG import syyenc","from SYYG import syyinit","from SYYG import syyranmes", f"syy=syyinit({size},{l})", f"m=syyranmes(syy,{ms})"])
        
        ms=111
        runner.timeit(name=f"NS-Enc-{size}-{dlp}-{ms}", stmt="nsenc(ns,m)", setup=["from NSG import nsenc","from NSG import nsranmes",f"m=nsranmes(ns,{ms})"], globals={"ns":ns})
        