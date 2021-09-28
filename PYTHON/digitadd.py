t = int(input())

for i in range(t):
    x = int(input())
    a=0
    while(x>0):
        r=x%10
        a+=r
        x=x//10
    print(a)
