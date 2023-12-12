import numpy as np
from esgtoolkit import simdiff

kappa = 1.5
V0 = theta = 0.04
sigma_v = 0.2
theta1 = kappa * theta
theta2 = kappa
theta3 = sigma_v

# OU

sims = simdiff(
    n=7,
    horizon=5,
    frequency="quarterly",
    model="OU",
    x0=V0,
    theta1=theta1,
    theta2=theta2,
    theta3=theta3,
)

print(sims)

# GBM

sims = simdiff(
    n=7,
    horizon=5,
    frequency="semi-annual",
    model="GBM",
    x0=V0,
    theta1=theta1,
    theta2=theta2,
    theta3=theta3,
)

print(sims)
