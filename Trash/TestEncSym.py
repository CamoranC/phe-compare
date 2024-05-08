# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:35:23 2024

@author: Christian
"""

import pyperf

runner = pyperf.Runner()

for size in [128,192]:
    if size == 128:
        for msf in [0.25,0.5,0.75,1.0]:
            ms=int(msf*size)-1
            runner.timeit(name=f"ASHE-Enc-{size}-{ms}", stmt="asheenc(dgk,m)", setup=["from ASHEG import asheenc","from ASHEG import asheinit","from ASHEG import asheranmes", f"ashe=asheinit({size})", f"m=asheranmes(ashe,{ms})"])
            runner.timeit(name=f"SAHE-Enc-{size}-{ms}", stmt="saheenc(dgk,m)", setup=["from SAHEG import saheenc","from SAHEG import saheinit","from SAHEG import saheranmes", f"sahe=saheinit({size})", f"m=saheranmes(sahe,{ms})"])
            runner.timeit(name=f"SMHE-Enc-{size}-{ms}", stmt="smheenc(dgk,m)", setup=["from SMHEG import smheenc","from SMHEG import smheinit","from SMHEG import smheranmes", f"smhe=smheinit({size})", f"m=smheranmes(smhe,{ms})"])
    else:
        ms=127
        runner.timeit(name=f"ASHE-Enc-{size}-{ms}", stmt="asheenc(dgk,m)", setup=["from ASHEG import asheenc","from ASHEG import asheinit","from ASHEG import asheranmes", f"ashe=asheinit({size})", f"m=asheranmes(ashe,{ms})"])
        runner.timeit(name=f"SAHE-Enc-{size}-{ms}", stmt="saheenc(dgk,m)", setup=["from SAHEG import saheenc","from SAHEG import saheinit","from SAHEG import saheranmes", f"sahe=saheinit({size})", f"m=saheranmes(sahe,{ms})"])
        runner.timeit(name=f"SMHE-Enc-{size}-{ms}", stmt="smheenc(dgk,m)", setup=["from SMHEG import smheenc","from SMHEG import smheinit","from SMHEG import smheranmes", f"smhe=smheinit({size})", f"m=smheranmes(smhe,{ms})"])