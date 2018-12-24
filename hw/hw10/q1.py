import numpy as np
a = np.array([[0,0,0,1],[1,0,1,1],[1,0,0,1],[0,0,1,0]])
k = int(input("Enter k:"))
bk = np.zeros((4,4))
b = np.eye(4)

for i in range(k):
    b = np.matmul(a, b)
    bk += b 
    
print(bk)
