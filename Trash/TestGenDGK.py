# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:17:11 2024

@author: Christian
"""

import pyperf

runner = pyperf.Runner()

runner.timeit(name="DGK-Gen-1024-160-32", stmt="dgen(dgk,1024,160,32)", setup=["from DGKG import dgen","from DGKG import dinit","dgk=dinit()"])
runner.timeit(name="DGK-Gen-2048-224-16", stmt="dgen(dgk,2048,224,16)", setup=["from DGKG import dgen","from DGKG import dinit","dgk=dinit()"])
runner.timeit(name="DGK-Gen-2048-224-32", stmt="dgen(dgk,2048,224,32)", setup=["from DGKG import dgen","from DGKG import dinit","dgk=dinit()"])
runner.timeit(name="DGK-Gen-2048-256-64", stmt="dgen(dgk,2048,224,64)", setup=["from DGKG import dgen","from DGKG import dinit","dgk=dinit()"])
runner.timeit(name="DGK-Gen-3072-256-32", stmt="dgen(dgk,3072,256,32)", setup=["from DGKG import dgen","from DGKG import dinit","dgk=dinit()"])
runner.timeit(name="DGK-Gen-7680-384-32", stmt="dgen(dgk,7680,384,32)", setup=["from DGKG import dgen","from DGKG import dinit","dgk=dinit()"])
