#!/usr/bin/python

from sklearn import  tree

# note here we have hoursepower and number of seats for sports and van
#features= [[300,2],[450,2],[150,8],[200,9]]

# here 1 for 2 seats and 0 for 9 seats
features= [[300,1],[450,1],[150,0],[200,0]]

# here we have lables for apple and bananas

labels=["sports","sports","van","van"]
#labels=[0,0,1,1]


clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
print  clf.predict([[600,1]])
