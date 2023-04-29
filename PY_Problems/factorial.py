t = int(input("Enter test cases: "))

for i in range(t):
    x = int(input("Enter the number: "))
    a = 1
    while(x>0):
        a = a*x
        x = x-1

    print(a)