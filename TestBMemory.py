# -*- coding: utf-8 -*-
"""
Created on Wed May  1 19:33:35 2024

@author: Christian
"""

from BG import binit
from BG import branmes
from BG import benc
from BG import bdec
from BG import breenc
from BG import badd
from BG import bgen
import tracemalloc
from statistics import median

for size in [1024,2048,3072,7680]:
    r=16
    b=binit(size,r)
    #genList=list()
    #for _ in range(0,10):
        #tracemalloc.start()
        #bgen(b,size)
        #(a,c)=tracemalloc.get_traced_memory()
        #tracemalloc.stop()
        #genList.append(c)
    #print(f"B-Gen-{r}-{size}-MAX:", max(genList))
    #print(f"B-Gen-{r}-{size}-MIN:", min(genList))
    #print(f"B-Gen-{r}-{size}-MEDIAN:", median(genList))
    
    m=branmes(b,r)
    m2=branmes(b,r)
    
    tracemalloc.start()
    benc(b,m)
    print(f"B-Enc-{r}-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    c=benc(b,m)
    c2=benc(b,m2)
    
    tracemalloc.start()
    bdec(b,c)
    print(f"B-Dec-{r}-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    tracemalloc.start()
    breenc(b,c)
    print(f"B-Re-Enc-{r}-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    tracemalloc.start()
    badd(b,c,c2)
    print(f"B-Add-{r}-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    if size==2048:
        for r in [12,20]:
            #b=binit(size,r)
            #genList=list()
            #for _ in range(0,10):
                #tracemalloc.start()
               #bgen(b,size)
                #(a,c)=tracemalloc.get_traced_memory()
                #tracemalloc.stop()
                #genList.append(c)
            #print(f"B-Gen-{r}-{size}-MAX:", max(genList))
            #print(f"B-Gen-{r}-{size}-MIN:", min(genList))
            #print(f"B-Gen-{r}-{size}-MEDIAN:", median(genList))
            
            m=branmes(b,r)
            m2=branmes(b,r)
            
            tracemalloc.start()
            benc(b,m)
            print(f"B-Enc-{r}-{size}:", tracemalloc.get_traced_memory())
            tracemalloc.stop()
            
            c=benc(b,m)
            c2=benc(b,m2)
            
            tracemalloc.start()
            bdec(b,c)
            print(f"B-Dec-{r}-{size}:", tracemalloc.get_traced_memory())
            tracemalloc.stop()
            
            tracemalloc.start()
            breenc(b,c)
            print(f"B-Re-Enc-{r}-{size}:", tracemalloc.get_traced_memory())
            tracemalloc.stop()
            
            tracemalloc.start()
            badd(b,c,c2)
            print(f"B-Add-{r}-{size}:", tracemalloc.get_traced_memory())
            tracemalloc.stop()