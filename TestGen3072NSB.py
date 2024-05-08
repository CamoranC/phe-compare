# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:39:23 2024

@author: Christian
"""

import pyperf

runner = pyperf.Runner()

size = 3072
dlp =256


runner.timeit(name=f"NS-Gen-{size}-{dlp}", stmt=f"nsgen(ns,{size},{dlp})", setup=["from NSG import nsgen","from NSG import nsinit","ns=nsinit()"])
runner.timeit(name=f"B-Gen-{size}-32", stmt=f"bgen(b,{size},32)", setup=["from BG import bgen","from BG import binit","b=binit()"])
