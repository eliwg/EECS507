import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import sys, getopt
from scipy.fft import fft, fftfreq, irfft
import os



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
f = open("data/steps/" + inputfile.strip(".txt") + "_steps.txt",'w')

with open(data_path + inputfile, 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=',')
    sample_count = 0
    for ROWS in plotting:
        Y.append(int(ROWS[0]))
        X.append(int(sample_count))
        sample_count += 1

#convert samples to time
time = np.array(X)/100
volt_diff = np.array(Y)

yf = fft(volt_diff)
xf = fftfreq(np.size(time), 1 / 100)

# yf = yf * (abs(xf) < 40)
plt.plot(xf, np.abs(yf))
plt.show()

# filetered = irfft(yf)
# plt.plot(X,np.array(Y))
# plt.plot(filetered[0:6000])
# plt.show()
# plt.plot(X,abs(np.array(Y)))
# plt.plot(abs(filetered[0:6000]))
# plt.show()
