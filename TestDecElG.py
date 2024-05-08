# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 01:14:19 2024

@author: Christian
"""

import pyperf

runner = pyperf.Runner()

for size in [1024,2048,3072,7680]:
    if size==2048:
        for msf in [0.25,0.5,0.75,1.0]:
            ms=int(msf*size)-1
            runner.timeit(name=f"ElG-Dec-{size}-{ms}", stmt="elgdec(elg,c)", setup=["from ElGG import elgenc","from ElGG import elginit","from ElGG import elgranmes", "from ElGG import elgdec", f"elg=elginit({size})", f"m=elgranmes(elg,{ms})", "c=elgenc(elg,m)"])
            if msf == 0.5:
                runner.timeit(name=f"ElG-A-Dec-{size}-{ms}", stmt="elgdec(elg,c)", setup=["from ElGG import elgenc","from ElGG import elginit","from ElGG import elgranmes", "from ElGG import elgdec", f"elg=elginit({size},True)", f"m=elgranmes(elg,{ms})", "c=elgenc(elg,m)"])
    else:
        ms=1023
        runner.timeit(name=f"ElG-Dec-{size}-{ms}", stmt="elgdec(elg,c)", setup=["from ElGG import elgenc","from ElGG import elginit","from ElGG import elgranmes", "from ElGG import elgdec", f"elg=elginit({size})", f"m=elgranmes(elg,{ms})", "c=elgenc(elg,m)"])