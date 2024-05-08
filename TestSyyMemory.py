# -*- coding: utf-8 -*-
"""
Created on Sat May  4 01:10:18 2024

@author: Christian
"""


from SYYG import syyinit
from SYYG import syyranmes
from SYYG import syyenc
from SYYG import syydec
from SYYG import syyreenc
from SYYG import syymult
from SYYG import syygen
import tracemalloc
from statistics import median

for size in [1024,2048,3072,7680]:
    
    genList=list()
    for _ in range(0,10):
        tracemalloc.start()
        syyinit(size,8)
        (a,b)=tracemalloc.get_traced_memory()
        tracemalloc.stop()
        genList.append(b)
    print(f"SYY-Gen-{size}-MAX:", max(genList))
    print(f"SYY-Gen-{size}-MIN:", min(genList))
    print(f"SYY-Gen-{size}-MEDIAN:", median(genList))
    
    #m=syyranmes(syy,1)
    #m2=syyranmes(syy,1)
    
    #tracemalloc.start()
    #syyenc(syy,m)
    #print(f"SYY-Enc-{size}:", tracemalloc.get_traced_memory())
    #tracemalloc.stop()
    
    #c=syyenc(syy,m)
    #c2=syyenc(syy,m2)
    
    #tracemalloc.start()
    #syydec(syy,c)
    #print(f"SYY-Dec-{size}:", tracemalloc.get_traced_memory())
    #tracemalloc.stop()
    
    reencList=list()
    #for _ in range(0,10):
        #tracemalloc.start()
        #syyreenc(syy,c)
        #print(f"SYY-Re-Enc-{size}:", tracemalloc.get_traced_memory())
        #(a,b)=tracemalloc.get_traced_memory()
        #tracemalloc.stop()
        #reencList.append(b)
    #print(f"SYY-Re-{size}-MAX:", max(reencList))
    #print(f"SYY-Re-{size}-MIN:", min(reencList))
    #print(f"SYY-Re-{size}-MEDIAN:", median(reencList))
        
    #tracemalloc.start()
    #syymult(syy,c,c2)
    #print(f"SYY-x-{size}:", tracemalloc.get_traced_memory())
    #tracemalloc.stop()
    if size==2048:
        for l in [16,32]:
            syy=syyinit(size,l)
            genList=list()
            for _ in range(0,10):
                tracemalloc.start()
                syygen(syy,size)
                (a,b)=tracemalloc.get_traced_memory()
                tracemalloc.stop()
                genList.append(b)
            print(f"SYY-Gen-{size}-MAX:", max(genList))
            print(f"SYY-Gen-{size}-MIN:", min(genList))
            print(f"SYY-Gen-{size}-MEDIAN:", median(genList))
            
            #m=syyranmes(syy,1)
            #m2=syyranmes(syy,1)
            
            #tracemalloc.start()
            #syyenc(syy,m)
            #print(f"SYY-Enc-{size}:", tracemalloc.get_traced_memory())
            #tracemalloc.stop()
            
            #c=syyenc(syy,m)
            #c2=syyenc(syy,m2)
            
            #tracemalloc.start()
            #syydec(syy,c)
            #print(f"SYY-Dec-{size}:", tracemalloc.get_traced_memory())
            #tracemalloc.stop()
            
            #reencList=list()
            #for _ in range(0,10):
                #tracemalloc.start()
                #syyreenc(syy,c)
                #print(f"SYY-Re-Enc-{size}:", tracemalloc.get_traced_memory())
                #(a,b)=tracemalloc.get_traced_memory()
                #tracemalloc.stop()
                #reencList.append(b)
            #print(f"SYY-Re-{size}-MAX:", max(reencList))
            #print(f"SYY-Re-{size}-MIN:", min(reencList))
            #print(f"SYY-Re-{size}-MEDIAN:", median(reencList))
            
            #tracemalloc.start()
            #syymult(syy,c,c2)
            #print(f"SYY-x-{size}:", tracemalloc.get_traced_memory())
            #tracemalloc.stop()