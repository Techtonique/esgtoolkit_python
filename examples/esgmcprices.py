import numpy as np
import os
import pandas as pd
from esgtoolkit import simdiff, simshocks, esgmcprices
from time import time

print(f"\n ----- Running: {os.path.basename(__file__)}... ----- \n")

r = 0.03

eps0 = simshocks(n = 100, horizon = 5, frequency = "semi-annual", 
                 return_R_obj=True)

sim_GBM = simdiff(n = 100, horizon = 5, frequency = "semi-annual",   
               model = "GBM", 
               x0 = 100, theta1 = 0.03, theta2 = 0.1, 
               eps = eps0, return_R_obj=True)

# convergence to a specific price
print(esgmcprices(r, sim_GBM, return_R_obj=True))
print(esgmcprices(r, sim_GBM, 2, return_R_obj=True))
print(esgmcprices(r, sim_GBM))
print(esgmcprices(r, sim_GBM, 2))


