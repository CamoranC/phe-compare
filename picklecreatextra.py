# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 18:29:17 2024

@author: Christian
"""

from ElGG import elginit
from BG import binit
import pickle

for size in [1024,2048,3072,7680]:
    dlp=160
    bsize=512
    if size==2048:
        dlp=224
    if size==3072:
        dlp=256
    if size==7680:
        dlp=384
    elg=elginit(size,dlp)
    with open(f'ElG-{size}-{dlp}.pickle', 'wb') as file:
        pickle.dump(elg, file)
    elga=elginit(size,dlp,True)
    with open(f'ElG-A-{size}-{dlp}.pickle', 'wb') as file:
        pickle.dump(elga, file)
    b=binit(size,bsize)
    with open(f'B-{size}-{bsize}.pickle', 'wb') as file:
        pickle.dump(b, file)
    if size==2048:
        bh=binit(size,1024)
        with open(f'B-{size}-1024.pickle', 'wb') as file:
            pickle.dump(bh, file)