# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 02:16:58 2024

@author: Christian
"""
import pyperf

runner = pyperf.Runner()

size=1024
ms=1023
runner.timeit(name=f"RSA-Enc-{size}-{ms}", stmt="rsaenc(rsa,m)", setup=["from RSAG import rsaenc","from RSAG import rsainit","from RSAG import rsaranmes", f"rsa=rsainit({size})", f"m=rsaranmes(rsa,{ms})"])
runner.timeit(name=f"GM-Enc-{size}-{ms}", stmt="gmenc(gm,m)", setup=["from GMG import gmenc","from GMG import gminit","from GMG import gmranmes", f"gm=gminit({size})", f"m=gmranmes(gm,{ms})"])