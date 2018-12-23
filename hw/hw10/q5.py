import numpy as np

n = int(input("Enter n:"))
a = int(input("Enter a:"))
b = int(input("Enter b:"))

x = np.linspace(a,b,n)
y = x ** 2
s = [(y[i] + y[i+1]) * (b-a)/(2*n) for i in range(len(y)-1)]

intfx = np.sum(s)

print("integral result is:", intfx)
print("error is:", abs(intfx - (b**3 - a**3)/3))
