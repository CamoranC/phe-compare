# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 00:05:03 2024

@author: Christian
"""

import pyperf
import pickle

runner = pyperf.Runner()

for size in [1024,2048]:
    dlp = 160
    if size==2048:
        dlp=226
    with open(f'NS-{size}-{dlp}.pickle', 'rb') as file:
        ns = pickle.load(file)
    runner.timeit(name=f"NS-Gen-{size}-{dlp}", stmt=f"nsgen(ns,{size},{dlp})", setup=["from NSG import nsgen"],globals={"ns":ns})