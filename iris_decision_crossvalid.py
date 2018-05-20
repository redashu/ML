#/usr/bin/python3
from sklearn.datasets import load_iris

# loading iris datasets
iris=load_iris()
# loading features
iris_data=iris.data
# loading labels
iris_target=iris.target
# importing  sklearn cross_validation to split training and testing data
from sklearn.model_selection  import train_test_split

train_data,test_data,train_target,test_target=train_test_split(iris_data,iris_target,test_size=0.1)

# here 0.1 mean 90% for training and remaining half for testing
# calling decision tree 
from sklearn import tree
clf=tree.DecisionTreeClassifier()
trained=clf.fit(train_data,train_target)
predicted=trained.predict(test_data)
print(predicted)

# calculating accuracy 
from sklearn.metrics import accuracy_score
print(accuracy_score(test_target,predicted))
