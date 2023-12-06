# Kyle Schipf Empirical Evidence Group Project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# initializing dataframe
df = pd.read_csv("data/finance.csv")


# Storing and computing ratios from Minnesota data on debts, spending, and revenue per year

minnesota_data = df.loc[df['State'] == 'MINNESOTA']
ratio = minnesota_data['Debt at end of fiscal year']/minnesota_data['Revenue']
ratio2 = minnesota_data['General expenditure']/minnesota_data['Revenue']


# plotting ratio 1

plt.plot(minnesota_data['Year'], ratio,'m--', label = 'Debt to Revenue Ratio')

# setting graph boundaries then printing the graph

listof_Xticks = np.arange(1992, 2023, 3)
plt.xticks(listof_Xticks)

listof_Yticks = np.arange(0.10, 0., 0.10)
plt.yticks(listof_Yticks)

plt.ylabel('Annual Debt to Revenue Ratio')
plt.xlabel('Year')
plt.title('Fiscal Debt Over Annual Revenue (in billions/year)')
plt.show()


# plotting ratio 2
plt.plot(minnesota_data['Year'], ratio2,'r-.', label = 'General Expenditure to Revenue Ratio')

# setting graph boundaries then printing the graph

listof_Xticks = np.arange(1992, 2023, 3)
plt.xticks(listof_Xticks)

listof_Yticks = np.arange(0.60, 1.15, 0.050)
plt.yticks(listof_Yticks)

plt.ylabel('Expenditure to Revenue Ratio')
plt.xlabel('Year')
plt.title('General Expenditure Over Annual Revenue (in billions/year)')
plt.show()





