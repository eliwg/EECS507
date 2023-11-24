import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import sys, getopt
from scipy.fft import fft, fftfreq, irfft
from scipy.signal import butter, filtfilt
import os
import plotly.graph_objects as go



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
#f = open("data/steps/" + inputfile.strip(".txt") + "_steps.txt",'w')

with open(data_path + inputfile, 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=',')
    sample_count = 0
    for ROWS in plotting:
        Y.append(int(ROWS[0]))
        X.append(int(sample_count))
        sample_count += 1

# #convert samples to time
# time = np.array(X)/100
# volt_diff = np.array(Y)

# yf = fft(volt_diff)
# xf = np.abs(fftfreq(np.size(time), 1 / 100))

# # # yf = yf * (abs(xf) < 40)
# plt.plot(xf, np.abs(yf))
# plt.show()

# # filetered = irfft(yf)
# # plt.plot(X,np.array(Y))
# # plt.plot(filetered[0:6000])
# # plt.show()
# # plt.plot(X,abs(np.array(Y)))
# # plt.plot(abs(filetered[0:6000]))
# # plt.show()


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
y = filtfilt(b, a, data)
# plt.plot(np.linspace(0,np.size(y),np.size(y),endpoint=False),y)
# plt.show()

# fig = go.Figure()
# fig.add_trace(go.Scatter(
#             y = data,
#             line =  dict(shape =  'spline' ),
#             name = 'signal with noise'
#             ))
# fig.add_trace(go.Scatter(
#             y = y,
#             line =  dict(shape =  'spline' ),
#             name = 'filtered signal'
#             ))
# fig.show()


sig_noise_fft = fft(data)
sig_noise_amp = 2 / np.size(data) * np.abs(sig_noise_fft)
sig_noise_freq = np.abs(fftfreq(np.size(data), 60/np.size(data)))
# plt.plot(np.abs(sig_noise_freq), sig_noise_amp)
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Amplitude")
# plt.title(inputfile.strip(".txt") + " dataset Frequency Domain")
# #plt.show()
# plt.savefig("pictures/"+inputfile.strip(".txt")+"_FD.png")

# runner = inputfile.split('W')[1][0]  
# if(runner == 'n'):
print(np.std(np.abs(y)))