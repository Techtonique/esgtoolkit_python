import numpy as np
import os
from esgtoolkit import simdiff, simshocks
from time import time

print(f"\n ----- Running: {os.path.basename(__file__)}... ----- \n")

kappa = 1.5
V0 = theta = 0.04
sigma_v = 0.2
theta1 = kappa * theta
theta2 = kappa
theta3 = sigma_v

# OU

print("1 - Ornstein-Uhlenbeck process: ----------------- \n")
start = time()
sims = simdiff(
    n=1000,
    horizon=5,
    frequency="quarterly",
    model="OU",
    x0=V0,
    theta1=theta1,
    theta2=theta2,
    theta3=theta3,
)
print(f"Time taken: {time() - start}")

print(sims)

# GBM

print("2 - Geometric Brownian Motion: ----------------- \n")
start = time()
sims = simdiff(
    n=100,
    horizon=5,
    frequency="semi-annual",
    model="GBM",
    x0=V0,
    theta1=theta1,
    theta2=theta2,
    theta3=theta3,
)
print(f"Time taken: {time() - start}")

print(sims)

# GBM2
print("3 - Geometric Brownian Motion with input shock: ----------------- \n")
start = time()
eps0 = simshocks(n = 100, horizon = 5, frequency = "quarterly")
sim_GBM = simdiff(n = 100, horizon = 5, frequency = "quarterly",   
               model = "GBM", 
               x0 = 100, theta1 = 0.03, theta2 = 0.1, 
               eps = eps0)
print(f"Time taken: {time() - start}")
print(sim_GBM)


# GBM3
print("4 - Geometric Brownian Motion with input shock 2: ----------------- \n")
start = time()
eps0 = simshocks(n = 100, horizon = 5, frequency = "quarterly", seed=13)
sim_GBM = simdiff(n = 100, horizon = 5, frequency = "quarterly",   
               model = "GBM", 
               x0 = 100, theta1 = 0.03, theta2 = 0.1, 
               eps = eps0)
print(f"Time taken: {time() - start}")
print(sim_GBM)