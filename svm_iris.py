#!/usr/bin/python3

from sklearn.datasets import load_iris

from  sklearn.svm import SVC
import numpy as np
import  matplotlib.pyplot as plt 

iris=load_iris()
# visualizing between sepal and target 

# taking only two features 
two_sepal=iris.data[:,:2]
# loading target 
target=iris.target

svmclf=SVC()
trained_svm=svmclf.fit(two_sepal,target)
# by default kernel is rbf
trained_svm.predict()
#making data 	available into two units 
"""
plt.scatter(two_sepal[:,0],two_sepal[:,1],c=target,cmap=plt.cm.coolwarm)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('Sepal Title')
plt.show()


#  now plotting  for petal length & petal width

#taking last two features
two_petal=iris.data[:,2:]

plt.scatter(two_petal[:,0],two_sepal[:,1],c=target,cmap=plt.cm.coolwarm)
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.title('petal Title')
plt.show()
"""
