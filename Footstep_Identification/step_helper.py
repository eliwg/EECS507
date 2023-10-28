from collections import deque
import numpy as np


#this file provides some helper functions for FootStepSplicer.py


#at calcs mean and std of abs(window)
#do I really need this function anymore?
def calc_std(window_):
    window = window_.copy()
    sum = 0
    
    #get mean
    for i in window:
        sum += abs(i)
    mean = sum / len(window)
    
    #get sum portion of std eq: sum( (x-mean)^2 )
    denominator = 0
    for i in window:
        denominator += pow(abs(i)-mean,2)

    q_std = np.sqrt(denominator/( len(window) - 1))
    return q_std, mean

# used for set threshold
# def is_step(window_, threshV, min_count):
#     window = window_.copy()
#     count = 0
#     while(not (len(window) == 0 )):
#         #print(len(step_q))
#         samp = window.popleft()
#         if abs(samp) > threshV:
#             count += 1
#             if count > min_count:
#                 return True
#     return False

#determines if slideing window is step
#detemination based on window mean vs mean of
#entire sample
def is_step(window_, mean_thresh):
    window = window_.copy()
    std, mean = calc_std(window)
    #mean = np.mean(abs(window))
    #print(abs(mean))
    if mean > mean_thresh:
        return True
    return False

#writes a step to file in csv  format
def add_step_to_file(window,f):
    for sample in window:
        f.write(str((sample))+',')
    f.write('\n')