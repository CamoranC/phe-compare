# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 01:03:23 2024

@author: Christian
"""

import pyperf

runner = pyperf.Runner()
for size in [1024,2048,3072,7680]:
    if size==2048:
        for msf in [0.25,0.5,0.75,1.0]:
            ms = int(size*msf)-1
            runner.timeit(name=f"RSA-Dec-{size}-{ms}", stmt="rsadec(rsa,c)", setup=["from RSAG import rsaenc","from RSAG import rsainit","from RSAG import rsaranmes", "from RSAG import rsadec", f"rsa=rsainit({size})", f"m=rsaranmes(rsa,{ms})", "c=rsaenc(rsa,m)"])
            runner.timeit(name=f"GM-Dec-{size}-{ms}", stmt="gmdec(gm,c)", setup=["from GMG import gmenc","from GMG import gminit","from GMG import gmranmes", "from GMG import gmdec", f"gm=gminit({size})", f"m=gmranmes(gm,{ms})", "c=gmenc(gm,m)"])
            runner.timeit(name=f"SYY-Dec-{size}-8-{ms}", stmt="syydec(syy,c)", setup=["from SYYG import syyenc","from SYYG import syyinit","from SYYG import syyranmes", "from SYYG import syydec", f"syy=syyinit({size},8)", f"m=syyranmes(syy,{ms})", "c=syyenc(syy,m)"])
            ms = int(size*32)-1
            runner.timeit(name=f"B-Dec-{size}-32-{ms}", stmt="bdec(b,c)", setup=["from BG import benc","from BG import binit","from BG import branmes", "from BG import bdec", f"b=binit({size},32)", f"m=branmes(b,{ms})", "c=benc(b,m)"])
            if msf == 0.5:
                for block in [16,64]:
                    ms = int(block*msf)-1
                    runner.timeit(name=f"B-Dec-{size}-{block}-{ms}", stmt="bdec(b,c)", setup=["from BG import benc","from BG import binit","from BG import branmes", "from BG import bdec", f"b=binit({size},{block})", f"m=branmes(b,{ms})", "c=benc(b,m)"])
                for l in [16,32]:
                    ms = int(size*msf)-1
                    runner.timeit(name=f"SYY-Dec-{size}-{l}-{ms}", stmt="syydec(syy,c)", setup=["from SYYG import syyenc","from SYYG import syyinit","from SYYG import syyranmes", "from SYYG import syydec", f"syy=syyinit({size},{l})", f"m=syyranmes(syy,{ms})", "c=syyenc(syy,m)"])
            dlp = 224
            ms= int(msf*dlp)-1
            runner.timeit(name=f"NS-Dec-{size}-{dlp}-{ms}", stmt="nsdec(ns,c)", setup=["from NSG import nsenc","from NSG import nsinit","from NSG import nsranmes", "from NSG import nsdec", f"ns=nsinit({size},{dlp})", f"m=nsranmes(ns,{ms})", "c=nsenc(ns,m)"])
            runner.timeit(name=f"NS-D-Dec-{size}-{dlp}-{ms}", stmt="nsdec(ns,c)", setup=["from NSG import nsenc","from NSG import nsinit","from NSG import nsranmes", "from NSG import nsdec", f"ns=nsinit({size},{dlp},True)", f"m=nsranmes(ns,{ms})", "c=nsenc(ns,m)"])
    else:
        ms=1023
        runner.timeit(name=f"RSA-Dec-{size}-{ms}", stmt="rsadec(rsa,c)", setup=["from RSAG import rsaenc","from RSAG import rsainit","from RSAG import rsaranmes", "from RSAG import rsadec", f"rsa=rsainit({size})", f"m=rsaranmes(rsa,{ms})", "c=rsaenc(rsa,m)"])
        runner.timeit(name=f"GM-Dec-{size}-{ms}", stmt="gmdec(gm,c)", setup=["from GMG import gmenc","from GMG import gminit","from GMG import gmranmes", "from GMG import gmdec", f"gm=gminit({size})", f"m=gmranmes(gm,{ms})", "c=gmenc(gm,m)"])
        runner.timeit(name=f"SYY-Dec-{size}-8-{ms}", stmt="syydec(syy,c)", setup=["from SYYG import syyenc","from SYYG import syyinit","from SYYG import syyranmes", "from SYYG import syydec", f"syy=syyinit({size},8)", f"m=syyranmes(syy,{ms})", "c=syyenc(syy,m)"])
        ms = 15
        runner.timeit(name=f"B-Dec-{size}-32-{ms}", stmt="bdec(b,c)", setup=["from BG import benc","from BG import binit","from BG import branmes", "from BG import bdec", f"b=binit({size},32)", f"m=branmes(b,{ms})", "c=benc(b,m)"])
        dlp=160
        if size==3072:
            dlp=256
        if size==7680:
            dlp=384
        ms = 111
        runner.timeit(name=f"NS-Dec-{size}-{dlp}-{ms}", stmt="nsdec(ns,c)", setup=["from NSG import nsenc","from NSG import nsinit","from NSG import nsranmes", "from NSG import nsdec", f"ns=nsinit({size},{dlp})", f"m=nsranmes(ns,{ms})", "c=nsenc(ns,m)"])
        