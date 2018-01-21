#!/usr/bin/env python3

import  numpy as np
from sklearn.naive_bayes import GaussianNB

# training data
x=np.array([[-3,7],[1,5],[1,2],[-2,0],[2,3],[-4,0],[-1,1],[1,1],[-2,2],[2,7],[-4,1],[-2,7]])
y=np.array([3,3,3,3,4,3,3,4,3,4,4,4])

clfgnb=GaussianNB()

trained=clfgnb.fit(x,y)
output=trained.predict([[1,2],[3,4]])

print(output)
