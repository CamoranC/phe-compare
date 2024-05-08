# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:03:41 2024

@author: Christian
"""
import pyperf
import pickle

runner = pyperf.Runner()
size=1024
dlp=160
ms=159
with open(f'NS-{size}-{dlp}.pickle', 'rb') as file:
    ns = pickle.load(file)
with open(f'NS-c-{size}-{dlp}.pickle', 'rb') as file:
    cf = pickle.load(file)
runner.timeit(name=f"NS-RE-{size}-{dlp}-{ms}",stmt="nsreenc(ns,cf)",setup=["from NSG import nsreenc"],globals={"ns":ns,"cf":cf})