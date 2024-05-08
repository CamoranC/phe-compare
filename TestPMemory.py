# -*- coding: utf-8 -*-
"""
Created on Sat May  4 23:46:13 2024

@author: Christian
"""

from PG import pinit
from PG import pranmes
from PG import penc
from PG import pdec
from PG import padd
from PG import pgen
from PG import preenc
import tracemalloc
from statistics import median

for size in [1024,2048,3072,7680]:
    p=pinit(size)
    #genList=list()
    #for _ in range(0,10):
        #tracemalloc.start()
        #pgen(p,size)
        #(a,b)=tracemalloc.get_traced_memory()
        #tracemalloc.stop()
        #genList.append(b)
    #print(f"P-Gen-{size}-MAX:", max(genList))
    #print(f"P-Gen-{size}-MIN:", min(genList))
    #print(f"P-Gen-{size}-MEDIAN:", median(genList))
    
    m=pranmes(p,size)
    m2=pranmes(p,size)
    
    tracemalloc.start()
    penc(p,m)
    print(f"P-Enc-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    c=penc(p,m)
    c2=penc(p,m2)
    
    tracemalloc.start()
    pdec(p,c)
    print(f"P-Dec-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    tracemalloc.start()
    preenc(p,c)
    print(f"P-Re-Enc-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    tracemalloc.start()
    padd(p,c,c2)
    print(f"P-ADD-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()