#!/usr/bin/python3

import numpy as np
import pandas as pd
import  scipy.stats  as stats
import matplotlib.pyplot as plt
from  sklearn import  datasets, linear_model

# loading csv file 

data_frame=pd.read_csv("Housing.csv")

X=data_frame['price']
Y=data_frame['lotsize']

X=X.values.reshape(len(X),1)
Y=Y.values.reshape(len(Y),1)

#  now time for data spiliting  into testing sets
X_train=X[:-250]

X_test=X[-250:]
# spliting  targets into testing sets 

Y_train=Y[:-250]

Y_test=Y[-250:]


# ploting  output 

plt.scatter(X_test,Y_test,color='black')
plt.title('Test case data')
plt.xlabel('Size')
plt.ylabel('Price')
plt.xticks(())
plt.yticks(())

#plt.show()

#  Now  linear regression 

regr=linear_model.LinearRegression()
regr.fit(X_train,Y_train)
plt.plot(X_test,regr.predict(X_test),color='red',linewidth=3)

plt.show()


