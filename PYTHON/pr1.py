a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Enter 4th number: "))

if(a>d):
    f1 = a
else:
    f1 = d

if(b>c):
    f2 = b
else:
    f2 = c

if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")