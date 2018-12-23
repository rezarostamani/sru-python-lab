n = int(input("Enter n:"))
k = int(input("Enter k:"))
josephus = list(range(1,n+1))
idx = 1
print(josephus)
while len(josephus) > 1:
    print(josephus[idx])
    del josephus[idx]
    idx = (idx + k - 1) % len(josephus)

print("the survivor is:",josephus)