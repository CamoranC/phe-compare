# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 23:27:03 2024

@author: Christian
"""

def eekinv(a:int, b:int)->int:
     s0=1
     s1=0
     t0=0
     t1=1
     while b != 0:
         q= a//b
         (a,b)=(b,a-q*b)
         (s0,s1)=(s1,s0-q*s1)
         (t0,t1)=(t1,t0-q*t1)
     if s0 < 0:
         s0=s0%b
     return s0