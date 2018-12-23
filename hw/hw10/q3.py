n = int(input("Enter n:"))
m = int(input("Enter m:"))
for i in range(1, min(m,n) + 1):
    if (n % i) == (m % i) == 0:
        print(i)
