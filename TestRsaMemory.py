# -*- coding: utf-8 -*-
"""
Created on Fri May  3 00:59:43 2024

@author: Christian
"""

from RSAG import rsainit
from RSAG import rsaranmes
from RSAG import rsaenc
from RSAG import rsadec
from RSAG import rsamult
from RSAG import rsagen
import tracemalloc
from statistics import median

for size in [1024,2048,3072,7680]:
    rsa=rsainit(size)
    #genList=list()
    #for _ in range(0,10):
        #tracemalloc.start()
        #rsagen(rsa,size)
        #(a,b)=tracemalloc.get_traced_memory()
        #tracemalloc.stop()
        #genList.append(b)
    #print(f"RSA-Gen-{size}-MAX:", max(genList))
    #print(f"RSA-Gen-{size}-MIN:", min(genList))
    #print(f"RSA-Gen-{size}-MEDIAN:", median(genList))
    
    m=rsaranmes(rsa,size)
    m2=rsaranmes(rsa,size)
    
    tracemalloc.start()
    rsaenc(rsa,m)
    print(f"RSA-Enc-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    c=rsaenc(rsa,m)
    c2=rsaenc(rsa,m2)
    
    tracemalloc.start()
    rsadec(rsa,c)
    print(f"RSA-Dec-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    tracemalloc.start()
    rsamult(rsa,c,c2)
    print(f"RSA-XOR-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()