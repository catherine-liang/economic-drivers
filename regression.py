import matplotlib.pyplot as plt
import pandas as pd
import time
import csv
import numpy as np
import statsmodels.api as sm
import seaborn as sns

start = time.time()

df = pd.read_csv("hcvsincome.csv")
print(df.info())
reg = sm.formula.ols("2010 ~ ratio_mort_male", data = df).fit()

plt.figure(figsize = (15, 10))
plt.scatter(df.ratio_mort_male, df.change_votes)
plt.xlabel("Ratio Mort Male")
plt.ylabel("Proportion Change in Votes")
plt.title("Ratio Mort Male vs Proportion Change in Votes")
plt.plot([.6, 1.5], [reg.params[0] + reg.params[1] * .6, reg.params[0] + reg.params[1] * 1.5])
plt.show()

reg = sm.formula.ols("change_votes ~ ratio_mort_male + prop_catholic + prop_workers", data = df).fit()
print("\n\nUNWEIGHTED REGRESSION TABLE:")
print(reg.summary())

end = time.time()
print("Time: " + str(end-start))