# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:44:44 2024

@author: Christian
"""

from GMG import gminit
from GMG import gmranmes
from GMG import gmenc
from GMG import gmdec
from GMG import gmreenc
from GMG import gmxor
from GMG import gmgen
import tracemalloc
from statistics import median

for size in [1024,2048,3072,7680]:
    gm=gminit(size)
    #genList=list()
    #for _ in range(0,10):
        #tracemalloc.start()
        #gmgen(gm,size)
        #(a,b)=tracemalloc.get_traced_memory()
        #tracemalloc.stop()
        #genList.append(b)
    #print(f"GM-Gen-{size}-MAX:", max(genList))
    #print(f"GM-Gen-{size}-MIN:", min(genList))
   # print(f"GM-Gen-{size}-MEDIAN:", median(genList))
    
    m=gmranmes(gm,1)
    m2=gmranmes(gm,1)
    
    tracemalloc.start()
    gmenc(gm,m)
    print(f"GM-Enc-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    c=gmenc(gm,m)
    c2=gmenc(gm,m2)
    
    tracemalloc.start()
    gmdec(gm,c)
    print(f"GM-Dec-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    tracemalloc.start()
    gmreenc(gm,c)
    print(f"GM-Re-Enc-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    tracemalloc.start()
    gmxor(gm,c,c2)
    print(f"GM-XOR-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()