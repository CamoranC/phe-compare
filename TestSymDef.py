# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 13:40:25 2024

@author: Christian
"""

import pyperf
from ASHEG import asheinit
from SAHEG import saheinit
from SMHEG import smheinit


runner = pyperf.Runner()

#pm=[-1,1]

for size in [192]:
    ashe=asheinit(size)
    sahe=saheinit(size)
    smhe=smheinit(size)
    ms=127   
    #runner.timeit(name=f"ASHE-Enc-{size}-{ms}", stmt="asheenc(ashe,m)",setup=["from ASHEG import asheinit", "from ASHEG import asheranmes", "from ASHEG import asheenc", f"ashe=asheinit({size})", f"m=asheranmes(ashe,{ms})"])
    #runner.timeit(name=f"SAHE-Enc-{size}-{ms}", stmt="saheenc(sahe,m)",setup=["from SAHEG import saheinit", "from SAHEG import saheranmes", "from SAHEG import saheenc", f"sahe=saheinit({size})", f"m=saheranmes(sahe,{ms})"])
    #runner.timeit(name=f"SMHE-Enc-{size}-{ms}", stmt="smheenc(smhe,m)",setup=["from SMHEG import smheranmes", "from SMHEG import smheenc", f"m=smheranmes(smhe,{ms})"], globals={"smhe":smhe})
    runner.timeit(name=f"ASHE-Dec-{size}-{ms}", stmt="ashedec(ashe,c)",setup=["from ASHEG import asheinit", "from ASHEG import asheranmes", "from ASHEG import asheenc", "from ASHEG import ashedec", f"ashe=asheinit({size})",f"m=asheranmes(ashe,{ms})","c=asheenc(ashe,m)"])
    runner.timeit(name=f"SAHE-Dec-{size}-{ms}", stmt="sahedec(sahe,c)",setup=[ "from SAHEG import saheranmes", "from SAHEG import saheenc", "from SAHEG import sahedec", f"m=saheranmes(sahe,{ms})","c=saheenc(sahe,m)"], globals={"sahe":sahe})
    runner.timeit(name=f"SMHE-Dec-{size}-{ms}", stmt="smhedec(smhe,c)",setup=["from SMHEG import smheranmes", "from SMHEG import smheenc", "from SMHEG import smhedec", f"m=smheranmes(smhe,{ms})","c=smheenc(smhe,m)"], globals={"smhe":smhe})
    runner.timeit(name=f"ASHE-+-{size}-{ms}", stmt="asheadd(ashe,c1,c2)",setup=["from ASHEG import asheinit", "from ASHEG import asheranmes", "from ASHEG import asheenc", "from ASHEG import asheadd", f"ashe=asheinit({size})", f"m1=asheranmes(ashe,{ms})","c1=asheenc(ashe,m1)", f"m2=asheranmes(ashe,{ms})","c2=asheenc(ashe,m2)"])
    runner.timeit(name=f"SAHE-+-{size}-{ms}", stmt="saheadd(sahe,c1,c2)",setup=["from SAHEG import saheranmes", "from SAHEG import saheenc", "from SAHEG import saheadd", f"m1=saheranmes(sahe,{ms})","c1=saheenc(sahe,m1)", f"m2=saheranmes(sahe,{ms})","c2=saheenc(sahe,m2)"], globals={"sahe":sahe})
    runner.timeit(name=f"SMHE-x-{size}-{ms}", stmt="smhemult(smhe,c1,c2)",setup=["from SMHEG import smheranmes", "from SMHEG import smheenc", "from SMHEG import smhemult", f"m1=smheranmes(smhe,{ms})","c1=smheenc(smhe,m1)", f"m2=smheranmes(smhe,{ms})","c2=smheenc(smhe,m2)"], globals={"smhe":smhe})
    for kb in [2,4,8]:     
        runner.timeit(name=f"SAHE-xk-{size}-{ms}-{kb}", stmt="sahemultk(sahe,c1,k)",setup=["from SAHEG import saheinit", "from SAHEG import saheranmes", "from SAHEG import saheenc", "from SAHEG import sahemultk", "from random import randint", f"m1=saheranmes(sahe,{ms})","c1=saheenc(sahe,m1)", "k=randint(-(2**kb),2**kb)"],globals={"kb":kb, "sahe":sahe})
        runner.timeit(name=f"SMHE-^k-{size}-{ms}-{kb}", stmt="smheexpk(smhe,c1,k)",setup=["from SMHEG import smheinit", "from SMHEG import smheranmes", "from SMHEG import smheenc", "from SMHEG import smheexpk", "from random import randint", f"m1=smheranmes(smhe,{ms})","c1=smheenc(smhe,m1)", "k=randint(-(2**kb),2**kb)"],globals={"kb":kb, "smhe":smhe})
    
    for loop in [5,10]:    
        runner.timeit(name=f"ASHE-Dec-{size}-{ms}-{loop}", stmt="ashedec(ashe,c)",setup=["from ASHEG import asheinit", "from ASHEG import asheranmes", "from ASHEG import asheenc", "from ASHEG import ashedec", "from ASHEG import asheadd", f"ashe=asheinit({size})", f"m=asheranmes(ashe,{ms})","c=asheenc(ashe,m)", f"for _ in range(0,{loop}): c=asheadd(ashe,c,c)"])
        runner.timeit(name=f"SAHE-Dec-{size}-{ms}-{loop}", stmt="sahedec(sahe,c)",setup=["from SAHEG import saheranmes", "from SAHEG import saheenc", "from SAHEG import sahedec", "from SAHEG import saheadd", "from SAHEG import sahemultk", "from random import choice", f"m=saheranmes(sahe,{ms})","c=saheenc(sahe,m)", f"for _ in range(0,{loop}): c=saheadd(sahe,c,sahemultk(sahe,c,choice([-1,1])))"], globals={"sahe":sahe})
        runner.timeit(name=f"SMHE-Dec-{size}-{ms}-{loop}", stmt="smhedec(smhe,c)",setup=["from SMHEG import smheranmes", "from SMHEG import smheenc", "from SMHEG import smhedec", "from SMHEG import smhemult", "from SMHEG import smheexpk", "from random import choice", f"m=smheranmes(smhe,{ms})","c=smheenc(smhe,m)", f"for _ in range(0,{loop}): c=smhemult(smhe,c,smheexpk(smhe,c,choice([-1,1])))"], globals={"smhe":smhe})
        runner.timeit(name=f"ASHE-+-{size}-{ms}-{loop}", stmt="asheadd(ashe,c1,c2)",setup=["from ASHEG import asheinit", "from ASHEG import asheranmes", "from ASHEG import asheenc", "from ASHEG import asheadd", f"ashe=asheinit({size})", f"m1=asheranmes(ashe,{ms})","c1=asheenc(ashe,m1)", f"m2=asheranmes(ashe,{ms})","c2=asheenc(ashe,m2)", f"for _ in range(0,{loop}): c1=asheadd(ashe,c1,c1)", f"for _ in range(0,{loop}): c2=asheadd(ashe,c2,c2)"])
        runner.timeit(name=f"SAHE-+-{size}-{ms}-{loop}", stmt="saheadd(sahe,c1,c2)",setup=["from SAHEG import saheranmes", "from SAHEG import saheenc", "from SAHEG import saheadd", "from SAHEG import sahemultk", "from random import choice", f"m1=saheranmes(sahe,{ms})","c1=saheenc(sahe,m1)", f"m2=saheranmes(sahe,{ms})","c2=saheenc(sahe,m2)", f"for _ in range(0,{loop}): c1=saheadd(sahe,c1,sahemultk(sahe,c1,choice([-1,1])))", f"for _ in range(0,{loop}): c2=saheadd(sahe,c2,sahemultk(sahe,c2,choice([-1,1])))"], globals={"sahe":sahe})
        runner.timeit(name=f"SMHE-x-{size}-{ms}-{loop}", stmt="smhemult(smhe,c1,c2)",setup=["from SMHEG import smheranmes", "from SMHEG import smheenc", "from SMHEG import smhemult", "from SMHEG import smheexpk", "from random import choice", f"m1=smheranmes(smhe,{ms})","c1=smheenc(smhe,m1)", f"m2=smheranmes(smhe,{ms})","c2=smheenc(smhe,m2)", f"for _ in range(0,{loop}): c1=smhemult(smhe,c1,smheexpk(smhe,c1,choice([-1,1])))", f"for _ in range(0,{loop}): c2=smhemult(smhe,c2,smheexpk(smhe,c2,choice([-1,1])))"], globals={"smhe":smhe})
            
        runner.timeit(name=f"SAHE-xk-{size}-{ms}-{loop}-4", stmt="sahemultk(sahe,c1,k)",setup=["from SAHEG import saheranmes", "from SAHEG import saheenc", "from SAHEG import sahemultk", "from SAHEG import saheadd", "from random import randint", "from random import choice", f"m1=saheranmes(sahe,{ms})","c1=saheenc(sahe,m1)", "k=randint(-(2**4),2**4)", f"for _ in range(0,{loop}): c1=saheadd(sahe,c1,sahemultk(sahe,c1,choice([-1,1])))"], globals={"sahe":sahe})
        runner.timeit(name=f"SMHE-^k-{size}-{ms}-{loop}-4", stmt="smheexpk(smhe,c1,k)",setup=["from SMHEG import smheranmes", "from SMHEG import smheenc", "from SMHEG import smheexpk", "from SMHEG import smhemult", "from random import randint", "from random import choice", f"m1=smheranmes(smhe,{ms})","c1=smheenc(smhe,m1)", "k=randint(-(2**4),2**4)", f"for _ in range(0,{loop}): c1=smhemult(smhe,c1,smheexpk(smhe,c1,choice([-1,1])))"], globals={"smhe":smhe})
   