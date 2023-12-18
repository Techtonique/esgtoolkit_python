import numpy as np
import os
from esgtoolkit import simdiff, esgplotbands
from time import time

print(f"\n ----- Running: {os.path.basename(__file__)}... ----- \n")

kappa = 1.5
V0 = theta = 0.04
sigma_v = 0.2
theta1 = kappa * theta
theta2 = kappa
theta3 = sigma_v

# OU
start = time()
sims = simdiff(
    n=100,
    horizon=5,
    frequency="quarterly",
    model="OU",
    x0=V0,
    theta1=theta1,
    theta2=theta2,
    theta3=theta3,
    return_R_obj=True
)
print(f"Time taken: {time() - start}")

esgplotbands(sims)

