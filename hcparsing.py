import matplotlib.pyplot as plt
import pandas as pd
import time
import csv
import numpy as np

#source: FBI UCR

start = time.time()

yearstart = 2010
yearend = 2016

hcdf = pd.read_csv("Hate_Crimes.csv")
hcnp = hcdf.to_numpy()
print(len(hcdf))

nydf = pd.read_csv("NYAAW.csv")
nynp = nydf.to_numpy()
#print(nydf.info())

for i in range(1,len(nynp)):
    curr = nynp[i][1]                               #
    for j in range(1, len(hcnp)):
        if hcnp[j][0] in curr:
            print(curr)
            index = int(hcnp[j][1])-2001
            






end = time.time()
print("Time: " + str(end-start))