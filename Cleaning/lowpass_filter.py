import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import sys, getopt
from scipy.fft import fft, fftfreq, irfft
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
        #convert samples to time
        time = np.array(X)/time
        volt_diff = np.array(Y)

        #for null, take mean value of the 20 sec freq for footstep ID
        if(runner == 'n'):
            pass 

        yf = fft(volt_diff)
        xf = fftfreq(np.size(time), 1 / 100)

        #pass through lowpass
        yf = yf * (abs(xf) < 38)
        # plt.plot(xf, np.abs(yf))
        # plt.show()
        f_clean = open(new_path,'w')
        filetered = irfft(yf)
        
        #write filtered data 
        for i in range(sample_count):
            f_clean.write(str(filetered[i]))

        f_clean.close()
        f.close()

        # plt.plot(X,abs(np.array(Y)))
        # plt.show()
        # plt.plot(abs(filetered[0:6000]))
        # plt.show()


            
