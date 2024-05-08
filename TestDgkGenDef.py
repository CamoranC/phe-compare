# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 11:26:05 2024

@author: Christian
"""
import pyperf
import pickle


runner = pyperf.Runner()

for size in [1024,2048,3072]:
    dlp=160
    if size==2048:
        dlp=224
    if size==3072:
        dlp=256
    block=16
    if size != 2048:
        with open(f'DGK-{size}-{dlp}-{block}.pickle', 'rb') as file:
            d = pickle.load(file)
        runner.timeit(name=f"DGK-Gen-{size}-{dlp}-{block}", stmt=f"dgen(d,{size},{dlp},{block})", setup=["from DGKG import dgen"],globals={"d":d})
    if size==2048:
        for block in [12,20]:
            with open(f'DGK-{size}-{dlp}-{block}.pickle', 'rb') as file:
                d = pickle.load(file)
            runner.timeit(name=f"DGK-Gen-{size}-{dlp}-{block}", stmt=f"dgen(d,{size},{dlp},{block})", setup=["from DGKG import dgen"],globals={"d":d})
