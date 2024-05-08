# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 01:02:50 2024

@author: Christian
"""
import pickle
from DGKG import dranmes
from DGKG import denc

for size in [1024,3072]:
    dblock=32
    dms=31
    if size == 1024:
        dlp=160
    else:
        dlp=256
    with open(f'DGK-{size}-{dlp}-{dblock}.pickle', 'rb') as file:
        d = pickle.load(file)
    md=dranmes(d,dms)
    cd=denc(d,md)
    with open(f'./picklec/DGK-c-{size}-{dlp}-{dblock}-{dms}.pickle', 'wb') as file:
        pickle.dump(cd, file)