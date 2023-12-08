import numpy as np 
from esgtoolkit import calculatereturns

x = np.random.normal(size=10)

# convert R object to pandas dataframe
print(calculatereturns(x))