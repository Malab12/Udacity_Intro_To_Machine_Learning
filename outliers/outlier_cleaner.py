#!/usr/bin/python

from operator import itemgetter
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    l = []
    for pred, age, worth in zip(predictions, ages, net_worths):
        a = age[0]
        w = worth[0]
        p = pred[0]
        
        tup = (a, w, pow(p - w, 2))
        #print tup
        l.append(tup)
    #print l
    l = sorted(l, key = itemgetter(2), reverse = True)
    cleaned = l[9:]
    cleaned_data = sorted(cleaned, key = itemgetter(0))
    ### your code goes here

    
    return cleaned_data
