import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("data/finance.csv")

year = df.loc[df["Year"] == 1996]

r = np.corrcoef(year['Health'], year['Parks Total Expenditure'])
r = str(r)
corr = ''
for i in range(13, 23):
    corr += r[i]


plt.plot(year['Health'], year['Parks Total Expenditure'], 'ro')
plt.ylabel("Parks Total Expenditure in USD")
plt.xlabel("Health Expenditure in millions of USD")
plt.axis((0, 6000000, 0, 500000))
plt.title("Health Expenditure vs Parks Expenditure in 1996")
plt.text(2000000, 400000, f'r (correlation coefficient) = {corr}')



plt.show()
