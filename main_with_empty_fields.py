from matplotlib import pyplot
from scipy.stats import kendalltau
import pandas as pd

"""
Exploring the relationship between socioeconomic status and heart disease deaths
@authors: Mihaela Brodetchi, Adam Strahan, Sean Whelan
The below code uses Kendall Tau with datasets where any empty fields are kept and the NaN-policy is set to omit.
"""

# Load in data with Pandas
gdp = pd.read_csv('./Datasets/GDP_empty_vals.csv',
                  usecols=['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999',
                           '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
                           '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'])
heart = pd.read_csv('./Datasets/Health_empty_vals.csv',
                    usecols=['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999',
                             '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
                             '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'])

# print out summary of data
print(heart)
print(gdp)
# visualise data with scatter plots
pyplot.scatter(heart, gdp)
pyplot.show()

# calculate kendall tau correlation
coefficient, p_value = kendalltau(heart, gdp, nan_policy='omit')

print("coefficient and p-value with all decimal pts:")
print(coefficient)
print(p_value)

print('Kendall correlation coefficient rounded to 3 decimal pts: %.3f' % coefficient)
# interpret the result
alpha = 0.05
if p_value > alpha:
    # does not reject null hypothesis
    print('Samples are uncorrelated %.3f' % p_value)
else:
    # rejects null hypothesis
    print('Samples are correlated %.3f' % p_value)
