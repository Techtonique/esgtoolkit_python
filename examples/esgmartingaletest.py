import numpy as np
import os
import pandas as pd
from esgtoolkit import simdiff, simshocks, esgmartingaletest
from time import time

print(f"\n ----- Running: {os.path.basename(__file__)}... ----- \n")

r0 = 0.03
S0 = 100

eps0 = simshocks(n=100, horizon=3, frequency="quarterly", return_R_obj=True)

sim_GBM = simdiff(
    n=100,
    horizon=3,
    frequency="quarterly",
    model="GBM",
    x0=S0,
    theta1=r0,
    theta2=0.1,
    eps=eps0,
    seed=10,
    return_R_obj=True,
)

mc_test = esgmartingaletest(r0, X=sim_GBM, p0=S0, alpha=0.05, return_R_obj=True)

print(mc_test)

mc_test2 = esgmartingaletest(
    r0, X=sim_GBM, p0=S0, alpha=0.05, return_R_obj=False
)

print(mc_test2)
