import matplotlib.pyplot as plt
import csv
import socket
  
x = []
y = []
TCP_IP = '0.0.0.0'
TCP_PORT = 8888
BUFFER_SIZE = 20  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
  
while True:
    data = "".join(iter(lambda:conn.recv(1),"\n"))       
  
    if not data: break                
    for row in data:
        x.append(row[0])
        y.append(int(row[2]))
  
plt.bar(x, y, color = 'g', width = 0.72, label = "Faces")
plt.xlabel('TimeStamp')
plt.ylabel('Number of Faces')
plt.title('Number of faces on different timestamp')
plt.legend()
plt.show()

conn.close()
