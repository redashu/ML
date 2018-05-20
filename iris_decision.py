#/usr/bin/python3
from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
x=[0,50,100]

# loading iris datasets
iris=load_iris()
#features and labels collection or training data collection
# features
train_data=np.delete(iris.data,x,axis=0)
#labeles
train_target=np.delete(iris.target,x)

# testing data preparing
test_data=iris.data[x]

# calling  classifier
clf=tree.DecisionTreeClassifier()
trained=clf.fit(train_data,train_target)
predicted=trained.predict([[5.1 ,3.5, 1.4, 0.2]])
print(predicted)
