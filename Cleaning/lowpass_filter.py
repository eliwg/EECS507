import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import sys, getopt
from scipy.signal import butter, filtfilt
import os


Y = []
X = []

data_path = "data/raw/"
clean_data_path = "data/clean/"
for file_name in os.listdir(data_path):
    f_path = os.path.join(data_path, file_name)
    if os.path.isfile(f_path):
        f = open(f_path,'r')
        runner = f_path.split('W')[1][0]                    # runner or null
        time = int(f_path.split('_')[3][0] + f_path.split('_')[3][1])   #length of sample
        new_file = f_path.split('/')[2]
        new_path = clean_data_path + new_file
        print(new_path)
        #convert to freq domain
        raw_data = csv.reader(f, delimiter=',')
        sample_count = 0
        for samp in raw_data:
            Y.append(int(samp[0]))
            X.append(int(sample_count))
            sample_count += 1
        
        #Butter
        # Filter requirements.
        T = 60        # Sample Period
        fs = 100.0       # sample rate, Hz
        cutoff = 37      # desired cutoff frequency of the filter, Hz ,      slightly higher than actual 1.2 Hz
        nyq = 0.5 * fs  # Nyquist Frequency
        order = 2       # sin wave can be approx represented as quadratic
        n = int(T * fs) # total number of samples
        data = np.array(Y)



        normal_cutoff = cutoff / nyq
        # Get the filter coefficients 
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        filtered = filtfilt(b, a, data)


        f_clean = open(new_path,'w')
        #write filtered data 
        for i in range(sample_count):
            f_clean.write(str(filtered[i]) + '\n')

        f_clean.close()
        f.close()

        # plt.plot(X,abs(np.array(Y)))
        # plt.show()
        # plt.plot(abs(filetered[0:6000]))
        # plt.show()


            
