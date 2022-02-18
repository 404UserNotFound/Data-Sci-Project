from matplotlib import pyplot
from scipy.stats import pearsonr
import pandas as pd

"""
Exploring the relationship between socioeconomic status and heart disease deaths
@authors: Mihaela Brodetchi, Adam Strahan, Sean Whelan
The below code uses Pearson's with datasets where any empty fields are kept with drop=True added to corrwith
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


p = gdp.corrwith(heart, method='pearson', drop=True)
print(p)