import math
a = []
t = int(input("Enter number of elements: "))
if t < 2:
    print("Invalid input")
else:
    for i in range(t):
        x = int(input("Enter Number: "))
        a.append(x)
    print("list = ",a)
a.sort()
print("Smallest element is",a[0])