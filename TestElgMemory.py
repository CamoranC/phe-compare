# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:36:39 2024

@author: Christian
"""
from ElGG import elginit
from ElGG import elgranmesn
from ElGG import elgenc
from ElGG import elgdec
from ElGG import elgmult
from ElGG import elggen
from ElGG import elgadd
from ElGG import elgreenc
import tracemalloc
from statistics import median
import pickle

for size in [3072,7680]:
    dlp=160
    if size==2048:
        dlp=224
    if size==3072:
        dlp=256
    if size==7680:
        dlp=384
 
    with open(f'ElG-{size}-{dlp}.pickle', 'rb') as file:
        elg = pickle.load(file) 
    elga=elginit(size,dlp,True)
    print("done init")
    if size!=1024: 
        genList=list()
        for _ in range(0,1):
            tracemalloc.start()
            elggen(elg,size,dlp)
            (a,b)=tracemalloc.get_traced_memory()
            tracemalloc.stop()
            genList.append(b)
            
        print(f"ElG-Gen-{size}-MAX:", max(genList))
        print(f"ElG-Gen-{size}-MIN:", min(genList))
        print(f"ElG-Gen-{size}-MEDIAN:", median(genList))
    
    m=elgranmesn(elg)
    m2=elgranmesn(elg)
    
    ma=elgranmesn(elga)
    ma2=elgranmesn(elga)
    
    tracemalloc.start()
    elgenc(elg,m)
    print(f"ElG-Enc-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    tracemalloc.start()
    elgenc(elga,ma)
    print(f"ElG-A-Enc-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    c=elgenc(elg,m)
    c2=elgenc(elg,m2)
    
    ca=elgenc(elga,ma)
    ca2=elgenc(elga,ma2)
    
    tracemalloc.start()
    elgdec(elg,c)
    print(f"ElG-Dec-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    tracemalloc.start()
    elgmult(elg,c,c2)
    print(f"ElG-Mult-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    tracemalloc.start()
    elgadd(elga,ca,ca2)
    print(f"ElG-Add-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    tracemalloc.start()
    elgreenc(elg,c)
    print(f"ElG-Re-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()

    
