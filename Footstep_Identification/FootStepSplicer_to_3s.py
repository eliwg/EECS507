import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import step_helper
import sys, getopt

#saves steps in groups of 3


inputfile = ""
argv = sys.argv[1:]
opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
for opt, arg in opts:
  if opt == '-h':
     print ('test.py -i <inputfile>')
     sys.exit()
  elif opt in ("-i", "--ifile"):
     inputfile = arg.split("/")[-1]


Y = []
Y_step = []
X = []
step_size = 12
after_step = 15
data_path = "data/raw/"
f = open("data/steps_in_3s/" + inputfile.strip(".txt") + "_steps.txt",'w')

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
triplet_count = 0
triplet = []
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
            if(i + after_step < len(Y)):
                for j in range(after_step):
                    i += 1
                    window.append(Y[i])
                #add step to triplet
                if step_helper.add_to_triplet(triplet, window, step_size+after_step):
                    step_helper.add_step_to_file(triplet,f)
                    triplet_count += 1
                    triplet.clear()
                i +=1
                window.clear()
                step_count += 1
            else:
                i += after_step

            
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
print("number of triplets: ", triplet_count)

print("number of samples: ", len(Y))