#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3 ,random_state = 42)

### it's all yours from here forward!  
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
print clf.score(features_test,labels_test)
pred = clf.predict(features_test)

from sklearn.metrics import precision_score, recall_score
print precision_score(labels_test, pred)
print recall_score(labels_test, pred)

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
true_positive = 0
false_positive = 0
false_negative = 0
print len(predictions)
for i, j in zip(predictions, true_labels):
    if i == j == 1:
        true_positive += 1
    elif i == 1 and j == 0:
        false_positive += 1
    elif i == 0 and j == 1:
        false_negative += 1
print true_positive, false_positive, false_negative 