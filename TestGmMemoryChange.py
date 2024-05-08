# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 23:04:48 2024

@author: Christian
"""

from GMG import gminit
from GMG import gmranmes
from GMG import gmenc
from GMG import gmdec
from GMG import gmreenc
from GMG import gmxor
from GMG import gmgen
import random
import tracemalloc
from sympy import legendre_symbol
from Crypto.Util.number import getPrime



tracemalloc.start()
getPrime(512)
print("Prime", tracemalloc.get_traced_memory())
tracemalloc.stop()
    
