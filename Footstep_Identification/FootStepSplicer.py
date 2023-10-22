import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import step_helper.py

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
while i < len(Y):
    if step.qsize() < step_size:
        step.append(Y[i])
        ++i
    else:
        step.append(Y[i])
        if is_step(step):
            #add to step
        else:
            step.pop()
            ++i
        
        
print(len(step))
        
    

print("number of samples: ", len(Y))