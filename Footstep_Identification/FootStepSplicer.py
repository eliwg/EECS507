import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import step_helper
import sys, getopt


inputfile = ""
argv = sys.argv[1:]
opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
for opt, arg in opts:
  if opt == '-h':
     print ('test.py -i <inputfile>')
     sys.exit()
  elif opt in ("-i", "--ifile"):
     inputfile = arg.split("/")[-1]

#idea 1 save last 10 samp if |5 samp| > 5000 -> step
#idea 2 is above easier than 10 samp abs moving avg
#idea 3 check stand dev above certain threshold

##########################
Y = []
Y_step = []
X = []
step_size = 15
#abs_threshold = 1500
data_path = "data/raw/"
f = open("data/steps/" + inputfile.strip(".txt") + "_steps.txt",'w')

with open(data_path + inputfile, 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=',')
    sample_count = 0
    for ROWS in plotting:
        Y.append(int(ROWS[0]))
        X.append(int(sample_count))
        sample_count += 1
Y_step = Y.copy()

window = deque()
i = 0
step_count = 0
mean_thresh = np.mean(Y) + np.std(Y)
while i < len(Y):
    # print("i, Y[i]: ", i, ", ", Y[i])
    # print(len(step))
    window.append(Y[i])
    if len(window) < step_size:
        #print(len(step))
        
        i += 1
    else:
        if step_helper.is_step(window,mean_thresh):
            #add to step
            step_helper.add_step_to_file(window,f)
            i +=1
            window.clear()
            step_count += 1
        else:
            # print("i: ", i )
            # print(len(step))
            window.popleft()
            Y_step[i] = 0
            i += 1
        
f.close()


# plt.plot(X, Y_step)
# plt.title('Geophone Data')
# plt.xlabel('Data Points (Approximately 25 Readings each Second)')
# plt.ylabel('Steps')
# plt.show()

print("number of steps detected: ", step_count)
        
    

print("number of samples: ", len(Y))