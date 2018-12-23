n = int(input("Enter n:"))
x = input("Enter x:")
m = int(input("Enter m:"))


s = 0
for i in range(len(x)):
    d = int(x[-1-i]) if x[-1-i] < "9" and x[-1-i] > "0" else ord(x[-1-i])-55
    s += d * n**i

y = ""
while s > 0:
    d = s % m
    ch = chr(55+d) if d >= 10 else str(d)
    y = ch + y
    s //= m
    
print("y = ", y)