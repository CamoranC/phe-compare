# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:27:09 2024

@author: Christian
"""

from RSAG import rsainit
from GMG import gminit
from ElGG import elginit
from BG import binit
from DGKG import dinit
from NSG import nsinit
from SYYG import syyinit
from PG import pinit

import pickle

def create():
    for size in [7680]:
        dlp=160
        if size==2048:
            dlp=224
        if size==3072:
            dlp=256
        if size==7680:
            dlp=384
        #rsa=rsainit(size)
        #with open(f'RSA-{size}.pickle', 'wb') as file:
            #pickle.dump(rsa, file)
        #gm=gminit(size)
        #with open(f'GM-{size}.pickle', 'wb') as file:
            #pickle.dump(gm, file)
        #elg=elginit(size,dlp)
        #with open(f'ElG-{size}-{dlp}.pickle', 'wb') as file:
            #pickle.dump(elg, file)
        #elga=elginit(size,dlp,True)
        #with open(f'ElG-A-{size}-{dlp}.pickle', 'wb') as file:
             #pickle.dump(elga, file)
        #b=binit(size,16)
        #with open(f'B-{size}-16.pickle', 'wb') as file:
             #pickle.dump(b, file)
        dgk=dinit(size,dlp,16)
        with open(f'DGK-{size}-{dlp}-16.pickle', 'wb') as file:
             pickle.dump(dgk, file)
        #ns=nsinit(size,dlp)
        #with open(f'NS-{size}-{dlp}.pickle', 'wb') as file:
            #pickle.dump(ns, file)
        #nsd=nsinit(size,dlp,True)
        #with open(f'NS-D-{size}-{dlp}.pickle', 'wb') as file:
            #pickle.dump(nsd, file)
        #syy=syyinit(size,8)
        #with open(f'SYY-{size}-8.pickle', 'wb') as file:
            #pickle.dump(syy, file)
        #p=pinit(size)
        #with open(f'P-{size}.pickle', 'wb') as file:
            #pickle.dump(p, file)
        
        #if size==2048:
            #bh=binit(size,20)
            #with open(f'B-{size}-20.pickle', 'wb') as file:
                #pickle.dump(bh, file)
           # bl=binit(size,12)
            #with open(f'B-{size}-12.pickle', 'wb') as file:
                #pickle.dump(bl, file)
            #bvl=binit(size,5)
            #with open(f'B-{size}-12.pickle', 'wb') as file:
                #pickle.dump(bvl, file)
            #dgkl=dinit(size,224,12)
            #dgkh=dinit(size,224,20)
            #with open(f'DGK-{size}-{dlp}-12.pickle', 'wb') as file:
                #pickle.dump(dgkl, file)
            #with open(f'DGK-{size}-{dlp}-20.pickle', 'wb') as file:
                #pickle.dump(dgkh, file)
            #dgkvl=dinit(size,224,5)
            #with open(f'DGK-{size}-{dlp}-5.pickle', 'wb') as file:
                #pickle.dump(dgkvl, file)
            #syym=syyinit(size,16)
            #syyh=syyinit(size,32)
            #with open(f'SYY-{size}-16.pickle', 'wb') as file:
                #pickle.dump(syym, file)
            #with open(f'SYY-{size}-32.pickle', 'wb') as file:
                #pickle.dump(syyh, file)
        
if __name__ == "__main__":
    create()
        