import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open(r'C:\Users\CC\Desktop\data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[0])
        y.append(int(row[2]))
  
plt.plot(x, y)
plt.xlabel('Timestamp')
plt.ylabel('Number of faces')
plt.title('Number of faces at different timestamp')

plt.show()