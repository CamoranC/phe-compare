# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 13:26:52 2024

@author: Christian
"""

import pyperf
import pickle


runner = pyperf.Runner()



for size in [1024,2048,3072,7680]:
    dlp=160
    if size==2048:
        dlp=224
    if size==3072:
        dlp=256
    if size==7680:
        dlp=384

    with open(f'ElG-{size}-{dlp}.pickle', 'rb') as file:
        elg = pickle.load(file)    
    runner.timeit(name=f"ElG-Gen-{size}-{dlp}", stmt=f"elggen(elg,{size},{dlp})", setup=["from ElGG import elggen"],globals={"elg":elg})