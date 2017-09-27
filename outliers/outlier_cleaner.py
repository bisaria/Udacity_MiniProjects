#!/usr/bin/python

import numpy as np
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    
    ### your code goes here
    error = abs(net_worths - predictions)
   
    # https://stackoverflow.com/questions/7851077/how-to-return-index-of-a-sorted-list
    cleaned_index = sorted(range(len(error)), key=lambda k: error[k])[0:81]
    
    error = list(error[cleaned_index])
    ages = list(ages[cleaned_index])
    net_worths = list(net_worths[cleaned_index])
    
    for i in range(81):
        cleaned_data.append((ages[i][0], net_worths[i][0], error[i][0]))
        
    return cleaned_data

