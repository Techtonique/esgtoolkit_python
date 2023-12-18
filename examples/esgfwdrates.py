import numpy as np
import os
import pandas as pd
from esgtoolkit import simdiff, simshocks, esgfwdrates
from time import time

print(f"\n ----- Running: {os.path.basename(__file__)}... ----- \n")

# Yield to maturities
txZC = [0.01422,0.01309,0.01380,0.01549,0.01747,0.01940,0.02104,0.02236,0.02348,
         0.02446,0.02535,0.02614,0.02679,0.02727,0.02760,0.02779,0.02787,0.02786,0.02776
         ,0.02762,0.02745,0.02727,0.02707,0.02686,0.02663,0.02640,0.02618,0.02597,0.02578,0.02563]

print(len(txZC))

# Observed maturities
u = [i for i in range(1,31)]

print(len(u))

fwd1 = esgfwdrates(in_maturities = u, 
                   in_zerorates = txZC, 
                   n = 10, 
                   horizon = 20, 
                   out_frequency = "semi-annual", 
                   method = "fmm", 
                   return_R_obj=True)

print(fwd1)

fwd2 = esgfwdrates(in_maturities = u, 
                   in_zerorates = txZC, 
                   n = 10, 
                   horizon = 20, 
                   out_frequency = "semi-annual", 
                   method = "fmm", 
                   return_R_obj=False)

print(fwd2)