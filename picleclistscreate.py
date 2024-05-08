# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 21:42:13 2024

@author: Christian
"""

import pickle
import random
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
from ASHEG import asheinit
from SAHEG import saheinit
from SMHEG import smheinit

for size in [1024,2048,3072,7680]:
    dlp = 160
    if size==2048:
        dlp=224
    if size==3072:
        dlp=256
    if size==7680:
        dlp=384
    length = 2000
    l=8
    bblock=512
    ms=size-1
    dblock=32
    mds=31
    mbs=511
    mns=159
    
    with open(f'GM-{size}.pickle', 'rb') as file:
        gm = pickle.load(file)
    with open(f'B-{size}-{bblock}.pickle', 'rb') as file:
        b = pickle.load(file)
    if size != 7680:
        with open(f'DGK-{size}-{dlp}-{dblock}.pickle', 'rb') as file:
            d = pickle.load(file)
        dcl=list()
    with open(f'NS-{size}-{dlp}.pickle', 'rb') as file:
        ns = pickle.load(file)
    with open(f'NS-D-{size}-{dlp}.pickle', 'rb') as file:
        nsd = pickle.load(file)
    with open(f'SYY-{size}-{l}.pickle', 'rb') as file:
        syy = pickle.load(file)
    gmcl=list()
    bcl=list()
    nscl=list()
    nsdcl=list()
    syycl=list()
    
    while length > 0:
        gmm=gmranmes(gm,ms)
        gmc=gmenc(gm,gmm)
        gmcl.append(gmc)
        bm=branmes(b,mbs)
        bc=benc(b,bm)
        bcl.append(bc)
        if size != 7680:    
            dm=dranmes(d,mds)
            dc=denc(d,dm)
            dcl.append(dc)
        nsm=nsranmes(ns,mns)
        nsc=nsenc(ns,nsm)
        nscl.append(nsc)
        nsdm=nsranmes(nsd,mns)
        nsdc=nsenc(nsd,nsdm)
        nsdcl.append(nsdc)
        syym=syyranmes(syy,ms)
        syyc=syyenc(syy,syym)
        syycl.append(syyc)
        length-=1
    with open(f'./picklecl/GM-c-{size}-{ms}.pickle', 'wb') as file:
        pickle.dump(gmcl, file)
    with open(f'./picklecl/B-c-{size}-{bblock}-{mbs}.pickle', 'wb') as file:
        pickle.dump(bcl, file)
    if size != 7680:
        with open(f'./picklec/DGK-c-{size}-{dlp}-{dblock}-{mds}.pickle', 'wb') as file:
            pickle.dump(dcl, file)
    with open(f'./picklec/NS-c-{size}-{dlp}-{mns}.pickle', 'wb') as file:
        pickle.dump(nscl, file)
    with open(f'./picklec/NS-D-c-{size}-{dlp}-{mns}.pickle', 'wb') as file:
        pickle.dump(nsdcl, file)
    with open(f'./picklec/SYY-c-{size}-8-{ms}.pickle', 'wb') as file:
        pickle.dump(syycl, file)
    
    if size == 2048:
        for ms in [511,1535,2047]:
            gmcl=list()
            syycl=list()
            length=2000
            while length > 0:
                gmm=gmranmes(gm,ms)
                gmc=gmenc(gm,gmm)
                gmcl.append(gmc)
                syym=syyranmes(syy,ms)
                syyc=syyenc(syy,syym)
                syycl.append(syyc)
                length-=1
            with open(f'./picklecl/GM-c-{size}-{ms}.pickle', 'wb') as file:
                pickle.dump(gmcl, file)
            with open(f'./picklec/SYY-c-{size}-8-{ms}.pickle', 'wb') as file:
                pickle.dump(syycl, file)
        for syyblock in [16,64]:
            print("no")
