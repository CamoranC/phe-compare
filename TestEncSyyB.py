# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:24:28 2024

@author: Christian
"""

import pyperf

runner = pyperf.Runner()
for size in [1024,2048,3072,7680]:
    if size == 2048:
        for msf in [0.25,0.5,0.75,1.0]:
            if msf==0.5:
                for block in [16,32,64]:
                    ms=int(msf*block)-1
                    runner.timeit(name=f"B-Enc-{size}-{block}-{ms}", stmt="benc(b,m)", setup=["from BG import benc","from BG import binit","from BG import branmes", f"b=binit({size},{block})", f"m=branmes(b,{ms})"])
                ms = int(size*msf)-1
                for l in [8,16,32]:
                    runner.timeit(name=f"SYY-Enc-{size}-{l}-{ms}", stmt="syyenc(syy,m)", setup=["from SYYG import syyenc","from SYYG import syyinit","from SYYG import syyranmes", f"syy=syyinit({size},{l})", f"m=syyranmes(syy,{ms})"])
            else:
                block = 32
                l=8
                ms=int(msf*block)-1
                runner.timeit(name=f"B-Enc-{size}-{block}-{ms}", stmt="benc(b,m)", setup=["from BG import benc","from BG import binit","from BG import branmes", f"b=binit({size},{block})", f"m=branmes(b,{ms})"])
                ms = int(size*msf)-1
                runner.timeit(name=f"SYY-Enc-{size}-{l}-{ms}", stmt="syyenc(syy,m)", setup=["from SYYG import syyenc","from SYYG import syyinit","from SYYG import syyranmes", f"syy=syyinit({size},{l})", f"m=syyranmes(syy,{ms})"])
    else:
        block=32
        l=8
        ms=block-1
        runner.timeit(name=f"B-Enc-{size}-{block}-{ms}", stmt="benc(b,m)", setup=["from BG import benc","from BG import binit","from BG import branmes", f"b=binit({size},{block})", f"m=branmes(b,{ms})"])
        if size != 1024:
            ms = 1023
            runner.timeit(name=f"SYY-Enc-{size}-{l}-{ms}", stmt="syyenc(syy,m)", setup=["from SYYG import syyenc","from SYYG import syyinit","from SYYG import syyranmes", f"syy=syyinit({size},{l})", f"m=syyranmes(syy,{ms})"])