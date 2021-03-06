#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
from sklearn import svm
cf = svm.SVC(kernel = 'rbf',gamma = 'auto', C= 10000)
t0 = time()
cf.fit(features_train, labels_train)
print "training time:", round(time() - t0, 3), "s"
t1 = time()
pred = cf.predict(features_test)
print "prediction time:", round(time() - t1, 3), "s"
l = [0, 0]
for i in pred:
    if i == 0:
        l[0] = l[0] + 1
    else:
        l[1] = l[1] + 1
print l
print cf.score(features_test, labels_test)
#########################################################


