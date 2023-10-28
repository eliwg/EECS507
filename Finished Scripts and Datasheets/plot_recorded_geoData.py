import matplotlib.pyplot as plt
import csv
import sys, getopt


inputfile = ""
rec_length = 30
argv = sys.argv[1:]
opts, args = getopt.getopt(argv,"hi:o:",["ifile=","rec_length="])
for opt, arg in opts:
  if opt == '-h':
     print ('test.py -i <inputfile>')
     sys.exit()
  elif opt in ("-i", "--ifile"):
     inputfile = arg

X = []
Y = []
 
with open(inputfile, 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=',')
    sample_count = 0
    for ROWS in plotting:
        if abs(int(ROWS[0])) < 500:
            #Y.append(0)
            Y.append(int(ROWS[0]))
        else:
            Y.append(abs(int(ROWS[0])))
        X.append(sample_count)
        sample_count += 1
        
plt.plot(X, Y)
plt.title('Geophone Data')
plt.xlabel('Data Points (Approximately 25 Readings each Second)')
plt.ylabel('Voltage Value Post Gain Adjustment')
plt.show()