t = int(input())

for i in range(t):
    x = int(input())
    a = 1
    while(x>0):
        a = a*x
        x = x-1

    print(a)