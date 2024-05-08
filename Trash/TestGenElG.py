# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:26:54 2024

@author: Christian
"""

import pyperf

runner = pyperf.Runner()
runner.timeit(name="ElG-Gen-1024", stmt="elggen(elg,1024)", setup=["from ElGG import elggen","from ElGG import elginit","elg=elginit(6)"])
runner.timeit(name="ElG-Gen-2048", stmt="elggen(elg,2048)", setup=["from ElGG import elggen","from ElGG import elginit","elg=elginit(6)"])
runner.timeit(name="ElG-Gen-3072", stmt="elggen(elg,3072)", setup=["from ElGG import elggen","from ElGG import elginit","elg=elginit(6)"])
runner.timeit(name="ElG-Gen-7680", stmt="elggen(elg,7680)", setup=["from ElGG import elggen","from ElGG import elginit","elg=elginit(6)"])
#runner.timeit(name="ElG-Gen-2048", stmt="elggen(elg,2048)", setup=["from ElGG import elggen","from ElGG import elginit","elg=elginit(6)"])

