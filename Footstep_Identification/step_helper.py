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

#writes a step(s) to file in csv  format
def add_step_to_file(window,f):
    count = 0
    for sample in window:
        if(count == len(window) - 1):
            f.write(str((sample))+'\n')
        else:
            f.write(str((sample))+',')
        count += 1

#adds step to triplet with buffer -- no buffer for now
def add_to_triplet(triplet, window, step_size):
    #buffer = 5
    while(not (len(window) == 0 )):
        triplet.append(window.popleft())
    #checks if triplet is full
    if len(triplet) == (3*step_size):# + ( 2 * buffer):
            return True
    # for i in range(buffer):
    #     triplet.append(0)
    return False




def make_bucket(sig_noise_amp,sig_noise_freq):
    pass
        



