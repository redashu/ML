#!/usr/bin/env python3

from sklearn.datasets import load_iris
import  numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
#from sklearn.model_selection import train_test_split
iris=load_iris()
# removing each set of flower element
remove=[0,50,100]
train_data=np.delete(iris.data,remove,axis=0)
train_target=np.delete(iris.target,remove)

test_data=iris.data[remove]

print(test_data)

gnb=GaussianNB()
mnb=MultinomialNB()

clfgnb=gnb.fit(train_data,train_target)
print(clfgnb.predict(test_data))
