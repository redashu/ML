#!/usr/bin/python3

from sklearn.datasets import load_digits
from  sklearn.svm import  SVC
import  numpy  as np
import  matplotlib.pyplot  as plt
digit=load_digits()

# defining features
f=np.delete(digit.data,-1,axis=0)
l=np.delete(digit.target,-1)
print(f.shape) 
print(l.shape) 
f1=digit.data[:-1]
l1=digit.target[:-1]
print(f1.shape)
print(l1.shape)

clf_svm=SVC()
trained=clf_svm.fit(f,l)
output=trained.predict(digit.data[-2].reshape(1,64))
print(output)

plt.imshow(digit.images[-2],cmap=plt.cm.gray_r,interpolation="nearest")
plt.show()


