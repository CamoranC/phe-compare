# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 00:05:57 2024

@author: Christian
"""
import pyperf

runner = pyperf.Runner()

for size in [1024,2048,3072,7680]:
    if size==2048:
        for msf in [0.25,0.5,0.75,1.0]:
            ms=int(msf*size)-2
            runner.timeit(name=f"ElG-Enc-{size}-{ms}", stmt="elgenc(elg,m)", setup=["from ElGG import elgenc","from ElGG import elginit","from ElGG import elgranmes", f"elg=elginit({size})", f"m=elgranmes(elg,{ms})"])
            runner.timeit(name=f"ElG-A-Enc-{size}-{ms}", stmt="elgenc(elg,m)", setup=["from ElGG import elgenc","from ElGG import elginit","from ElGG import elgranmes", f"elg=elginit({size},True)", f"m=elgranmes(elg,{ms})"])
    else:
        ms=1022
        runner.timeit(name=f"ElG-Enc-{size}-{ms}", stmt="elgenc(elg,m)", setup=["from ElGG import elgenc","from ElGG import elginit","from ElGG import elgranmes", f"elg=elginit({size})", f"m=elgranmes(elg,{ms})"])