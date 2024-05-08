# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:04:51 2024

@author: Christian
"""
from GMG import gmenc
from ElGG import elgenc
from BG import benc
from DGKG import denc
from NSG import nsenc
from SYYG import syyenc
from GMG import gmranmes
from ElGG import elgranmes
from BG import branmes
from DGKG import dranmes
from NSG import nsranmes
from SYYG import syyranmes
from PG import penc
from PG import pranmes
import pickle

for size in [1024,2048,3072,7680]:
    #dlp=160
    ms=1
    #mselg=size-1
    #if size==2048:
        #dlp=224
    #if size==3072:
        #dlp=256
    #if size==7680:
        #=384
    
    #with open(f'P-{size}.pickle', 'rb') as file:
        #p=pickle.load(file)
    #mp=pranmes(p,ms)
    #cp=penc(p,mp)
    #with open(f'./picklec/P-{size}-{ms}.pickle','wb') as file:
        #pickle.dump(cp,file)
    
    #with open(f'ElG-{size}-{dlp}.pickle', 'rb') as file:
        #elg = pickle.load(file)
    #melg=elgranmes(elg,mselg)
    #celg=elgenc(elg,melg)
    #with open(f'./picklec/ElG-c-{size}-{dlp}-{mselg}.pickle', 'wb') as file:
        #pickle.dump(celg, file)
    
   # with open(f'GM-{size}.pickle', 'rb') as file:
        #gm = pickle.load(file)
    #mgm=gmranmes(gm,ms)
    #cgm=gmenc(gm,mgm)
    #with open(f'./picklec/GM-c-{size}-{ms}.pickle', 'wb') as file:
        #pickle.dump(cgm, file)
        
    #rblock=16
    #rms=15
    #with open(f'B-{size}-{rblock}.pickle', 'rb') as file:
        #b = pickle.load(file)
    #mb=branmes(b,rms)
    #cb=benc(b,mb)
    #with open(f'./picklec/B-c-{size}-{rblock}-{rms}.pickle', 'wb') as file:
        #pickle.dump(cb, file)
     
    #if size != 7680:
        #dblock=16
        #dms=16
        #with open(f'DGK-{size}-{dlp}-{dblock}.pickle', 'rb') as file:
            #d = pickle.load(file)
        #md=dranmes(d,dms)
        #cd=denc(d,md)
        #with open(f'./picklec/DGK-c-{size}-{dlp}-{dblock}-{dms}.pickle', 'wb') as file:
            #pickle.dump(cd, file)
        
    #nms=159
    #with open(f'NS-{size}-{dlp}.pickle', 'rb') as file:
        #ns = pickle.load(file)
    #mns=nsranmes(ns,ms)
    #cns=nsenc(ns,mns)
    #with open(f'./picklec/NS-c-{size}-{dlp}-{nms}.pickle', 'wb') as file:
        #pickle.dump(cns, file)
    
    lblock=8
    with open(f'SYY-{size}-{lblock}.pickle', 'rb') as file:
        syy = pickle.load(file)
    msyy=syyranmes(syy,ms)
    csyy=syyenc(syy,msyy)
    with open(f'./picklec/SYY-c-{size}-{lblock}-{ms}.pickle', 'wb') as file:
        pickle.dump(csyy, file)
    
    if size==2048:
        #for ms in [511,1023,1535,2047]:
            #with open(f'ElG-{size}-{dlp}.pickle', 'rb') as file:
                #elg = pickle.load(file)
            #melg=elgranmes(elg,ms)
            #celg=elgenc(elg,melg)
            #with open(f'./picklec/ElG-c-{size}-{dlp}-{ms}.pickle', 'wb') as file:
                #pickle.dump(celg, file)
        
            #with open(f'GM-{size}.pickle', 'rb') as file:
               # gm = pickle.load(file)
            #mgm=gmranmes(gm,ms)
            #cgm=gmenc(gm,mgm)
            #with open(f'./picklec/GM-c-{size}-{ms}.pickle', 'wb') as file:
                #pickle.dump(cgm, file)
                
            #lblock=8
            #with open(f'SYY-{size}-{lblock}.pickle', 'rb') as file:
                #syy = pickle.load(file)
            #msyy=syyranmes(syy,ms)
            #csyy=syyenc(syy,msyy)
            #with open(f'./picklec/SYY-c-{size}-{rblock}-{ms}.pickle', 'wb') as file:
                #pickle.dump(csyy, file)
        #for rblock in [12,20]:
            #rblock=1024
            #rms=rblock-1
            #with open(f'B-{size}-{rblock}.pickle', 'rb') as file:
                #b = pickle.load(file)
            #mb=branmes(b,rms)
            #cb=benc(b,mb)
            #with open(f'./picklec/B-c-{size}-{rblock}-{rms}.pickle', 'wb') as file:
                #pickle.dump(cb, file)
        
        #for dblock in [12,20]:
            #if dblock == 16:
                #dms=15
                #with open(f'DGK-{size}-{dlp}-{dblock}.pickle', 'rb') as file:
                    #d = pickle.load(file)
                #md=dranmes(d,dms)
                #cd=denc(d,md)
                #with open(f'./picklec/DGK-c-{size}-{dlp}-{dblock}-{dms}.pickle', 'wb') as file:
                    #pickle.dump(cd, file)
            #if dblock == 32:
                #dms=31
                #with open(f'DGK-{size}-{dlp}-{dblock}.pickle', 'rb') as file:
                    #d = pickle.load(file)
               #md=dranmes(d,dms)
                #cd=denc(d,md)
                #with open(f'./picklec/DGK-c-{size}-{dlp}-{dblock}-{dms}.pickle', 'wb') as file:
                    #pickle.dump(cd, file)
                
            #if dblock == 64:
                #for dms in [15,31,63]:
                     #with open(f'DGK-{size}-{dlp}-{dblock}.pickle', 'rb') as file:
                         #d = pickle.load(file)
                    # md=dranmes(d,dms)
                    # cd=denc(d,md)
                    # with open(f'./picklec/DGK-c-{size}-{dlp}-{dblock}-{dms}.pickle', 'wb') as file:
                         #pickle.dump(cd, file)
            #dms=dblock
            #with open(f'DGK-{size}-{dlp}-{dblock}.pickle', 'rb') as file:
                #d = pickle.load(file)
            #md=dranmes(d,dms)
            #cd=denc(d,md)
            #with open(f'./picklec/DGK-c-{size}-{dlp}-{dblock}-{dms}.pickle', 'wb') as file:
                #pickle.dump(cd, file)
            
        #for nms in [79,111,223]:
            #with open(f'NS-{size}-{dlp}.pickle', 'rb') as file:
                #ns = pickle.load(file)
            #mns=nsranmes(ns,ms)
            #cns=nsenc(ns,mns)
            #with open(f'./picklec/NS-c-{size}-{dlp}-{nms}.pickle', 'wb') as file:
                #pickle.dump(cns, file)
        
        for lblock in [16,32]:
            with open(f'SYY-{size}-{lblock}.pickle', 'rb') as file:
                syy = pickle.load(file)
            msyy=syyranmes(syy,ms)
            csyy=syyenc(syy,msyy)
            with open(f'./picklec/SYY-c-{size}-{lblock}-{ms}.pickle', 'wb') as file:
                pickle.dump(csyy, file)