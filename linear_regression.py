import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
"""
Exploring the relationship between socioeconomic status and heart disease deaths
@authors: Mihaela Brodetchi, Adam Strahan, Sean Whelan
The below code uses Pearson's with datasets where any empty fields are removed entirely
"""

X = pd.read_csv('./Datasets/GDP.csv',
                usecols=['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999',
                         '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
                         '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'])
y = pd.read_csv('./Datasets/Health.csv',
                usecols=['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999',
                         '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
                         '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'])

# split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,
                                                    random_state=1)

# create and train model using training set split
regression_model = linear_model.LinearRegression()
regression_model.fit(X_train, y_train)

# print coefficients as dataframe
coef_dataframe = pd.concat([pd.DataFrame(X.columns), pd.DataFrame(np.transpose(regression_model.coef_))], axis=1)
# save full output to csv
# cdf.to_csv('linear_reg.csv')
print(coef_dataframe)
print('Variance score: {}'.format(regression_model.score(X_test, y_test)))

# plot for residual error in test and training data
plt.style.use('fivethirtyeight')
plt.scatter(regression_model.predict(X_train), regression_model.predict(X_train) - y_train,
            color="green", s=10, label='Training data')
plt.scatter(regression_model.predict(X_test), regression_model.predict(X_test) - y_test,
            color="blue", s=10, label='Test data')

plt.hlines(y=0, xmin=0, xmax=50, linewidth=2)
plt.legend(loc='upper right')
plt.title("Residual error.")
plt.show()
