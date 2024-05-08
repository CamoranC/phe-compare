# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:31:06 2024

@author: Christian
"""

import pyperf
from ASHEG import asheinit
from SAHEG import saheinit
from SMHEG import smheinit

runner = pyperf.Runner()
ashe=asheinit()
sahe=saheinit()
smhe=smheinit()

for size in [128,192]:
    runner.timeit(name=f"ASHE-Gen-{size}", stmt=f"ashegen(ashe,{size})", setup=["from ASHEG import ashegen"],globals={"ashe":ashe})
    runner.timeit(name=f"SAHE-Gen-{size}", stmt=f"sahegen(sahe,{size})", setup=["from SAHEG import sahegen"],globals={"sahe":sahe})
    runner.timeit(name=f"SMHE-Gen-{size}", stmt=f"smhegen(smhe,{size})", setup=["from SMHEG import smhegen"],globals={"smhe":smhe})
    