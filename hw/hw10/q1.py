import numpy as np
a = np.array([[0,0,0,1],[1,0,1,1],[1,0,0,1],[0,0,1,0]])
k = int(input("Enter k:"))
bk = np.zeros((4,4))
for i in range(1, k+1):
    bk += a**i
print(bk)