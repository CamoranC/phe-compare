# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 22:10:05 2024

@author: Christian
"""

import pickle
from GMG import gmenc
from BG import benc
from DGKG import denc
from NSG import nsenc
from SYYG import syyenc
from GMG import gmranmes
from BG import branmes
from DGKG import dranmes
from NSG import nsranmes
from SYYG import syyranmes
from PG import penc
from PG import pranmes


for size in [1024,2048,3072,7680]:
    #dlp = 160
    #if size==2048:
        #dlp=224
    #if size==3072:
        #dlp=256
    #if size==7680:
        #dlp=384
    length=500
    #msed=1023
    #msop=size-1
    #bblock=16
    #bms=15
    #dblock=16
    #dms=16
    #nsmsed=159
    #nsmsop=dlp-1
    l=8
    ms=1
    
    #with open(f'GM-{size}.pickle', 'rb') as file:
        #gm = pickle.load(file)       
    #with open(f'B-{size}-{bblock}.pickle', 'rb') as file:
        #b = pickle.load(file)
    #if size != 7680:
        #with open(f'DGK-{size}-{dlp}-{dblock}.pickle', 'rb') as file:
           # d = pickle.load(file)
        #dcl=list()
    #with open(f'NS-{size}-{dlp}.pickle', 'rb') as file:
        #ns = pickle.load(file)
    #with open(f'NS-D-{size}-{dlp}.pickle', 'rb') as file:
        #nsd = pickle.load(file)
    with open(f'SYY-{size}-{l}.pickle', 'rb') as file:
        syy = pickle.load(file)
        
    #with open(f'P-{size}.pickle', 'rb') as file:
       #p=pickle.load(file)
        
    #gmcled=list()
    #bcl=list()
    #nscled=list()
    #nsdcled=list()
    syycled=list()
    #pcl=list()
    
    #if size != 1024:
        #gmclop=list()
        #nsclop=list()
        #nsdclop=list()
        #syyclop=list()
    
    while length > 0:
        
        #pm=pranmes(p,ms)
        #pmc=penc(p,pm)
        #pcl.append(pmc)
        
        #gmmed=gmranmes(gm,msed)
        #gmced=gmenc(gm,gmmed)
        #gmcled.append(gmced)
        
        #bm=branmes(b,bms)
        #bc=benc(b,bm)
        #bcl.append(bc)
        
        #nsm=nsranmes(ns,nsmsed)
        #nsc=nsenc(ns,nsm)
        #nscled.append(nsc)
        
        #nsdm=nsranmes(nsd,nsmsed)
        #nsdc=nsenc(nsd,nsdm)
        #nsdcled.append(nsdc)
        
        syym=syyranmes(syy,ms)
        syyc=syyenc(syy,syym)
        syycled.append(syyc)
        #if size != 1024:
            
            #gmmop=gmranmes(gm,msop)
            #gmcop=gmenc(gm,gmmop)
            #gmclop.append(gmcop)
            
            #nsm=nsranmes(ns,nsmsop)
            #nsc=nsenc(ns,nsm)
            #nsclop.append(nsc)
            
            #nsdm=nsranmes(nsd,nsmsop)
            #nsdc=nsenc(nsd,nsdm)
            #nsdclop.append(nsdc)
            
            #syym=syyranmes(syy,msop)
            #syyc=syyenc(syy,syym)
            #syyclop.append(syyc)
        
        #if size != 7680:    
            #dm=dranmes(d,dms)
            #dc=denc(d,dm)
            #dcl.append(dc)
        print(f"{size}-{length}-1")
        length -=1
    
    #with open(f'./picklecl/P-{size}-{ms}.pickle','wb') as file:
        #pickle.dump(pcl,file)
    
    #with open(f'./picklecl/GM-c-{size}-{msed}.pickle', 'wb') as file:
        #pickle.dump(gmcled, file)
   # with open(f'./picklecl/B-c-{size}-{bblock}-{bms}.pickle', 'wb') as file:
       # pickle.dump(bcl, file)
    #with open(f'./picklecl/NS-c-{size}-{dlp}-{nsmsed}.pickle', 'wb') as file:
        #pickle.dump(nscled, file)
    #with open(f'./picklecl/NS-D-c-{size}-{dlp}-{nsmsed}.pickle', 'wb') as file:
        #pickle.dump(nsdcled, file)
    with open(f'./picklecl/SYY-c-{size}-{l}-{ms}.pickle', 'wb') as file:
        pickle.dump(syycled, file)
    #if size != 7680:
        #with open(f'./picklecl/DGK-c-{size}-{dlp}-{dblock}-{dms}.pickle', 'wb') as file:
            #pickle.dump(dcl, file)
    #if size != 1024:
        #with open(f'./picklecl/GM-c-{size}-{msop}.pickle', 'wb') as file:
            #pickle.dump(gmclop, file)
        #with open(f'./picklecl/NS-c-{size}-{dlp}-{nsmsop}.pickle', 'wb') as file:
            #pickle.dump(nsclop, file)
        #with open(f'./picklecl/NS-D-c-{size}-{dlp}-{nsmsop}.pickle', 'wb') as file:
            #pickle.dump(nsdclop, file)
        #with open(f'./picklecl/SYY-c-{size}-{l}-{msop}.pickle', 'wb') as file:
            #pickle.dump(syyclop, file)
    
    if size == 2048:
        #for bblock in [12,20]:
        #bblock=1024
            #bms=bblock-1
            #with open(f'B-{size}-{bblock}.pickle', 'rb') as file:
                #b = pickle.load(file)
            #bcl=list()
            #length=500
            #while length > 0:
                #bm=branmes(b,bms)
                #bc=benc(b,bm)
               # bcl.append(bc)           
                #length -=1
                #print(f"{size}-{length}-b")
            #with open(f'./picklecl/B-c-{size}-{bblock}-{bms}.pickle', 'wb') as file:
                #pickle.dump(bcl, file)
            
        #for msed in [511,1535]:           
            #gmcled=list()   
            #syycled=list()
            #length=500
            #while length > 0:       
                #gmmed=gmranmes(gm,msed)
                #gmced=gmenc(gm,gmmed)
                #gmcled.append(gmced) 
                
                #syym=syyranmes(syy,msed)
                #syyc=syyenc(syy,syym)
                #syycled.append(syyc)
                #length -=1       
                #print(f"{size}-{msed}-{length}-2")
            #with open(f'./picklecl/GM-c-{size}-{msed}.pickle', 'wb') as file:
                #pickle.dump(gmcled, file)
            #with open(f'./picklecl/SYY-c-{size}-{l}-{msed}.pickle', 'wb') as file:
                #pickle.dump(syycled, file)
            
        #for dblock in [12,20]:
            #dms = dblock
            #with open(f'DGK-{size}-{dlp}-{dblock}.pickle', 'rb') as file:
                #d = pickle.load(file)
            #dcl=list()
            #length=500
            #while length > 0:
                #dm=dranmes(d,dms)
                #dc=denc(d,dm)
                #dcl.append(dc)
                #length-=1
                #print(f"{size}-{dblock}-{length}-d")
            #with open(f'./picklecl/DGK-c-{size}-{dlp}-{dblock}-{dms}.pickle', 'wb') as file:
                #pickle.dump(dcl, file)
                
        #for nsmsed in [79,111]:
            #nscled=list()
            #nsdcled=list()
            #length=500
            #while length > 0:  
                #nsm=nsranmes(ns,nsmsed)
                #nsc=nsenc(ns,nsm)
                #nscled.append(nsc)
                
                #nsdm=nsranmes(nsd,nsmsed)
                #nsdc=nsenc(nsd,nsdm)
                #nsdcled.append(nsdc)
                #length-=1
                #print(f"{size}-{nsmsed}-{length}-ns")
            #with open(f'./picklecl/NS-c-{size}-{dlp}-{nsmsed}.pickle', 'wb') as file:
                #pickle.dump(nscled, file)
            #with open(f'./picklecl/NS-D-c-{size}-{dlp}-{nsmsed}.pickle', 'wb') as file:
                #pickle.dump(nsdcled, file)
                
        for l in [16,32]:
            #msed=1023
            with open(f'SYY-{size}-{l}.pickle', 'rb') as file:
                syy = pickle.load(file)
            syycled=list()
            length=500
            while length > 0: 
                syym=syyranmes(syy,ms)
                syyc=syyenc(syy,syym)
                syycled.append(syyc)
                length-=1
                print(f"{size}-{l}-syy")
            with open(f'./picklecl/SYY-c-{size}-{l}-{ms}.pickle', 'wb') as file:
                pickle.dump(syycled, file)
                