# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:57:55 2024

@author: Christian
"""

import pyperf
from RSAG import rsainit
from RSAG import rsaranmes
from RSAG import rsaenc
import pickle

runner = pyperf.Runner()

with open("rsa.pickle", 'rb') as file:
    # Deserialize and retrieve the variable from the file
    rsa = pickle.load(file)
    size=7680
    ms=1023
    m=rsaranmes(rsa,ms)
    runner.timeit(name=f"RSA-Enc-{size}-{ms}", stmt="rsaenc(rsa,m)", setup=["from RSAG import rsaenc"], globals={"rsa":rsa,"m":m})
