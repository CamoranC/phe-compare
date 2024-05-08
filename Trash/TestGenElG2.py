# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 01:10:58 2024

@author: Christian
"""

import pyperf

runner = pyperf.Runner()
runner.timeit(name="ElG-Gen-1024", stmt="elg=elginit(1024)", setup=["from ElGG import elggen","from ElGG import elginit"])
runner.timeit(name="ElG-Gen-2048", stmt="elg=elginit(2048)", setup=["from ElGG import elggen","from ElGG import elginit"])
runner.timeit(name="ElG-Gen-3072", stmt="elg=elginit(3072)", setup=["from ElGG import elggen","from ElGG import elginit"])
runner.timeit(name="ElG-Gen-7680", stmt="elg=elginit(7680)", setup=["from ElGG import elggen","from ElGG import elginit"])