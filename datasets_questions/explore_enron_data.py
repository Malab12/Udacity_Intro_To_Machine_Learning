#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
name_list = enron_data.keys()
count_sal = 0
count_mail = 0
count_NaN = 0
count_poi = 0
for name in name_list:
    if enron_data[name]["poi"] == 1:
        count_poi = count_poi + 1
    if enron_data[name]["salary"] != 'NaN' :
        count_sal = count_sal + 1
    if enron_data[name]["email_address"] != 'NaN':
        count_mail = count_mail + 1
    if enron_data[name]["total_payments"] == 'NaN' and enron_data[name]["poi"] == 1:
        count_NaN = count_NaN + 1
print count_sal, count_mail, count_NaN, count_poi