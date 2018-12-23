ax = int(input("Enter ax:"))
ay = int(input("Enter ay:"))
bx = int(input("Enter bx:"))
by = int(input("Enter by:"))
cx = int(input("Enter cx:"))
cy = int(input("Enter cy:"))

ab = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5
ac = ((ax - cx) ** 2 + (ay - cy) ** 2) ** 0.5
bc = ((bx - cx) ** 2 + (by - cy) ** 2) ** 0.5

p = (ab + ac + bc) / 2

s = (p * (p-ab) * (p-ac) * (p-bc)) ** 0.5

print("Perimeter is:", 2 * p)

print("Area is:", s)
