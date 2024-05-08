# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:17:38 2024

@author: Christian
"""

from NSG import nsranmes
from NSG import nsenc
import pickle

for size in [3072,7680]:
    dlp=256
    if size==7680:
        dlp=384
    ms=dlp-1
    with open(f'NS-{size}-{dlp}.pickle', 'rb') as file:
        ns = pickle.load(file)
    mns=nsranmes(ns,ms)
    cns=nsenc(ns,mns)
    with open(f'./picklec/NS-c-{size}-{dlp}-{ms}.pickle', 'wb') as file:
        pickle.dump(cns, file)
    with open(f'NS-D-{size}-{dlp}.pickle', 'rb') as file:
        ns = pickle.load(file)
    mns=nsranmes(ns,ms)
    cns=nsenc(ns,mns)
    with open(f'./picklec/NS-D-c-{size}-{dlp}-{ms}.pickle', 'wb') as file:
        pickle.dump(cns, file)