# -*- coding: utf-8 -*-
"""
Created on Thu May  2 02:24:28 2024

@author: Christian
"""

from NSG import nsinit
from NSG import nsranmes
from NSG import nsenc
from NSG import nsdec
from NSG import nsreenc
from NSG import nsadd
from NSG import nsgen
import tracemalloc
from statistics import median

for size in [1024,2048,3072,7680]:
    dlp=160
    if size == 2048:
        dlp=224
    if size==3072:
        dlp=256
    if size==7680:
        dlp=384
    ns=nsinit(size,dlp)
    #genList=list()
    #for _ in range(0,10):
        #tracemalloc.start()
        #nsgen(ns,size,dlp)
        #(a,b)=tracemalloc.get_traced_memory()
        #tracemalloc.stop()
        #genList.append(b)
    #print(f"NS-Gen-{size}-MAX:", max(genList))
    #print(f"NS-Gen-{size}-MIN:", min(genList))
    #print(f"NS-Gen-{size}-MEDIAN:", median(genList))
    
    nsd=nsinit(size,dlp,True)
    m=nsranmes(ns,dlp)
    #m2=nsranmes(ns,dlp)
    
    #tracemalloc.start()
    #nsenc(ns,m)
    #print(f"NS-Enc-{size}:", tracemalloc.get_traced_memory())
    #tracemalloc.stop()
    
    tracemalloc.start()
    nsenc(nsd,m)
    print(f"NS-D-Enc-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    #c=nsenc(ns,m)
    #c2=nsenc(ns,m2)
    
    #tracemalloc.start()
    #nsdec(ns,c)
    #print(f"NS-Dec-{size}:", tracemalloc.get_traced_memory())
    #tracemalloc.stop()
    
    #tracemalloc.start()
    #nsreenc(ns,c)
    #print(f"NS-Re-Enc-{size}:", tracemalloc.get_traced_memory())
    #tracemalloc.stop()
    
    #tracemalloc.start()
    #nsadd(ns,c,c2)
    #print(f"NS-Add-{size}:", tracemalloc.get_traced_memory())
    #tracemalloc.stop()