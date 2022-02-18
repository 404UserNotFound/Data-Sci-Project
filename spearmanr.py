import numpy as np
from matplotlib import pyplot
from scipy.stats import pearsonr, stats, ttest_ind, ttest_rel, spearmanr
from scipy.stats import fisher_exact
import pandas as pd

"""
Exploring the relationship between socioeconomic status and heart disease deaths
@authors: Mihaela Brodetchi, Adam Strahan, Sean Whelan
The below code uses Spearman Rho with datasets where any empty fields are removed entirely.
"""

years = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999',
         '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
         '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
# Load in data with Pandas
for i in years:
    gdp = pd.read_csv('./Datasets/GDP.csv',
                      usecols=[i])
    heart = pd.read_csv('./Datasets/Health.csv',
                        usecols=[i])

    # calculate spearman r correlation
    coefficient, p_value = spearmanr(gdp, heart)

    print(i)
    print("coefficient and p-value:")
    print(coefficient)
    print(p_value)

    # interpret the result
    alpha = 0.05
    if p_value > alpha:
        # does not reject null hypothesis
        print('Samples are uncorrelated')
    else:
        # rejects null hypothesis
        print('Samples are correlated')
