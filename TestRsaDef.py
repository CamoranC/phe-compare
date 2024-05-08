# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 00:40:06 2024

@author: Christian
"""

import pyperf
import pickle


runner = pyperf.Runner()

for size in [1024,2048,3072,7680]:
    with open(f'RSA-{size}.pickle', 'rb') as file:
        rsa = pickle.load(file)
    ms=size-1
    mx=size-1
    #runner.timeit(name=f"RSA-Gen-{size}", stmt=f"rsagen(rsa,{size})", setup=["from RSAG import rsagen"],globals={"rsa":rsa})
    runner.timeit(name=f"RSA-Enc-{size}-{ms}", stmt="rsaenc(rsa,m)", setup=["from RSAG import rsaenc","from RSAG import rsaranmes", f"m=rsaranmes(rsa,{ms})"], globals={"rsa":rsa})
    runner.timeit(name=f"RSA-Dec-{size}-{ms}", stmt="rsadec(rsa,c)", setup=["from RSAG import rsaenc","from RSAG import rsaranmes", "from RSAG import rsadec", f"m=rsaranmes(rsa,{ms})", "c=rsaenc(rsa,m)"],globals={"rsa":rsa})
    runner.timeit(name=f"RSA-x-{size}-{mx}", stmt="rsamult(rsa,c1,c2)", setup=["from RSAG import rsaenc","from RSAG import rsaranmes", "from RSAG import rsamult", f"m1=rsaranmes(rsa,{mx})", "c1=rsaenc(rsa,m1)", f"m2=rsaranmes(rsa,{mx})", "c2=rsaenc(rsa,m2)"],globals={"rsa":rsa})
    
    #if size==2048:
        #for ms in [511,1535,2023]:
            #runner.timeit(name=f"RSA-Enc-{size}-{ms}", stmt="rsaenc(rsa,m)", setup=["from RSAG import rsaenc","from RSAG import rsaranmes", f"m=rsaranmes(rsa,{ms})"], globals={"rsa":rsa})
            #runner.timeit(name=f"RSA-Dec-{size}-{ms}", stmt="rsadec(rsa,c)", setup=["from RSAG import rsaenc","from RSAG import rsaranmes", "from RSAG import rsadec", f"m=rsaranmes(rsa,{ms})", "c=rsaenc(rsa,m)"],globals={"rsa":rsa})