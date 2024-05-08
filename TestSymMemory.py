# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:54:53 2024

@author: Christian
"""

from ASHEG import asheinit
from ASHEG import asheranmes
from ASHEG import asheenc
from ASHEG import ashedec
from ASHEG import asheadd
from ASHEG import ashegen
from SAHEG import saheinit
from SAHEG import saheranmes
from SAHEG import saheenc
from SAHEG import sahedec
from SAHEG import saheadd
from SAHEG import sahegen
from SAHEG import sahemultk
from SMHEG import smheinit
from SMHEG import smheranmes
from SMHEG import smheenc
from SMHEG import smhedec
from SMHEG import smhemult
from SMHEG import smhegen
from SMHEG import smheexpk
import tracemalloc
from statistics import median
from random import randint
from random import choice
import copy

for size in [128,192]:
    ashe=asheinit(size)
    sahe=saheinit(size)
    smhe=smheinit(size)
    #genlistashe=list()
    #genlistsahe=list()
    #genlistsmhe=list()
    #for _ in range(0,10):
        #tracemalloc.start()
        #ashegen(ashe,size)
        #(a,b)=tracemalloc.get_traced_memory()
        #tracemalloc.stop()
        #genlistashe.append(b)
        
        #tracemalloc.start()
        #sahegen(sahe,size)
        #(a,b)=tracemalloc.get_traced_memory()
        #tracemalloc.stop()
        #genlistsahe.append(b)
        
        #tracemalloc.start()
        #smhegen(smhe,size)
        #(a,b)=tracemalloc.get_traced_memory()
        #tracemalloc.stop()
        #genlistsmhe.append(b)
    #print(f"ASHE-Gen-{size}-MAX:", max(genlistashe))
    #print(f"ASHE-Gen-{size}-MIN:", min(genlistashe))
    #print(f"ASHE-Gen-{size}-MEDIAN:", median(genlistashe))
    
    #print(f"SAHE-Gen-{size}-MAX:", max(genlistsahe))
    #print(f"SAHE-Gen-{size}-MIN:", min(genlistsahe))
    #print(f"SAHE-Gen-{size}-MEDIAN:", median(genlistsahe))
    
    #print(f"SMHE-Gen-{size}-MAX:", max(genlistsmhe))
    #print(f"SMHE-Gen-{size}-MIN:", min(genlistsmhe))
    #print(f"SMHE-Gen-{size}-MEDIAN:", median(genlistsmhe))
    
    
    
    mashe=asheranmes(ashe,127)
    mashe2=asheranmes(ashe,127)
    
    msahe=saheranmes(sahe,127)
    msahe2=saheranmes(sahe,127)
    
    msmhe=smheranmes(smhe,127)
    msmhe2=smheranmes(smhe,127)
    
    tracemalloc.start()
    asheenc(ashe,mashe)
    print(f"ASHE-Enc-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    cashe=asheenc(ashe,mashe)
    cashe2=asheenc(ashe,mashe2)
    
    tracemalloc.start()
    ashedec(ashe,cashe)
    print(f"ASHE-Dec-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    
    tracemalloc.start()
    asheadd(ashe,cashe,cashe2)
    print(f"ASHE-ADD-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    tracemalloc.start()
    saheenc(sahe,msahe)
    print(f"SAHE-Enc-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    csahe=saheenc(sahe,msahe)
    csahe2=saheenc(sahe,msahe2)
    
    tracemalloc.start()
    sahedec(sahe,csahe)
    print(f"SAHE-Dec-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    
    tracemalloc.start()
    saheadd(sahe,csahe,csahe2)
    print(f"SAHE-ADD-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    tracemalloc.start()
    smheenc(smhe,msmhe)
    print(f"SMHE-Enc-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    csmhe=smheenc(smhe,msmhe)
    csmhe2=smheenc(smhe,msmhe2)
    
    tracemalloc.start()
    smhedec(smhe,csmhe)
    print(f"SMHE-Dec-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    
    tracemalloc.start()
    smhemult(smhe,csmhe,csmhe2)
    print(f"SMHE-Mult-{size}:", tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
    for kb in [2,4,8]:
        k=randint(-(2**kb),2**kb)
        
        csahek=copy.deepcopy(csahe)
        csmhek=copy.deepcopy(csmhe)
        
        tracemalloc.start()
        sahemultk(sahe,csahek,k)
        print(f"SAHE-MultK-{size}-{kb}:", tracemalloc.get_traced_memory())
        tracemalloc.stop()
        
        tracemalloc.start()
        smheexpk(smhe,csmhek,k)
        print(f"SMHE-ExpK-{size}-{kb}:", tracemalloc.get_traced_memory())
        tracemalloc.stop()
        
    for loop in [5,10]:
        cashel=copy.deepcopy(cashe)
        csahel=copy.deepcopy(csahe)
        csmhel=copy.deepcopy(csmhe)
        cashel2=copy.deepcopy(cashe2)
        csahel2=copy.deepcopy(csahe2)
        csmhel2=copy.deepcopy(csmhe2)
        k=randint(-(2**4),2**4)
        for _ in range(0,loop):
            cashel=asheadd(ashe,cashel,cashel)
            csahel=saheadd(sahe,csahel,sahemultk(sahe,csahel,choice([-1,1])))
            csmhel=smhemult(smhe,csmhel,smheexpk(smhe,csmhel,choice([-1,1])))
            
            cashel2=asheadd(ashe,cashel2,cashel2)
            csahel2=saheadd(sahe,csahel2,sahemultk(sahe,csahel2,choice([-1,1])))
            csmhel2=smhemult(smhe,csmhel2,smheexpk(smhe,csmhel2,choice([-1,1])))
        
        tracemalloc.start()
        ashedec(ashe,cashel)
        print(f"ASHE-Dec-{size}-{loop}:", tracemalloc.get_traced_memory())
        tracemalloc.stop()
        
        tracemalloc.start()
        sahedec(sahe,csahel)
        print(f"SAHE-Dec-{size}-{loop}:", tracemalloc.get_traced_memory())
        tracemalloc.stop()
        
        tracemalloc.start()
        smhedec(smhe,csmhel)
        print(f"SMHE-Dec-{size}-{loop}:", tracemalloc.get_traced_memory())
        tracemalloc.stop()
        
        tracemalloc.start()
        asheadd(ashe,cashel,cashel2)
        print(f"ASHE-ADD-{size}-{loop}:", tracemalloc.get_traced_memory())
        tracemalloc.stop()
        
        tracemalloc.start()
        saheadd(sahe,csahel,csahel2)
        print(f"SAHE-ADD-{size}-{loop}:", tracemalloc.get_traced_memory())
        tracemalloc.stop()
        
        tracemalloc.start()
        smhemult(smhe,csmhel,csmhel2)
        print(f"SMHE-MULT-{size}-{loop}:", tracemalloc.get_traced_memory())
        tracemalloc.stop()
        
        tracemalloc.start()
        sahemultk(sahe,csahel,k)
        print(f"SAHE-MultK-{size}-{loop}:", tracemalloc.get_traced_memory())
        tracemalloc.stop()
        
        tracemalloc.start()
        smheexpk(smhe,csmhel,k)
        print(f"SMHE-ExpK-{size}-{loop}:", tracemalloc.get_traced_memory())
        tracemalloc.stop()
        