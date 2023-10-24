import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import step_helper

#idea 1 save last 10 samp if |5 samp| > 5000 -> step
#idea 2 is above easier than 10 samp abs moving avg
#idea 3 check stand dev above certain threshold

##########################
Y = []
step_size = 10
 
with open('Geophone_Data.txt', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=',')
    sample_count = 0
    for ROWS in plotting:
        Y.append(int(ROWS[0]))

step = deque()
i = 0
step_count = 0
while i < len(Y):
    # print("i, Y[i]: ", i, ", ", Y[i])
    # print(len(step))
    step.append(Y[i])
    if len(step) < step_size:
        #print(len(step))
        
        i += 1
    else:
        if step_helper.is_step(step,500,5):
            #add to step
            i += 10
            step.clear()
            step_count += 1
        else:
            # print("i: ", i )
            # print(len(step))
            step.popleft()
            i += 1
        
        
print(len(step))
        
    

print("number of samples: ", len(Y))