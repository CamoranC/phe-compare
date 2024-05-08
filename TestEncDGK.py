# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 00:29:38 2024

@author: Christian
"""

import pyperf

runner = pyperf.Runner()

for size in [1024,2048,3072,7680]:
    if size==2048:
        for msf in [0.25,0.5,0.75,1.0]:
            ms=int(msf*32)-1
            dlp = 224
            runner.timeit(name=f"DGK-Enc-{size}-{dlp}-32-{ms}", stmt="dgkenc(dgk,m)", setup=["from DGKG import dgkenc","from DGKG import dgkinit","from DGKG import dgkranmes", f"dgk=dgkinit({size},{dlp},32)", f"m=dgkranmes(dgk,{ms})"])
            if msf == 0.5:
                for r in [16,64]:
                    ms=int(msf*r)-1
                    runner.timeit(name=f"DGK-Enc-{size}-{dlp}-{r}-{ms}", stmt="dgkenc(dgk,m)", setup=["from DGKG import dgkenc","from DGKG import dgkinit","from DGKG import dgkranmes", f"dgk=dgkinit({size},{dlp},{r})", f"m=dgkranmes(dgk,{ms})"])
    else:
        dlp = 160
        if size ==3072:
            dlp = 256
        if size == 7690:
            dlp=384
        ms=15
        runner.timeit(name=f"DGK-Enc-{size}-{dlp}-32-{ms}", stmt="dgkenc(dgk,m)", setup=["from DGKG import dgkenc","from DGKG import dgkinit","from DGKG import dgkranmes", f"dgk=dgkinit({size},{dlp},32)", f"m=dgkranmes(dgk,{ms})"])