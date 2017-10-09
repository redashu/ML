#!/usr/bin/python

from sklearn import  tree

# note here we have  weight and texture for apple and oranages
#features= [[140,"smooth"],[130,"smooth"],[150,"bumpy"],[160,"bumpy"]]

# here 1 for smooth and 0 for bumpy 
features= [[140,1],[130,1],[150,0],[160,0]]

# here we have lables for apple and bananas

labels=["apple","apple","orange","orange"]
#labels=[0,0,1,1]


clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
print  clf.predict([[145,0]])


"""
THis is supervised based approach by using ML and kind of method known as 
CLassifier method .

These specail type of problems that can be solved by Classification 
like : 
1.  To detect mail is a SPAM or NOT 
2.  Sports and normal car
3.  Difference between apple and orange 
"""


