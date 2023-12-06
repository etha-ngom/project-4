import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("finance.csv")

# the null hypothesis is that the ratio of education spending in florida over tax has remained constant since 1991
# the alternative is that the ratio of education spending in florida over tax has increased since 1991


# this function takes the parameters and produces a linear regression line of the fed in state
def make_linear_regression_plot(x,y,type,state):

    plt.title(state + ' ' + type + ' vs Tax Income')
    plt.xlabel('Tax in Hundred Millions')
    plt.ylabel(type)
    plt.scatter(x,y)
    b, a = np.polyfit(x, y, deg=1)
    xseq = np.linspace(x[:1], x[-2:], num=100)
    plt.plot(xseq, a + (b * xseq), color='k', lw=2.5)
    plt.show()
    print('Correlation Coefficient:',round(np.corrcoef(x, y)[0,1],4), state)


# function creates a graph of a ratio, in this case spending/revenue coming in
def ratio_spending_over_revenue(revenue, spending, year):
    plt.title("Ratio of Education Spending Over Tax Income Over Time")
    plt.ylabel("Ratio")
    plt.xlabel("Year")
    ratio = spending / revenue
    plt.scatter(year, ratio)
    plt.plot(year,ratio)
    plt.show()
    print("Correlation Coefficient:",round(np.corrcoef(ratio, year)[0,1],4))


# this makes a variable florida, that contains all of its data accessed through the name
florida = df.loc[df["State"]=='FLORIDA']

# this graphs florida tax and education spending as a scatter plit with their common points being the years and draws
# a linear regression line through the points
make_linear_regression_plot(florida['Tax'], florida['Education'], 'Education Spending',
                            'Florida')


ratio_spending_over_revenue(florida["Tax"], florida["Education"], florida["Year"])
plt.xlabel("Year")
plt.title("Money Spent on Education over the Years")
plt.ylabel("Education Spending in Ten Millions")
plt.scatter(florida["Year"], florida["Education"])
plt.plot(florida["Year"], florida["Education"])
plt.show()

plt.xlabel("Year")
plt.title("Tax Dollars Made over the Years")
plt.ylabel("Tax Dollars in 10 Millions")
plt.scatter(florida["Year"], florida["Tax"])
plt.plot(florida["Year"], florida["Tax"])
plt.show()

"""there is a 0.9974 positive, linear correlation between
 education spending in tens of millions, and the year.
 This is probably due to an increasing population and 
 increasing inflation. Unfortunately, due to a lack of data
 between 2004 and 2012, we can't see what may have been impacted
 by the 2008 crash. However, we can estimate that it would still have
 increased due to our line of linear regression."""

"""When looking at the data, there is evidence to reject the null, however I do it
 cautiously. I accept the null hypothesis that the ratio of education spending over tax
 income over the years in florida has increased since 1991. I accept this for two reasons:
 1. the line of linear regression comparing florida education spending and tax income
 results in a correlation coefficient of 0.9902. This number almost nearly confirms a positive
 and linear relationship between tax income and education spending. It shows that they both increase
 at a relative rate to each other. 2. that the ratio of tax income to education spending in relation
 to time also shows a positive linear relationship with a correlation coefficient of 0.8285. Although no line
 of linear regression was graphed for this relationship, the ratio was graphed over the years in which 
 it occurred. When calculating the correlation coefficient of that ratio we resulted in a fairly high
 high correlation that supports the relationship of education and tax. With these two points, I believe
 it is fair to reject the null hypothesis and consider the idea that the original ratio of education spending
 and tax income from 1991 has increased since then. Now I accept this cautiously for one reason, that being
 the gap in data between 2004 and 2012. The missing data has potential to skew the graphs and different
 correlation coefficients calculated. However, due to how strong those correlations were, I do still
 think it is a safe rejection to make."""


