import numpy as np
import os 
from esgtoolkit import simshocks
from time import time

print(f"\n ----- Running: {os.path.basename(__file__)}... ----- \n")

# example 1

print("1 - shock 1: ----------")
start = time()
sims = simshocks(
    n=1000,
    horizon=5,
    frequency="quarterly")
print(f"Time taken: {time() - start}")

print(sims)

# example 2

print("2 - shock 2: ----------")
start = time()
sims = simshocks(
    n=100,
    horizon=5,
    frequency="semi-annual")
print(f"Time taken: {time() - start}")
print(type(sims))
print(sims)

# example 3

print("3 - shock 3: ----------")
start = time()
sims = simshocks(
    n=100,
    horizon=5,
    frequency="semi-annual")
print(f"Time taken: {time() - start}")
print(type(sims))
print(sims)
