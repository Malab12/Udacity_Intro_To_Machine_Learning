#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from operator import itemgetter

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
data = sorted(data, key = itemgetter(1), reverse = True)
max_bonus = data[0][1]
print max_bonus
for person in data_dict:
    if data_dict[person]['bonus'] != 'NaN' and data_dict[person]['salary'] != 'NaN':
        if data_dict[person]['bonus'] >= 5000000 and data_dict[person]['salary'] >= 1000000:
            print person

    
print data_dict['LAY KENNETH L']['bonus']
