import matplotlib.pyplot as plt
import csv

X = []
Y = []
 
with open('Geophone_Data.txt', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=',')
    sample_count = 0
    for ROWS in plotting:
        Y.append(int(ROWS[0]))
        X.append(sample_count)
        sample_count += 1
        
plt.plot(X, Y)
plt.title('Geophone Data')
plt.xlabel('Data Points (Approximately 25 Readings each Second)')
plt.ylabel('Voltage Value Post Gain Adjustment')
plt.show()