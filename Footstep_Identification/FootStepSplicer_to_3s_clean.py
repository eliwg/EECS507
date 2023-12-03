import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import step_helper
import sys, getopt
from scipy.fft import fft, fftfreq, irfft

#saves steps in groups of 3

#calibration values for speeds      
s1_m = 124.81679604984159
s1_std = 75.89886535726346
s2_m = 189.25135470267435
s2_std = 139.13613480504378
s3_m = 282.48456661221473
s3_std = 221.8841855393617
s4_m = 258.15943423056785
s4_std = 171.9854435777837

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
step_starts = []
step_size = 12
after_step = 15
data_path = "data/raw/"
f = open("data/steps_in_3s_clean/" + inputfile.strip(".txt") + "_steps.txt",'w')
speed = int(inputfile.split('P')[1][0])            
time = int(inputfile.split('_')[3][0] + inputfile.split('_')[3][1])   #length of sample




with open(data_path + inputfile, 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=',')
    sample_count = 0
    for ROWS in plotting:
        Y.append(int(ROWS[0]))
        X.append(int(sample_count))
        sample_count += 1
Y_step = Y.copy()

abs_mean = -1
abs_std = -1

if speed == 1:
    abs_mean = s1_m
    abs_std = s1_std
elif speed == 2: 
    abs_mean = s2_m
    abs_std = s2_std
elif speed == 3: 
    abs_mean = s3_m
    abs_std = s3_std
elif speed == 4: 
    abs_mean = s4_m
    abs_std = s4_std



window = deque()
i = 0
step_count = 0
triplet_count = 0
triplet = []
mean_thresh = abs_mean + 2*abs_std
shown = 0
while i < len(Y):
    # print("i, Y[i]: ", i, ", ", Y[i])
    # print(len(step))
    window.append(Y[i])
    if len(window) < step_size:
        #print(len(step))
        
        i += 1
    else:
        if step_helper.is_step(window,mean_thresh):
            if(i + after_step < len(Y)):                #check if step can be added
                for j in range(after_step):
                    i += 1
                    window.append(Y[i])
                step_starts.append(i-step_size-after_step+1) #get step start point
                #add step to triplet
                if step_helper.add_to_triplet(triplet, window, step_size+after_step):
                    triplet_count += 1

                    #add the extra features
                    t1 = step_starts[-2] - step_starts[-3] - step_size - after_step
                    t2 = step_starts[-1] - step_starts[-2] - step_size - after_step
                    start_trip = step_starts[-3]
                    end_trip = i
                    
                    data= np.array(Y[start_trip:end_trip])
                    
                    sig_noise_fft = fft(data)
                    sig_noise_amp = 2 / np.size(data) * np.abs(sig_noise_fft)
                    sig_noise_freq = np.abs(fftfreq(np.size(data), (end_trip - start_trip)/100/np.size(data)))
                    amp_values = step_helper.make_bucket(sig_noise_amp,sig_noise_freq)
                    step_helper.add_features_to_file(triplet,t1,t2,amp_values,speed,f)
                    # if shown < 1:
                    #     #print(str(start_trip) + " " + str(end_trip))
                    #     plt.plot(np.abs(sig_noise_freq), sig_noise_amp)
                    #     plt.xlabel("Frequency (Hz)")
                    #     plt.ylabel("Amplitude")
                    #     plt.title(inputfile.strip(".txt") + " dataset Frequency Domain")
                    #     plt.show()
                    #     print(sig_noise_freq)
                    #     shown +=1
                    #     print(amp_values)
                    
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


