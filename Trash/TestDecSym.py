# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:58:00 2024

@author: Christian
"""

import pyperf

runner = pyperf.Runner()

for size in [128,192]:
    if size == 128:
        for msf in [0.25,0.5,0.75,1.0]:
            ms=int(msf*size)-1
            runner.timeit(name=f"ASHE-Dec-{size}-{ms}", stmt="ashedec(ashe,c)", setup=["from ASHEG import asheenc","from ASHEG import asheinit","from ASHEG import asheranmes", "from ASHEG import ashedec", f"ashe=asheinit({size})", f"m=asheranmes(ashe,{ms})", "c=asheenc(ashe,m)"])
            runner.timeit(name=f"SAHE-Dec-{size}-{ms}", stmt="sahedec(sahe,c)", setup=["from SAHEG import saheenc","from SAHEG import saheinit","from SAHEG import saheranmes", "from SAHEG import sahedec", f"sahe=saheinit({size})", f"m=saheranmes(sahe,{ms})", "c=saheenc(sahe,m)"])
            runner.timeit(name=f"SMHE-Dec-{size}-{ms}", stmt="smhedec(smhe,c)", setup=["from SMHEG import smheenc","from SMHEG import smheinit","from SMHEG import smheranmes", "from SMHEG import smhedec", f"smhe=smheinit({size})", f"m=smheranmes(smhe,{ms})", "c=smheenc(smhe,m)"])
    else:
        ms=127
        runner.timeit(name=f"ASHE-Dec-{size}-{ms}", stmt="ashedec(ashe,c)", setup=["from ASHEG import asheenc","from ASHEG import asheinit","from ASHEG import asheranmes", "from ASHEG import ashedec", f"ashe=asheinit({size})", f"m=asheranmes(ashe,{ms})", "c=asheenc(ashe,m)"])
        runner.timeit(name=f"SAHE-Dec-{size}-{ms}", stmt="sahedec(sahe,c)", setup=["from SAHEG import saheenc","from SAHEG import saheinit","from SAHEG import saheranmes", "from SAHEG import sahedec", f"sahe=saheinit({size})", f"m=saheranmes(sahe,{ms})", "c=saheenc(sahe,m)"])
        runner.timeit(name=f"SMHE-Dec-{size}-{ms}", stmt="smhedec(smhe,c)", setup=["from SMHEG import smheenc","from SMHEG import smheinit","from SMHEG import smheranmes", "from SMHEG import smhedec", f"smhe=smheinit({size})", f"m=smheranmes(smhe,{ms})", "c=smheenc(smhe,m)"])