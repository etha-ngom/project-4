import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/finance.csv")

# Plotting mean Police Protection Expenditure per year
data = df.groupby("Year")["Police protection"].mean().reset_index()
x = data["Year"]
y = data["Police protection"]
plt.plot(x, y)
plt.xlabel("Year")
plt.ylabel("Police Protection Expenditure")
plt.title("Mean Police Protection Expenditure vs Year")
plt.show()

# To find correlation, I will use 1992 (the min average), 2019 (the max average),
# and 2004 (strange bump in the middle)

def plot_for_year(df, x_col, y_col, year):
    data = df[df["Year"] == year]
    x = data[x_col]
    y = data[y_col]

    r = data[[x_col, y_col]].corr().loc[x_col, y_col]
    r = round(r, 4)

    plt.scatter(x, y, color="navy")
    plt.xlabel(f"{x_col}")
    plt.ylabel(f"{y_col}")
    plt.title(f"{y_col} vs {x_col} ({year})")
    plt.text(0, data[y_col].max(), f"Pearson Correlation Coefficient (r): {r}")
    plt.show()

x_col = "Revenue"
y_col = "Police protection"
year_min = 1992
plot_for_year(df, x_col, y_col, year_min)

year_max = 2019
plot_for_year(df, x_col, y_col, year_max)

year_bump = 2004
plot_for_year(df, x_col, y_col, year_bump)