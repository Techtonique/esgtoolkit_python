import numpy as np
import os
import pandas as pd
from esgtoolkit import simdiff, simshocks, esgdiscountfactor
from time import time

print(f"\n ----- Running: {os.path.basename(__file__)}... ----- \n")

kappa = 1.5
V0 = theta = 0.04
sigma_v = 0.2
theta1 = kappa*theta
theta2 = kappa
theta3 = sigma_v

# OU
r = simdiff(n = 10, horizon = 5, 
            frequency = "quarterly",  
            model = "OU", 
            x0 = V0, theta1 = theta1, theta2 = theta2, theta3 = theta3, 
            return_R_obj = True)

res1 = esgdiscountfactor(r, 1)

print(isinstance(res1, pd.DataFrame))

# Stochastic discount factors
print(f"\n esgdiscountfactor(r, 1): \n {res1} \n")

# GBM
X = simdiff(
    n=10,
    horizon=5,
    frequency="quarterly",
    model="GBM",
    x0=V0,
    theta1=theta1,
    theta2=theta2,
    theta3=theta3,
    return_R_obj=True,
)

res2 = esgdiscountfactor(r, X, return_R_obj=True)

print(isinstance(res2, pd.DataFrame))

# Stochastic discount factors
print(f"\n esgdiscountfactor(r, X): \n {res2} \n")