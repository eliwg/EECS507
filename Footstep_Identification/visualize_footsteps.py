import csv
import matplotlib.pyplot as plt
import sys, getopt


#plots the step files with a uniform space between each step

inputfile = ""
argv = sys.argv[1:]
opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
for opt, arg in opts:
  if opt == '-h':
     print ('test.py -i <inputfile>')
     sys.exit()
  elif opt in ("-i", "--ifile"):
     inputfile = arg


Y = []
X = []
buffer = 15

with open(inputfile, 'r') as datafile:
    plotting = csv.reader(datafile, delimiter='\n')
    sample_count = 0
    row_count = 0
    for ROWS in plotting:
        samples = ROWS[0].split(",")
        for s in samples:
            if not (s == ''):
                Y.append(abs(int(s)))
                X.append(int(sample_count))
                sample_count += 1
        for i in range (buffer):
            Y.append(0)
            X.append(sample_count)
            sample_count += 1
    

plt.plot(X, Y)
plt.title('Steps Detected in ' + inputfile)
plt.xlabel('Data Points (15 dead points added between steps)')
plt.ylabel('Voltage Value from Geophone')
plt.show()
