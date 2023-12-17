import numpy as np
import os
from esgtoolkit import esgcortest, simshocks
from time import time


n = 500

s0_par1 = simshocks(n = n, horizon = 3, frequency = "semi-annual",
family = 1, par = 0.2, par2= 0)

s0_par2 = simshocks(n = n, horizon = 3, frequency = "semi-annual", 
family = 1, par = 0.8, par2 = 0)

print(esgcortest(s0_par1))

print(esgcortest(s0_par2))


print(esgcortest(s0_par1, return_R_obj = True))

print(esgcortest(s0_par2, return_R_obj=True))