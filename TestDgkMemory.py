# -*- coding: utf-8 -*-
"""
Created on Mon May  6 18:56:52 2024

@author: Christian
"""
import pickle
from DGKG import dranmes
from DGKG import denc
from DGKG import ddec
from DGKG import dgen
from DGKG import dadd
from DGKG import dreenc
import tracemalloc
from statistics import median

for size in [1024,2048,3072]:
    dlp=160
    if size==2048:
        dlp=224
    if size==3072:
        dlp=256
    block=16
    ms=15
    with open(f'DGK-{size}-{dlp}-{block}.pickle', 'rb') as file:
        d = pickle.load(file)
    
    #genList=list()
    #for _ in range(0,2):
        #tracemalloc.start()
        #dgen(d,size,dlp)
        #(a,b)=tracemalloc.get_traced_memory()
        #tracemalloc.stop()
        #genList.append(b)
        
    #print(f"DGK-Gen-{size}-{block}-MAX:", max(genList))
    #print(f"DGK-Gen-{size}-{block}-MIN:", min(genList))
    #print(f"DGK-Gen-{size}-{block}-MEDIAN:", median(genList))
    
    m=dranmes(d,ms)
    m2=dranmes(d,ms)
    
    c=denc(d,m)
    c2=denc(d,m2)
    
    tracemalloc.start()
    denc(d,m)
    print(f"DGK-Enc-{size}-{block}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    tracemalloc.start()
    ddec(d,c)
    print(f"DGK-Dec-{size}-{block}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    tracemalloc.start()
    dadd(d,c,c2)
    print(f"DGK-Add-{size}-{block}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    tracemalloc.start()
    dreenc(d,c)
    print(f"DGK-Re-{size}-{block}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()

    if size==2048:
        for block in [12,20]:
            ms=block-1
            with open(f'DGK-{size}-{dlp}-{block}.pickle', 'rb') as file:
                d = pickle.load(file)
            #genList=list()
            #for _ in range(0,3):
                #tracemalloc.start()
                #dgen(d,size,dlp)
                #(a,b)=tracemalloc.get_traced_memory()
                #tracemalloc.stop()
                #genList.append(b)
                
            #print(f"DGK-Gen-{size}-{block}-MAX:", max(genList))
            #print(f"DGK-Gen-{size}-{block}-MIN:", min(genList))
            #print(f"DGK-Gen-{size}-{block}-MEDIAN:", median(genList))
            
            m=dranmes(d,ms)
            m2=dranmes(d,ms)
            
            c=denc(d,m)
            c2=denc(d,m2)
            
            tracemalloc.start()
            denc(d,m)
            print(f"DGK-Enc-{size}-{block}:", tracemalloc.get_traced_memory())
            tracemalloc.stop()
            
            tracemalloc.start()
            ddec(d,c)
            print(f"DGK-Dec-{size}-{block}:", tracemalloc.get_traced_memory())
            tracemalloc.stop()
            
            tracemalloc.start()
            dadd(d,c,c2)
            print(f"DGK-Add-{size}-{block}:", tracemalloc.get_traced_memory())
            tracemalloc.stop()
            
            tracemalloc.start()
            dreenc(d,c)
            print(f"DGK-Re-{size}-{block}:", tracemalloc.get_traced_memory())
            tracemalloc.stop()